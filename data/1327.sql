# Write your MySQL query statement below

# return names and ordered amount of products
# which have >= 100 units ordered in 2020 Feb

/*
select product_name, sum(unit) as unit
  from orders
  left join products using (product_id)
 where date_format(order_date,'%Y-%m') = '2020-02'
 group by 1
 having sum(unit) >= 100;
 */ 

--1316ms
 with cet as (
    select product_id, sum(unit) as unit
      from orders
     where year(order_date) = 2020 and month(order_date) = 2
     group by 1
     having sum(unit) >=100
 )
 select product_name, unit
   from cet
   left join productS using (product_id)
*/

 --1443
select product_name, sum(unit) as unit
  from orders
  left join products using (product_id)
 where year(order_date) = 2020 and month(order_date) = 2
 group by 1
 having sum(unit) >= 100;
 