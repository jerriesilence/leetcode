# prices of all products
# which is on 2019-08-16
# assume oroginal price before any changei s 10

select distinct 
       product_id, 
       first_value(new_price) over (partition by product_id order by change_date desc) as price
  from products
 where change_date <= '2019-08-16'

 union all

 select product_id, 
        10 as price
   from products
  group by product_Id
  having min(change_date) > '2019-08-16'

;

with cte as (
        select distinct 
            product_id, 
            first_value(new_price) over (partition by product_id order by change_date desc) as price
        from products
        where change_date <= '2019-08-16'
)
select distinct a.product_id, ifnull(cte.price,10) as price
  from products a
  left join cte using (product_id)