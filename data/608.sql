# Write your MySQL query statement below

# return note type


# if p_id is null: root
# if id is not in p_id, leaf
# else leaf

select t1.id, /*-- t1.p_id -- t2.id as k_id,*/
       case when t1.p_id is null then 'Root'
            when t2.id is null then 'Leaf'
            else 'Inner'
        end as type
  from tree t1
  left join tree t2 on t1.id = t2.p_id
  group by 1