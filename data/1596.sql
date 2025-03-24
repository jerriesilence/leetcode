# Write your MySQL query statement below

# return for each customer:
#   most frequently ordered products - product_id,product_name

select customer_id,
       product_id,
       product_name
  from (
    select  customer_id, 
            product_id,
            product_name,
            rank() over (partition by customer_id order by count(distinct order_date)  desc) as r
    from orders a
    left join products using(product_id)
    group by 1,2,3
  ) t
  where t.r = 1 

  
