CREATE VIEW T_city_date_ALL as
select *
from T_city_date_midterm
union
select *
from T_city_date_final