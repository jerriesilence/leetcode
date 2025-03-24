
# RETURN employees
# who hast op three unique slaries for that department


with cte as (
    select *,
           dense_rank() over (partition by departmentid order by salary desc) as rk
      from employee
)
select d.name as Department,
       e.name as Employee,
       Salary
  from cte e
  left join department d on e.departmentid = d.id
 where e.rk <= 3