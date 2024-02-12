-- https://leetcode.com/problems/monthly-transactions-i/submissions/1173135598/?envType=study-plan-v2&envId=top-sql-50

select substring(trans_date,1,7) as month, country, count(id) as trans_count, sum(
    case 
        when state = "approved" then 1 else 0
    end
) as approved_count, sum(amount) as trans_total_amount, sum(
    case
        when state = "approved" then amount else 0
    end
) as approved_total_amount
from Transactions 
group by month, country