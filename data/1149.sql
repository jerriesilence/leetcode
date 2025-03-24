# Write your MySQL query statement below

# RETURN user 
# who viewed more than 1 article on the same date
#  order by id


select distinct viewer_id as id
  from views
  group by viewer_id, view_date
  having count(distinct article_id) >=2
  order by viewer_id