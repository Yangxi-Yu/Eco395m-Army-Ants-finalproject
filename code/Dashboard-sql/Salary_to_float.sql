create view t_salary as 
select *,
	case 
		when (salary_float > 0 and salary_float <= 70000) then '< 70K'
		when (salary_float > 70000 and salary_float <= 175000) then '70K - 175K'
		when (salary_float > 17500) then '> 175K'
	else 'Salary Not Post'
	end as salary_range
	from salary_to_float stf 