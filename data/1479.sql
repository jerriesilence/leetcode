# Write your MySQL query statement below


# return on each day of week:
    # in each category
        # how many units have been ordered
    
# order by category

# Assumption: if item category sells 0, do we need to show? no


select item_category as category,
       sum(if(weekday(order_date) = 0, quantity, 0)) as 'Monday',
       sum(if(weekday(order_date) = 1, quantity, 0)) as 'Tuesday',
       sum(if(weekday(order_date) = 2, quantity, 0)) as 'Wednesday',
       sum(if(weekday(order_date) = 3, quantity, 0)) as 'Thursday',
       sum(if(weekday(order_date) = 4, quantity, 0)) as 'Friday',
       sum(if(weekday(order_date) = 5, quantity, 0)) as 'Saturday',
       sum(if(weekday(order_date) = 6, quantity, 0)) as 'Sunday'       
  from items
  left join orders using (item_id)
  group by 1
  order by item_category;


SELECT *
  FROM orders
  left join 
    PIVOT (SUM(quantity) FOR dayname(order_date)  )
      AS p
  ORDER BY item_category;