# Write your MySQL query statement below

# return cumulative salary summary for every employee in a single unified table

# for each month that employee worked:
#   sum up the salaries in that month and the previous 2 months
#   if employee did not work for the company in previous months, 0

# do not include the 3-month sum for the most recent month taht the employee worked for 
# do not include the 3-month sum for any months the employee did not work.

# Order by id, month desc

with recursive t0 as (
    select 1 as month
    union
    select month+1 from t0 where month <12
),

e as (
    select 1 as id
    union
    select id+1 from e where id <(select max(id) from employee)
),
t as (
    select id,
           month
     from t0, e
),

t1 as (
    select id,
           month,
           salary,
           sum(salary) over (partition by id order by month desc rows between current row and 2 following) as three_month_Salary
      from t
      left join employee using (id, month)
),

t2 as (

    select id,
           month,
           three_month_Salary as salary,
           first_value(month) over (partition by id order by month desc) as recent_month
      from t1
     where t1.salary is not null
)
select id, month, salary
  from t2
 where t2.recent_month <> month

