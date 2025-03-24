# CTE:
with cte as (
),
cte2 as (
)
select * from cte

# Time related
DATEDIFF(day, column1, column2) as  diff_days column2 - column1
date_trunc("year",'2023-04-28')  -- 2023-01-01
date_add(year, 1, '2023-03-01') --2024-03-01

# missing values
ifnull()
coalesce()

# if case
iff(condition, c1, c2)
case when dd then 
     when dd then 
     else 
     end

# window function
sum() over (partition by people order by date rows between 1 preceding and current row )
sum() over (partition by people order by date rows between UNBOUNDED preceding and current row )

sum() over (partition by col order by col rows between 1 preceding and current row)

sum() over (partition by col order by col rows between unbounded preceding and current tow)

sum(amount) over (order by visited_on rows between 6 PRECEDING and current row) as amount,


lead(column, 1) ignore nulls over (partition by col2 order by col3) # lead next row; lag previous row
lead(column,2) respect nulls over ()

first_value

ratio_to_report # shows the xx (%) wi

RANK() --gives you the ranking within your ordered partition. Ties are assigned the same rank, with the next ranking(s) skipped. So, if you have 3 items at rank 2, the next rank listed would be ranked 5.
/*
1
2
2
4
*/

DENSE_RANK() --again gives you the ranking within your ordered partition, but the ranks are consecutive. No ranks are skipped if there are ranks with multiple items.
/*
1
2
2
3
*/