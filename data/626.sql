# Write your MySQL query statement below

# return a new seat table 
# every two consecutive students having their seats swapped
# odd: i + 1
# even i - 1
# if total number of student is odd, id of last student is not swapped

# q: does id always start at 1? assume yes

# if id always start at 1

with cte as (
    select id,
        student,
        count(*) over () as num_stu
    from seat
)

select case when num_stu % 2 = 1 and id = num_stu then id
            when id % 2 = 1 then id + 1
            when id % 2 = 0 then id - 1
            else null
            end as id,
        student
  from cte
  order by id

# if id does not start with 1

# 2,3,4,5,6: 5 stu, 
with cte as (
    select id,
        student,
        count(*) over () as num_stu，
        min(id) over () as min_id
    from seat
)
select case when num_stu % 2 = 1 and id = num_stu + min_id - 1 then id
            when id % 2 = 1 then id + if(min_id % 2 = 1, 1,-1)
            when id % 2 = 0 then id + if(min_id % 2 = 1, -1,1)
            else null
            end as id,
        student
  from cte
  order by id
