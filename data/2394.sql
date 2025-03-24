# Write your MySQL query statement below

# return employe id
# who did not work the needed hours

# the number of minutes in each session is rounded up

# !!! iff employee doesn work at all in logs, it will be NULL.

select employee_id   
  from employees
  left join logs using (employee_id)
  group by employee_id
  having ifnull(sum(ceiling(TIMESTAMPDIFF(second, in_time, out_time)/60)),0) < avg(needed_hours*60)
