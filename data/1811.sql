# Write your MySQL query statement below

# return name, email of user
# who meets at least 1 of the two conditions below:
# 1) won any medal in  3 or more consecutive contests
# 2) won the gold medal in 3 or more different contests (not necessarily consecutive)

# note: no contest id is skipped, any consetivie ids are consetives

# working but exceding time

with cte as (
select user_id,
       name,
       mail,
       contest_id,
       #if(gold_medal = user_id or silver_medal = user_id or bronze_medal = user_id,1,0) as contest_won,
       #if(gold_medal = user_id, 1, 0) as gold_won,
       sum(if(gold_medal = user_id or silver_medal = user_id or bronze_medal = user_id,1,0)) over (partition by user_id order by contest_id rows between 2 PRECEDING and current row ) as contest_won_cnt,
       sum(if(gold_medal = user_id, 1, 0)) over (partition by user_id) as gold_won_cnt
  from contests c, users u
)
select distinct name, mail
  from cte
 where contest_won_cnt = 3 or gold_won_cnt >=3


# working but exceding time
/*
with cte as (
select user_id,
       name,
       mail,
       contest_id,
       #if(gold_medal = user_id or silver_medal = user_id or bronze_medal = user_id,1,0) as contest_won,
       #if(gold_medal = user_id, 1, 0) as gold_won,
       sum(if(gold_medal = user_id or silver_medal = user_id or bronze_medal = user_id,1,0)) over (partition by user_id order by contest_id rows between 2 PRECEDING and current row ) as contest_won_cnt
       #sum(if(gold_medal = user_id, 1, 0)) over (partition by user_id) as gold_won_cnt
  from contests c, users u
)
select distinct name, mail
  from cte
 where contest_won_cnt = 3

union

select name, mail
  from users u1
  left join contests c1 on u1.user_id = c1.gold_medal
  group by name, mail
  having count(*) >=3
  */

with t0 as (
select contest_id, gold_medal as user_id
  from contests

union all

select contest_id, silver_medal as user_id
  from contests

union all

select contest_id, bronze_medal as user_id
  from contests
),

t1 as (

    select user_id, contest_id, row_number() over (partition by user_id order by contest_id) as rn
    from t0
)
select distinct name,mail
  from t1
  left join users using (user_id)
 group by name,mail, contest_id - rn
 having count(*) >=3 
 union 
select name, mail
  from users u1
  left join contests c1 on u1.user_id = c1.gold_medal
  group by name, mail
  having count(*) >=3
  