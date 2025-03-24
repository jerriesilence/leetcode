# Write your MySQL query statement below

# return for each user_id, product_id
# which the user spent the most money
# if multiple product_Ids, report all

with cte as (

    select user_id,
        product_id,
        sum(quantity*price) as total_price
    from sales
    left join product using (product_id)
    group by 1,2
)
select user_id, product_id 
  from (
    select user_id,
        product_id,
        total_price,
        max(total_price) over (partition by user_id) as max_total_price
    from cte
  ) t 
where t.total_price = t.max_total_price