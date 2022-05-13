create view salary_to_float as 
select *,
	case 
	when salary_mean = '' then 0
	else cast(salary_mean as float)
	end as salary_float 
from t_city_date_all