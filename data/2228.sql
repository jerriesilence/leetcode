# Write your MySQL query statement below

# return user_id 
# who made any 2 purchases at most 7 days apart
# ordered by user_id

select distinct user_id
  from purchases a
  left join purchases b using (user_id)
 where abs(datediff(a.purchase_date,b.purchase_date))<=7 and a.purchase_id <> b.purchase_id
 order by user_id;

