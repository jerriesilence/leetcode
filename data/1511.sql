# Write your MySQL query statement below

# report customer id and customer name
# for customers who spendt >= 100 in each month of june and july 2020

/*
with final_customer(customer_id, mth_cnt, min_month_total_price) as (
    select customer_id, count(distinct mth) as mth_cnt, min(month_total_price) as min_month_total_price 
    from 
        (select o.customer_id, month(o.order_date) as mth, sum(p.price * o.quantity) as month_total_price
        from orders o
        left join product p on o.product_id = p.product_id
        where order_date between '2020-06-01' and '2020-07-31'
        group by 1,2) x
    group by 1
    having mth_cnt = 2 and min_month_total_price >=100
) 
select t.customer_id, c.name
  from final_customer t
  left join customers  c on t.customer_id = c.customer_id
*/

select o.customer_id, c.name
  from orders o
  left join customers c using (customer_id)
  left join product p using (product_id)
 where o.order_date between '2020-06-01' and '2020-07-31'
  group by 1, 2
  having sum( if(month(order_date) = 6, quantity,0) * p.price ) >=100
     and sum( if(month(order_date) = 7, quantity,0) * p.price ) >=100;
