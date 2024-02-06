-- https://leetcode.com/problems/article-views-i/description/?envType=study-plan-v2&envId=top-sql-50

select author_id as id from Views
where author_id = viewer_id
group by author_id
order by author_id