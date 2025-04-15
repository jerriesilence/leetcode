-- longest winning streak

-- Write your PostgreSQL query statement below

-- Matches table:
-- +-----------+------------+--------+
-- | player_id | match_day  | result |
-- +-----------+------------+--------+
-- | 1         | 2022-01-17 | Win    |
-- | 1         | 2022-01-18 | Win    |
-- | 1         | 2022-01-25 | Win    |
-- | 1         | 2022-01-31 | Draw   |
-- | 1         | 2022-02-08 | Win    |
-- | 2         | 2022-02-06 | Lose   |
-- | 2         | 2022-02-08 | Lose   |
-- | 3         | 2022-03-30 | Win    |
-- +-----------+------------+--------+

-- 1 1 ->diff 0
-- 2 2        0
-- 3 3        0
-- 4 1        3
-- 5 1        4
-- 6 1        5
-- 7 2        5
-- 8 1        7
with wins as 
(
    select player_id, match_day, result, row_number() over (order by player_id, match_day) - row_number() over (partition by player_id, result order by match_day) as diff
      from matches
),

player_consecutive_wins as 
(
    select player_id, diff, count(*) as consecutive_win_cnt
      from wins
      where result = 'Win'
     group by 1,2
  )

select t1.player_Id, coalesce(max_win,0) as longest_streak
  from (select distinct player_id from matches) t1
  left join  (select player_id, max(consecutive_win_cnt) as max_win from player_consecutive_wins grou
