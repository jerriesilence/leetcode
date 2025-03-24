# Write your MySQL query statement below

# return id and name of managers, # of emp report directly to them, avg of reports rounded to int


select man.reports_to as employee_id,
       emp.name,
       count(distinct man.employee_id) as reports_count,
       round(avg(rep.age)) as average_age
  from employees as man
  left join employees as emp on man.reports_to = emp.employee_id
  left join employees as rep on man.employee_id = rep.employee_id
  where man.reports_to is not null
  group by 1,2
  order by man.reports_to
  