--Merge job skill tables by title
create table if not exists merge_job_skill_counts_data_analyst as (
select distinct * from (
select * from job_skill_counts_data_analyst_final
union
select * from job_skill_counts_data_analyst_midterm)as merge_job_skill_counts_data_analyst
);

create table if not exists merge_job_skill_counts_data_engineer as (
select distinct * from (
select * from job_skill_counts_data_engineer_final 
union
select * from job_skill_counts_data_engineer_midterm)as merge_job_skill_counts_data_engineer
);


create table if not exists merge_job_skill_counts_data_scientist as (
select distinct * from (
select * from job_skill_counts_data_scientist_final 
union
select * from job_skill_counts_data_scientist_midterm)as merge_job_skill_counts_data_scientist
);

--Create a general table
create table if not exists merge_job_skill_counts as (
select distinct * from (
select * from merge_job_skill_counts_data_scientist
union
select * from merge_job_skill_counts_data_engineer
union
select * from merge_job_skill_counts_data_analyst)as merge_job_skill_counts
);