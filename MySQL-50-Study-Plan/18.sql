-- https://leetcode.com/problems/percentage-of-users-attended-a-contest/?envType=study-plan-v2&envId=top-sql-50

select contest_id, ROUND((COUNT(DISTINCT user_id) * 100 / (SELECT COUNT(user_id) FROM Users)), 2) AS percentage
from Register
group by contest_id
order by percentage desc, contest_id