CREATE VIEW T_city_date_midterm as
select prim.*, jpd."date" ,jpd.weekofday, cmp.industry
from (select *
from(select *, regexp_replace(location_in_detail,',([+ A-Za-z0-9]+)', '','g') as city,
regexp_replace(location,'State', '','g') as state
FROM job_basic_information_midterm
) result) as prim
left join 
job_post_date_midterm jpd 
on prim.jid=jpd.jid 
left join merge_cmp_industry cmp
on prim.company_name=cmp.company_name
