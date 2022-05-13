--Clean the table with company name and industry	
create table if not exists merge_company_name_industry as(
select
	company_name,
	industry
from
	(
	select
		company_name,
		industry,
		row_number() over (
      partition by company_name
	order by
		industry desc
   ) row_num
	from
	merge_cmp_industry
	order by company_name) as part_mci
where
	part_mci.row_num = '1')