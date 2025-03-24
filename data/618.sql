# Write your MySQL query statement below


# create 3 tables with same id and join them together on id
# The test cases are generated so that the student number from America is not less than either Asia or Europe.

with t1 as (
    select row_number() over () as id,
           name as America
           from student
where  continent ='America'
order by America
),
t2 as (
        select row_number() over () as id,
           name as Asia
           from student
where  continent ='Asia'
order by Asia
),
t3 as (
        select row_number() over () as id,
           name as Europe
           from student
where  continent ='Europe'
order by Europe
)
select America,
       Asia,
       Europe
  from t1 a 
  left join t2  using (id)
  left join t3 using (id)