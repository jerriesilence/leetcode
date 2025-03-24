# Write your MySQL query statement below

# return:
#    for each pair of distinct persons: (p1, p2), (p1<p2)
#        the number of calls, total call duration 


select if(from_id < to_id, from_id, to_id) as person1,
       if(from_id < to_id, to_id, from_id) as person2,
       count(*) as call_count, -- if no null value, or 0 value to be taken care of
       sum(duration) as total_duration
  from calls
 group by person1, person2 