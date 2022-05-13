CREATE VIEW T_city_date_final as
select prim.*, jpd."date" ,jpd.weekofday, cmp.industry
from (select *
from(select *, regexp_replace(location_in_detail,',([+ A-Za-z0-9]+)', '','g') as city,
regexp_replace(location,'State', '','g') as state
FROM job_basic_information_final
) result) as prim
left join 
job_post_date jpd 
on prim.jid=jpd.jid 
left join merge_cmp_industry cmp
on prim.company_name=cmp.company_name

