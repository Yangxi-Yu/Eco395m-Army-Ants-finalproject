--merge job description html tables
create table if not exists merge_job_des_html as(
select * from job_des_html_data_analyst
union
select * from job_des_html_data_engineer
union
select * from job_des_html_data_scientist
union
select * from job_des_html_midterm_data_analyst
union
select * from job_des_html_midterm_data_engineer
union
select * from job_des_html_midterm_data_scientist);