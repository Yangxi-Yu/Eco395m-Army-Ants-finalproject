CREATE VIEW t_job_type AS
select *,
case when "location" like '%Remote%' then 'Remote'
when "location" like '%Hybrid%' then 'Hybrid'
else 'In person'
end as  job_type
from job_basic_information_all 