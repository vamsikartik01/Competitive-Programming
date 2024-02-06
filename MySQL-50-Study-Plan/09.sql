-- https://leetcode.com/problems/rising-temperature/?envType=study-plan-v2&envId=top-sql-50

-- method #1
select w1.id from Weather w1
where temperature > (
    select temperature from Weather w 
    where recordDate = DATE_SUB(w1.recordDate, INTERVAL 1 DAY)
)

-- using join
select w1.id from Weather w1
join Weather w2
on DATE_SUB(w1.recordDate, INTERVAL 1 DAY) = w2.recordDate
where w1.temperature > w2.temperature