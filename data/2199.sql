with words as (
    Select
    post_id,
    unnest(string_to_array(lower(content),' ')) as content -- content: str 'this is such a great book we love it', 
  -- string_to_array turns it into array (list, and unnest changes 1 row list to multiple rows (each row is a word)
    from
    Posts
),

post_topics as (
select distinct post_id, kw.topic_id
  from words w
  left join keywords kw on lower(kw.word) = w.content
)

-- select * from post_topics

select post_id, coalesce(string_agg(topic_id::varchar, ',' order by topic_id), 'Ambiguous!') as topic
       -- string_agg combine str of multiple rows into one row using ',' as seperator
  from post_topics
 group by 1
