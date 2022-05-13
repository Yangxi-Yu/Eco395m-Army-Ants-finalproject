--Merge tables containing company name and industry
create table merge_cmp_industry as (
select distinct * from
(select distinct * from data_analyst_final_cmp_industry
union
select distinct * from data_analyst_midterm_cmp_industry
union
select distinct * from data_engineer_final_cmp_industry
union
select distinct * from data_engineer_midterm_cmp_industry
union
select distinct * from data_scientist_final_cmp_industry
union
select distinct * from data_scientist_midterm_cmp_industry)as merge_cmp_industry
);