--At first create a bucket on our GCP and import midterm csv files.
--Merge final page html tables with midterm page html tables.
create table if not exists merge_searched_html_all as 
(select * from (
select * from merge_searched_job_html msjh
union
select * from old_merge_searched_job_html omsjh) as merge_searched_html_all
order by page,title,location);




