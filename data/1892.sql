-- Write your PostgreSQL query statement below
/*
page
- not like by the user
- like at least by 1 friend of the user

1. create all user - friend list
2. find potential pages that the current user not like
3. count the friend like for the potential pages.
*/


with all_user_friend as (
    SELECT 
        user1_id AS user_id, user2_id AS friend_user_id 
    FROM friendship
    UNION ALL
    SELECT 
        user2_id AS user_id, user1_id AS friend_user_id 
    FROM friendship
),


potential_page as (
select t.user_id, p.page_id
  from (select distinct user_id from all_user_friend) t
  cross join (select distinct page_id from likes) p
  left join likes l on t.user_id = l.user_id and p.page_id = l.page_id
  where l.user_id is null -- user not like this page
)

select pp.user_id, pp.page_id, count(distinct af.friend_user_id) as friends_likes 
  from potential_page pp
  left join all_user_friend af on pp.user_id = af.user_id
  join likes l on l.user_id = af.friend_user_id and l.page_id = pp.page_id
  group by 1,2
  order by pp.user_id, pp.page_id

-- select t.user_id, pp.page_id, count(distinct af.friend_user_id) as friends_likes
--   from all_user t
--   left join all_user_friend af on t.user_id = af.user_id
--   left join potential_page pp on t.user_id = pp.user_id
--   left join likes l on l.user_id = af.friend_user_id and l.page_id = pp.page_id
--   group by 1,2
