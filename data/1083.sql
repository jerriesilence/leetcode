# Write your MySQL query statement below

select buyer_id
  from sales
  left join product using (product_id)
  group by buyer_id
  having sum(if(product_name = 'S8',1,0)) > 0 and  sum(if(product_name = 'iPhone',1,0)) =0
