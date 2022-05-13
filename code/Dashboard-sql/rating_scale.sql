create view t_categorized_rating_try as 
select result.*,case
    when result.rating >= 0 and result.rating < 3.5 then 'Rating 0-3.5'
    when result.rating >= 3.5 and result.rating <= 3.8 then 'Rating 3.5-3.8'
    when result.rating > 3.8 and result.rating <=5.0 then 'Rating 3.8-5.0'
end as RatingClassfication
from 
(
select jid,job_title,location_in_detail,location,Title, cast(rating as float)
from job_basic_information_all jbi
where rating !=''
) as result




