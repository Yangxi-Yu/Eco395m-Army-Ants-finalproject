--Merge final and midterm job date tables
create table if not exists merge_job_post_date as (
select distinct * from job_post_date
union
select distinct * from job_post_date_midterm);