-- https://leetcode.com/problems/students-and-examinations/?envType=study-plan-v2&envId=top-sql-50

select s.student_id, s.student_name, sb.subject_name, count(e.subject_name) as attended_exams from Students s
join Subjects sb
left join Examinations e on s.student_id = e.student_id and sb.subject_name = e.subject_name
group by s.student_id, sb.subject_name
order by s.student_id, sb.subject_name