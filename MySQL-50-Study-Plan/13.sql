-- https://leetcode.com/problems/managers-with-at-least-5-direct-reports/?envType=study-plan-v2&envId=top-sql-50

select e1.name 
from Employee e
join Employee e1
on e.managerId = e1.id
group by e.managerId
having count(e.managerId) >= 5