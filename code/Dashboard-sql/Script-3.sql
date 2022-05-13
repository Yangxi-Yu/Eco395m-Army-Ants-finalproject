create table job_degree as
select * from job_post_date_midterm jpdm 
union 
select * from job_post_date jpd2

select count(*),title,"location" ,"date" from job_basic1
group by title,"location","date"