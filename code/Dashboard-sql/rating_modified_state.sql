
create view t_categorized_rating as 
select t_categorized_rating_try.*, replace (location, 'New York State', 'New York') as state
from  t_categorized_rating_try
