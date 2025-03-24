# Write your MySQL query statement below

# return cancellation rate : # canceled requests with unbanded users / # requests with unbanded users on that day

## return cancellation rate of reuqests  with  unbanded users (noth not banned) each day 
## between 2013-10-01 and 2013-10-03

# round 2

select request_at as Day,
       round(sum(if(status IN ('cancelled_by_client', 'cancelled_by_driver'),1.0,0)) / count(*),2) as "Cancellation Rate"
  from trips t
  left join users d on d.users_id = t.driver_id
  left join users c on c.users_id = t.client_Id
  where d.banned = 'No' and c.banned = 'No'
    and request_at between '2013-10-01' and '2013-10-03'
 group by 1
 order by day
  