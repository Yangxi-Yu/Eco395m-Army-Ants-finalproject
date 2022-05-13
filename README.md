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
## Findings
After making the data visualization in Tableau, we get a story composed of 2 dashboards: Overview and Searching. The Overview gives basic information about the posted jobs across NY, TX, and CA. When choosing a specific country, the dashboard will show the country-specific job salary, the number of job postings, the main industry, and the companies. The interactive dashboard pictures the general portrait of the data-related jobs. Then we design the Searching, which includes the information of posted jobs, to help jobseekers to find jobs based on their unique needs by using the filter on the top.![image](https://user-images.githubusercontent.com/98198613/168220127-c7399d74-0ca7-4c16-8b41-b1137dba096b.png)
### *Overview*
From a geographical view, NYC has the most job posted; jobs in Texas are mostly in Austin, Houston, and Dallas; jobs in California are mainly posted from San Francisco and Los Angeles. Most data-related jobs are in the big cities, especially in Texas and New York. Jobs in TX and NY are concentrated in big cities, but jobs in California are relatively scattered and are distributed in cities around SF and LA.![image](https://user-images.githubusercontent.com/98198613/168220327-f4652b03-5c71-4dc7-869d-808b076e975c.png)

Now we choose three representative cities: Austin, New York, and San Francisco from Texas, New York State, and California.![image](https://user-images.githubusercontent.com/98198613/168220349-86b926dc-234e-4549-9f68-63838345157e.png)

Austin, TX
The number of job postings is almost the same as in March-April, but the summit in March is in the middle of the month, that in April is at the end of the month. The companies in Austin focus on technology and manufacturing, and famous companies are Advanced Micro Devices and General Motors.
![image](https://user-images.githubusercontent.com/98198613/168220363-a9dc569f-f0ff-4afe-bcea-45d48a2550d5.png)

New York City
Compared with March, the number of NYC job postings declined in April, but suddenly surged in the last week. The companies in NYC focus on financial services and information technology, and many famous companies like JP Morgan, Citi, and Deloitte had high demand
![image](https://user-images.githubusercontent.com/98198613/168220387-c037df67-04dc-4ea2-b795-005620330ac0.png)

Los Angeles, CA
The overall number of data-related jobs provided in March and April was basically unchanged, and the trend in different periods of each month was also similar. The main Industries are Education and Informational Technology. Many famous companies are CGI Group and Microsoft in LA. 
![image](https://user-images.githubusercontent.com/98198613/168220413-c606932a-194c-4712-81de-ea4490774792.png)

### *Searching*

Taking Austin, TX as an example, because we’re current graduate students, so we set the master's degree. Firstly, we got recommended 86 jobs in this process, and the top 3 skills needed are SQL, Python, and Cloud, which is consistent with the results of the mid-term project. Also, the office occupies an important position. Most job descriptions lack the salary part and the need for entry-level is more than in others. Secondly, we now add the bachelor's level, which gives us 545 jobs, which is much more than the jobs that require a higher degree. Thus, most data-related job only requires a bachelor's degree. In addition, we set that Rating 0-3.5 represents the dissatisfaction of employees with data positions. From our data, the master dissatisfaction rate is 17/86=19.77%, and the rate decreases to 91/545= 16.70% when we add the bachelor in the group. Having compared different degree levels’ data, we can conclude that the higher the degree required, the lower the job satisfaction. Maybe the reason is the master level job needs more tasks and the employee will meet more pressure in the working process. So, this might increase the job dissatisfaction rate of higher degrees. ![image](https://user-images.githubusercontent.com/98198613/168220467-9edb0e51-93a8-4544-83ea-3cd32b9c4b12.png)

Now we make the cross-sectional analysis. In the past 3 months, the proportion of the remote job and the job satisfaction are increasing. It’s reasonable for the job contentment when we consider the recovery from the covid pandemic. For the job type, it’s surprising that the remote job has risen, and we guess that would be the future trend and many job seekers will consider more data positions when they search the job information. ![image](https://user-images.githubusercontent.com/98198613/168220488-a1d89808-9811-41a7-bdbb-c1777377e8d3.png)




## Limitation
1. Intuitively, the salary for the same position is higher in NYC than in California and Texas. However, from our dashboard, it’s the opposite. San Francisco’s posted position’s salary is the highest. The possible reason is that many posted jobs don’t mention their salary in the job description, thus leading to this bias. Another reason is NYC has many diverse companies and some small corporates provide lower salary to jobseekers. This can decrease the mean salary of data positions in NYC and the result opposites our intuitions. We will research and use more data to get accurate information on the data-related positions in big cities. ![image](https://user-images.githubusercontent.com/98198613/168220546-5da7d527-8b55-4712-b4e4-5afc1d56c7fa.png)

