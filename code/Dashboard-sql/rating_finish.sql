
select result.*,case
    when result.rating >= 0 and result.rating < 3.0 then 'Rating 0-3.0'
    when result.rating >= 3.0 and result.rating <= 4.0 then 'Rating 3.0-4.0'
    when result.rating > 4.0 and result.rating <= 5.0 then 'Rating 4.0-5.0'
end as RatingClassfication
from 
(
select jid,job_title,location_in_detail,Title, cast(rating as float)
from job_basic_information_all jbi
where rating !=''
) as result