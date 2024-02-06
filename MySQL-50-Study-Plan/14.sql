-- https://leetcode.com/problems/confirmation-rate/submissions/1167967244/?envType=study-plan-v2&envId=top-sql-50

select s.user_id, ifnull(round(avg(action='confirmed'),2),0) as confirmation_rate
from Signups s
left join Confirmations c
on s.user_id = c.user_id
group by s.user_id