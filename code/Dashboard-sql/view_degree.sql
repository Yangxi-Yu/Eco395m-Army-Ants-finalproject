CREATE VIEW  job_degree AS
select *,
case when "degree" like '%bachelor%' then 'bachelor'
when "degree" like '%master%' then 'master'
when "degree" like '%phd%' then 'phd'
else 'not posted'
end as  required_degree
from merge_job_cleaned_description mjcd 