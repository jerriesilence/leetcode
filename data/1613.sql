# Write your MySQL query statement below

# return customer id
# who is not in the table but value between 1 and max(customer_id) (<100)
# order by id

with recursive cte as (
    select 1 as n # base case
      union
    select n+1 from cte # recursive
    where n<(select max(customer_id) from customers) # stop criteria
)

select n as ids
  from cte
 where n not in (select customer_id from customers)