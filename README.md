# Eco395m-Army-Ants-finalproject
## Team Army Ants Midterm Project for Python, Data, and Databases
## Group Members
* Yangxi Yu
* Xiaohan Sun
* Shuyan Yue
* Zonghao li
* Chen Tang
* Liming Pang
* Xiaohan Wu
* Chengkan Tao
* Yiwen Wang
* Shankai Liao

## Methodology

### Matching Tools
![Methodology](https://github.com/Yangxi-Yu/Eco395m-Army-Ants-finalproject/blob/140-model-methodology/image/Methodology%20-%20Matching%20Tools.png)

## Findings
After making the data visualization in Tableau, we get a story composed of 2 dashboards: Overview and Searching. The Overview gives basic information about the posted jobs across NY, TX, and CA. When choosing a specific country, the dashboard will show the country-specific job salary, the number of job postings, the main industry, and the companies. The interactive dashboard pictures the general portrait of the data-related jobs. Then we design the Searching, which includes the information of posted jobs, to help jobseekers to find jobs based on their unique needs by using the filter on the top.
### *Overview*
From a geographical view, NYC has the most job posted; jobs in Texas are mostly in Austin, Houston, and Dallas; jobs in California are mainly posted from San Francisco and Los Angeles. Most data-related jobs are in the big cities, especially in Texas and New York. Jobs in TX and NY are concentrated in big cities, but jobs in California are relatively scattered and are distributed in cities around SF and LA.

Now we choose three representative cities: Austin, New York, and San Francisco from Texas, New York State, and California.

Austin, TX
The number of job postings is almost the same as in March-April, but the summit in March is in the middle of the month, that in April is at the end of the month. The companies in Austin focus on technology and manufacturing, and famous companies are Advanced Micro Devices and General Motors.


New York City
Compared with March, the number of NYC job postings declined in April, but suddenly surged in the last week. The companies in NYC focus on financial services and information technology, and many famous companies like JP Morgan, Citi, and Deloitte had high demand


Los Angeles, CA
The overall number of data-related jobs provided in March and April was basically unchanged, and the trend in different periods of each month was also similar. The main Industries are Education and Informational Technology. Many famous companies are CGI Group and Microsoft in LA. 


### *Searching*

Taking Austin, TX as an example, because we’re current graduate students, so we set the master's degree. Firstly, we got recommended 86 jobs in this process, and the top 3 skills needed are SQL, Python, and Cloud, which is consistent with the results of the mid-term project. Also, the office occupies an important position. Most job descriptions lack the salary part and the need for entry-level is more than in others. Secondly, we now add the bachelor's level, which gives us 545 jobs, which is much more than the jobs that require a higher degree. Thus, most data-related job only requires a bachelor's degree. In addition, we set that Rating 0-3.5 represents the dissatisfaction of employees with data positions. From our data, the master dissatisfaction rate is 17/86=19.77%, and the rate decreases to 91/545= 16.70% when we add the bachelor in the group. Having compared different degree levels’ data, we can conclude that the higher the degree required, the lower the job satisfaction. Maybe the reason is the master level job needs more tasks and the employee will meet more pressure in the working process. So, this might increase the job dissatisfaction rate of higher degrees. 

Now we make the cross-sectional analysis. In the past 3 months, the proportion of the remote job and the job satisfaction are increasing. It’s reasonable for the job contentment when we consider the recovery from the covid pandemic. For the job type, it’s surprising that the remote job has risen, and we guess that would be the future trend and many job seekers will consider more data positions when they search the job information.




## Limitation
1. Intuitively, the salary for the same position is higher in NYC than in California and Texas. However, from our dashboard, it’s the opposite. San Francisco’s posted position’s salary is the highest. The possible reason is that many posted jobs don’t mention their salary in the job description, thus leading to this bias. Another reason is NYC has many diverse companies and some small corporates provide lower salary to jobseekers. This can decrease the mean salary of data positions in NYC and the result opposites our intuitions. We will research and use more data to get accurate information on the data-related positions in big cities.

## Instructions

### 2-1. Data Cleaning – clean job description
Run `python3 code/clean_job_description.py` and enter job title, scraping time, which will clean job description HTML for each job in our database and add degree, experience level columns.

|Generate Tables|Parameters Entered|
|--------------|------------------|
|job_cleaned_description_midterm_data_analyst|Data Analyst, Midterm|
|job_cleaned_description_midterm_data_scientist|Data Scientist, Midterm|
|job_cleaned_description_midterm_data_engineer|Data Engineer, Midterm|
|job_cleaned_description_final_data_analyst|Data Analyst, Final|
|job_cleaned_description_final_data_scientist|Data Scientist, Final|
|job_cleaned_description_final_data_engineer|Data Engineer, Final|

### 2-2. Job-Job Matching Tool
Run `python3 code/ select_top_10_related_jid.py`, which return a top 10 related jobs for each job in our database. The output table is `select_top_10`.

### 2-3. Resume-Job Matching Tool
Open and run `input.ipynb`, and enter Job Title, Location, Date Posted, your Highest Education, Experience Level, and your resume/keywords you want to search. It will return a top 50 related job in our database. The output table is `cosine_similarity_matrix`.
