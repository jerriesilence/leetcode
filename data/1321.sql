# Write your MySQL query statement below

/*
select visited_on, amount, round(amount/7,2) as average_amount
  from (
          select visited_on, 
                 sum(amt) over (ORDER BY visited_on asc ROWS BETWEEN 6 PRECEDING AND CURRENT ROW ) as amount,
                 row_number() over (order by visited_on asc) as cnt
            from
                (
                  select visited_on, sum(amount) as amt
                    from customer
                  group by visited_on) daily
            ) f
  where cnt>=7

*/

/*
SELECT 
       a.visited_on AS visited_on, SUM(b.day_sum) AS amount,
       ROUND(AVG(b.day_sum), 2) AS average_amount
FROM
  (SELECT visited_on, SUM(amount) AS day_sum FROM Customer GROUP BY visited_on ) a,
  (SELECT visited_on, SUM(amount) AS day_sum FROM Customer GROUP BY visited_on ) b
WHERE DATEDIFF(a.visited_on, b.visited_on) BETWEEN 0 AND 6
GROUP BY a.visited_on
HAVING COUNT(b.visited_on) = 7
*/
/*
select *
  from (SELECT visited_on, SUM(amount) AS day_sum FROM Customer GROUP BY visited_on ) a
  left join (SELECT visited_on, SUM(amount) AS day_sum FROM Customer GROUP BY visited_on ) b on DATEDIFF(a.visited_on, b.visited_on) BETWEEN 0 AND 6 # a.vistied_on - b.visited_on
  #group by a.visited_on
  #having count(b.visited_on) = 7

*/

# return average_amount (rounded to 2):
#    moving average of how much the customer paid in 7 days window (current day + 6 days before)
#    order by visited_on asce
# note: (there will be at least one customer every day).
--843
with cte as (
    select visited_on, sum(amount) as amount
    from customer
    group by 1
    order by 1 
)
select visited_on,
       sum(amount) over (order by visited_on rows between 6 preceding and current row) as amount,
       round(avg(amount) over (order by visited_on rows between 6 PRECEDING and current row),2) as average_amount
  from cte
 limit 6,999999999999999


--1093
with cte as (
select distinct visited_on,
       sum(amount) over (order by visited_on range between interval 6 day preceding and current row) as amount,
       min(visited_on) over() min_date
  from customer
) 
select visited_on, amount, round(amount/7,2) as average_amount
  from cte
 where visited_on >= min_date+6
 */

--917
with cte as (
    select visited_on, sum(amount) as amount
    from customer
    group by 1
    order by 1
)
select visited_on, amount, average_amount
  from (
    select visited_on,
           min(visited_on) over () as min_visited_on,
           sum(amount) over (order by visited_on rows between 6 PRECEDING and current row) as amount,
           round(avg(amount) over (order by visited_on rows between 6 PRECEDING and current row),2) as average_amount
    from cte
  )  t
   where t.visited_on >= t.min_visited_on+6
 