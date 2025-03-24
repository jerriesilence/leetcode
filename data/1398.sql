# Write your MySQL query statement below

# return cusotmer_id, customer name of customers
# who bought products "A", "B" but did notbuy "C"
# results order by customer_id

select customer_id, customer_name
  from orders
  left join customers using (customer_id)
 group by 1,2
 having sum(if(product_name = "A",1,0))>0
    AND sum(if(product_name = "B",1,0))>0
    AND sum(if(product_name = "C",1,0))=0