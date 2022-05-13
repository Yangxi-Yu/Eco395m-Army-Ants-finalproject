--Merge cleaned job description tables
create table merge_job_cleaned_description as (
select distinct * from(
select * from job_cleaned_description_final_data_analyst
union
select * from job_cleaned_description_final_data_engineer
union
select * from job_cleaned_description_final_data_scientist
union
select * from job_cleaned_description_midterm_data_analyst
union
select * from job_cleaned_description_midterm_data_engineer
union
select * from job_cleaned_description_midterm_data_scientist)as merge_job_cleaned_description);