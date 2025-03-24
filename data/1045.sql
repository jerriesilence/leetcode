# Write your MySQL query statement below

# return customer id
# who bought all products in product table


# assume all product_key in customer table exist in product table

select customer_id
  from customer
  group by customer_id
  having count(distinct product_key) = (select count(*) from product);
