-- https://leetcode.com/problems/employee-bonus/?envType=study-plan-v2&envId=top-sql-50

select e.name, b.bonus from Employee e
left join Bonus b
on e.empId = b.empId
where b.bonus < 1000 or b.bonus is null