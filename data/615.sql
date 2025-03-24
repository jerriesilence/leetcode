# Write your MySQL query statement below


# return comparison result of ()the average salary of employees in a department) to (company's average salary)

with t1 as (
    select date_format(pay_date,'%Y-%m') as pay_month,
        department_id,
        avg(amount) as depart_avg
    from salary
    left join employee using (employee_id)
    group by 1,2
),
t2 as (
    select date_format(pay_date,'%Y-%m') as pay_month,
           avg(amount) as company_avg
      from salary
     group by 1
)

select pay_month,
       department_id,
       case when depart_avg = company_avg then 'same'
            when depart_avg > company_avg then 'higher'
            when depart_avg < company_avg then 'lower'
            else null
            end as comparison
  from t1
  left join t2 using (pay_month)
       
