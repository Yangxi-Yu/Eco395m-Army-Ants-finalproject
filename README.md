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

## Data Source
The raw data comes from the [Indeed](https://www.indeed.com) website. 

## Goal of the Analysis
The final project will continue to explore the topic in Midterm of how to find the data-relevant position in Indeed. The goals are to give an insightful idea about the data-relevant job market in Texas, California, and New York, visualized by Tableau and to help job-seekers match the job position effectively and efficiently by developing a interactive matching tool. 

Compared with our midterm project, there are some improvements: 
1. Using PostgreSQL to store the web-scraping data from Indeed and organize and optimize the database efficiently; 
2. Using Tabkeau as Dashboard to visualize the data and illustrates the trend of different position on a time-varying scale;
3. Develop a matching tool to find the most related job postings in our database.

## Methodology

### High Level - Overview
![Methodology-overview](https://github.com/Yangxi-Yu/Eco395m-Army-Ants-finalproject/blob/high-level-methodology/image/Methodology%20-%20High%20Level.png)

### Detail - Web Scraping
![Methodology-web scraping](https://github.com/Yangxi-Yu/Eco395m-Army-Ants-finalproject/blob/main/image/Methodology%20-%20Web%20Scraping.PNG)

### Detail - Matching Tools
![Methodology-Tools](https://github.com/Yangxi-Yu/Eco395m-Army-Ants-finalproject/blob/140-model-methodology/image/Methodology%20-%20Matching%20Tools%201.png)

### Detail - Database Schema 
![Methodology-Database](https://github.com/Yangxi-Yu/Eco395m-Army-Ants-finalproject/blob/main/image/Methodology%20-%20database.png)


## Findings
After making the data visualization in Tableau, we get a story composed of 2 dashboards: Overview and Searching. The Overview gives basic information about the posted jobs across NY, TX, and CA. When choosing a specific country, the dashboard will show the country-specific job salary, the number of job postings, the main industry, and the companies. The interactive dashboard pictures the general portrait of the data-related jobs. Then we design the Searching, which includes the information of posted jobs, to help jobseekers to find jobs based on their unique needs by using the filter on the top.
### Overview
From a geographical view, NYC has the most job posted; jobs in Texas are mostly in Austin, Houston, and Dallas; jobs in California are mainly posted from San Francisco and Los Angeles. Most data-related jobs are in the big cities, especially in Texas and New York. Jobs in TX and NY are concentrated in big cities, but jobs in California are relatively scattered and are distributed in cities around SF and LA.

Now we choose three representative cities: Austin, New York, and San Francisco from Texas, New York State, and California.
<br />
<br />



![This is an image](https://github.com/Yangxi-Yu/Eco395m-Army-Ants-finalproject/blob/readme_gif/image/Austin.GIF)
Austin, TX
The number of job postings is almost the same as in March-April, but the summit in March is in the middle of the month, that in April is at the end of the month. The companies in Austin focus on technology and manufacturing, and famous companies are Advanced Micro Devices and General Motors.
<br />
<br />
<br />

![This is an image](https://github.com/Yangxi-Yu/Eco395m-Army-Ants-finalproject/blob/readme_gif/image/New%20York.GIF)

New York City
Compared with March, the number of NYC job postings declined in April, but suddenly surged in the last week. The companies in NYC focus on financial services and information technology, and many famous companies like JP Morgan, Citi, and Deloitte had high demand
<br />
<br />
<br />

![This is an image](https://github.com/Yangxi-Yu/Eco395m-Army-Ants-finalproject/blob/readme_gif/image/Los%20Angeles.GIF)

Los Angeles, CA
The overall number of data-related jobs provided in March and April was basically unchanged, and the trend in different periods of each month was also similar. The main Industries are Education and Informational Technology. Many famous companies are CGI Group and Microsoft in LA. 


### Searching

![This is an image](https://github.com/Yangxi-Yu/Eco395m-Army-Ants-finalproject/blob/readme_gif/image/Searching.GIF)

Taking Austin, TX as an example, because we’re current graduate students, so we set the master's degree. Firstly, we got recommended 86 jobs in this process, and the top 3 skills needed are SQL, Python, and Cloud, which is consistent with the results of the mid-term project. Also, the office occupies an important position. Most job descriptions lack the salary part and the need for entry-level is more than in others. Secondly, we now add the bachelor's level, which gives us 545 jobs, which is much more than the jobs that require a higher degree. Thus, most data-related job only requires a bachelor's degree. In addition, we set that Rating 0-3.5 represents the dissatisfaction of employees with data positions. From our data, the master dissatisfaction rate is 17/86=19.77%, and the rate decreases to 91/545= 16.70% when we add the bachelor in the group. Having compared different degree levels’ data, we can conclude that the higher the degree required, the lower the job satisfaction. Maybe the reason is the master level job needs more tasks and the employee will meet more pressure in the working process. So, this might increase the job dissatisfaction rate of higher degrees. 

Now we make the cross-sectional analysis. In the past 3 months, the proportion of the remote job and the job satisfaction are increasing. It’s reasonable for the job contentment when we consider the recovery from the covid pandemic. For the job type, it’s surprising that the remote job has risen, and we guess that would be the future trend and many job seekers will consider more data positions when they search the job information.

The next part below the horizontal bar chart is one table that includes the company’s name, city, job titles, and job links. The number of information corresponds to the total number: 86 after we select the Austin and master’s degree levels. Job seekers can just click the link and apply for it on indeed and it’s very convenient for job seekers to see and find real jobs quickly if they fill out basic information at the top of this page.
<br />

![This is an image](https://github.com/Yangxi-Yu/Eco395m-Army-Ants-finalproject/blob/readme_gif/image/Similarity.GIF)

Another advantage of this searching page is at the left corner named Similarity Matrix. If job seekers click the job title in the job posting part, it will connect the specific information of this job in Indeed. When they go back to the Searching page of the Dashboard, the page will use this job id and illustrate other Top 10 similar jobs which job seekers can choose and compare. 
<br />
<br />
<br />
![This is an image](https://github.com/Yangxi-Yu/Eco395m-Army-Ants-finalproject/blob/readme_gif/image/Recommendation.GIF)

This page also includes one cartoon image which attracts people to click. When job seekers click it, it will connect to one Jupyter lab, and job seekers can type jobs’ basic information on this page. When it runs and the Searching page has been renewed after interacting with Jupyter, the Recommendation part in the right corner provides several jobs which fulfill the requirement of job seekers’ willingness and job’s basic information. This interaction can help job seekers get several recommendations when they use the Searching page. 


## Limitations
1. Refreshing and loading data source can take a long time (usually takes 3 - 4 days).
2. Dashboard cannot interact well with jupyter notebook.
3. For the job title classifications and locations, this project only selects specific jobs by filtering keywords such as'data analyst' and 'Texas'. However, data-related jobs may have various names but have similar job descriptions, and this hiring information is ignored, which leads to incomplete data collection.
4. Intuitively, the salary for the same position is higher in NYC than in California and Texas. However, from our dashboard, it’s the opposite. San Francisco’s posted position’s salary is the highest. The possible reason is that many posted jobs don’t mention their salary in the job description, thus leading to this bias. Another reason is NYC has many diverse companies and some small corporates provide lower salary to jobseekers. This can decrease the mean salary of data positions in NYC and the result opposites our intuitions. We will research and use more data to get accurate information on the data-related positions in big cities.

## Extensions
1. Consider to use Streamlit rather than Tableau, which can interact soomthly with users.
2. Use automatic ETL process to refresh the data source and load in the database. 
3. Use PostgreSQL Full Text search to improve the matching tool performance.

## Instructions

### 0. Installation
Run `pip install -r requirements_final.txt`

### 1. Data Scraping
*Please note that the data scraping process may take a lot of time, so, it’s better to skip this section and start reproduce process from section 2 – Data Cleaning.*
Output: `merge_searched_html_all`; `merge_job_des_html`
#### Step 1. Get Searched Job List HTML
Run `python3 database_code/get_searched_job_html.py` and enter position, location, date range, sort to scrape the job list html in the indeed website. Enter a job title (Data Analyst/ Data Scientist/ Data Engineer), a location (Texas/ California/ New York State), a time period (30) and sorting (date) to get page html tables. Here are all the tables that need to be generated in this step:

|Generate Tables|Parameters Entered|
|--------------|------------------|
|data_analyst_texas_30|Data Analyst, Texas, 30, date|
|data_analyst_california_30|Data Analyst, California, 30, date|
|data_analyst_new_york_state_30|Data Analyst, New York State, 30, date|
|data_engineer_texas_30|Data Engineer, Texas, 30, date|
|data_engineer_california_30|Data Engineer, California, 30, date|
|data_engineer_new_york_state_30|Data Engineer, New York State, 30, date|
|data_scientist_texas_30|Data Scientist, Texas, 30, date|
|data_scientist_california_30|Data Scientist, California, 30, date|
|data_scientist_new_york_state_30|Data Scientist, New York State, 30, date|

Run `python3 database_code/merge_html_tables.py`, which merges nine tables in step 1. The output table is `merge_searched_job_html`. We need create bucket in GCP to upload the corresponding table in midterm, named `old_merge_searched_job_html`, and insert it into database. Run `merge_page_html.sql` to merge midterm and final tables into one table named `merge_searched_html_all` in the sql command.

#### Step 2. Select jobs in each job titles (Data Analyst, Data Engineer, Data Scientist) and get their job description HTML
This time we select all of jobs, releasing the restriction of just selecting 300 jobs in midterm project. Run `python3 database_code/get_job_descriptions_final.py` and `python3 database_code/get_job_descriptions_midterm.py` and enter a job title (Data Analyst/ Data Scientist/ Data Engineer) to get all of the job descriptions. Here are all the tables that need to be generated:

|Generate Tables|Parameters Entered|
|--------------|------------------|
|job_des_html_data_analyst|Data Analyst|
|job_des_html_data_engineer|Data Engineer|
|job_des_html_data_scientist|Data Scientist|
|job_des_html_midterm_data_analyst|Data Analyst|
|job_des_html_midterm_data_engineer|Data Engineer|
|job_des_html_midterm_data_scientist|Data Scientist|

In sql, merge tables of midterm data with tables with final data and get merge_job_des_html. Run `database-code/merge_job_des_html.sql` in Dbeaver to get `merge_job_des_html` table.

### 2. Data Cleaning
### 2-1. Clean HTML tables to get basic information for each job
Output: `job_basic_information_midterm`; `job_basic_information_final`; `job_basic_information_all`

Run `python3 database_code/html_dataframe.py` to generate job_basic_information_midterm, job_basic_information_final, job_basic_information_all with information of job_id, salary, ratings, company, location, title, specific location and specific title. 

|Generate Tables|Parameters Entered|
|--------------|------------------|
|job_basic_information_midterm|Midterm|
|job_basic_information_final|Final|
|job_basic_information_all|All|

### 2-2. Clean HTML tables to get posted date for each job
Output: `job_post_date`; `job_post_date_midterm`; `merge_job_post_date`

Run `python3 database_code/job_post_date.py` and `python3 database_code/job_post_date_midterm.py` to generate job_post_date with job_id, title, location and some information of posted date. In sql, we get two tables named `job_post_date` and `job_post_date_midterm`. Then run `database-code/merge_job_post_date.sql` to merge these two tables into `merge_job_post_date`.

### 2-3. Clean HTML tables to get detailed information for each job
Output: `merge_jid_cmp`; `merge_cmp_industry`

#### Step 1. Get the tables of industry information
Run `python3 database_code/get_industry.py` and enter a job title (Data Analyst/ Data Scientist/ Data Engineer) and a time period (Midterm/ Final) to fetch industry information for all the jobs. Here are the output files:

|Generate Tables|Parameters Entered|
|--------------|------------------|
|data_analyst_final_jid_cmp|Data Analyst, Final|
|data_engineer_final_jid_cmp|Data Engineer, Final|
|data_scientist_final_jid_cmp|Data Scientist, Final|
|data_analyst_final_cmp_industry|Data Analyst, Final|
|data_engineer_final_cmp_industry|Data Engineer, Final|
|data_scientist_final_cmp_industry|Data Scientist, Final|
|data_analyst_midterm_jid_cmp|Data Analyst, Midterm|
|data_engineer_midterm_jid_cmp|Data Engineer, Midterm|
|data_scientist_midterm_jid_cmp|Data Scientist, Midterm|
|data_analyst_midterm_cmp_industry|Data Analyst, Midterm|
|data_engineer_midterm_cmp_industry|Data Engineer, Midterm|
|data_scientist_midterm_cmp_industry|Data Scientist, Midterm|

In Dbeaver, run `database_code/merge_jid_cmp.sql` to merge tables containing job id and company name into one table named `merge_jid_cmp`. Similarly, run `database/merge_cmp_industry.sql` to get one table named `merge_cmp_industry` by dealing with tables containing company name and industry.

#### Step 2. Clean the tables above
In merge_cmp_industry table, there are 3 situations needed to be solved.        
(1) a same company has different expressions for industry, such as ‘HealthCare’ and ‘Health Care’.     
(2) The industry corresponding to a same company has a real value and an empty value.      
(3) Some companies have empty values of industry.   
To solve these problems, we group the companies by name, taking only the first line, ensuring that each company corresponds to an industry, i.e., run `database_code/clean_cmp_industry.sql`

#### Step 3. Get counting of skills
Run `python3 database_code/get_skills_list.py` and enter a job title (Data Analyst/ Data Scientist/ Data Engineer) and enter a time period (Midterm/ Final) to fetch industry information for all the jobs in section. Here are the output tables:

|Generate Tables|Parameters Entered|
|--------------|------------------|
|job_skill_counts_data_analyst_midterm|Data Analyst; Midterm|
|job_skill_counts_data_engineer_midterm|Data Engineer; Midterm|
|job_skill_counts_data_scientist_midterm|Data Scientist; Midterm|
|job_skill_counts_data_analyst_final|Data Analyst; Final|
|job_skill_counts_data_engineer_final|Data Engineer; Final|
|job_skill_counts_data_scientist_final|Data Scientist; Final|

In Dbeaver, run `database_code/merge_job_skill_list.sql` to merge tables above by job title to get three tables: `merge_job_skill_counts_data_analyst_midterm`, `merge_job_skill_counts_data_engineer`, `merge_job_skill_counts_data_scientist`.

### 2-4. Build relationships between merged tables
Run `database_code/build_up_relationships.sql` in Dbeaver:
(1) Select `company name` as a primary key in `merge_company_name_industry` table, and connect the foreign key `company name` in `merge_jid_cmp table`.
(2) Select `jid` as a primary key in `merge_job_des_html` table, and connect the foreign key `jid` in `merge_jid_cmp` table.
(3) Select `jid` as a foreign key in `job_basic_information_all` table, and connect the primary key `jid` in `merge_job_des_html` table.
(4) Select `jid` as a foreign key in `merge_job_post_date` table, and connect the primary key `jid` in `merge_job_des_html` table.   

### 2-5. Clean job description
Run `python3 code/clean_job_description.py` and enter job title, scraping time, which will clean job description HTML for each job in our database and add degree, experience level columns.

|Generate Tables|Parameters Entered|
|--------------|------------------|
|job_cleaned_description_midterm_data_analyst|Data Analyst, Midterm|
|job_cleaned_description_midterm_data_scientist|Data Scientist, Midterm|
|job_cleaned_description_midterm_data_engineer|Data Engineer, Midterm|
|job_cleaned_description_final_data_analyst|Data Analyst, Final|
|job_cleaned_description_final_data_scientist|Data Scientist, Final|
|job_cleaned_description_final_data_engineer|Data Engineer, Final|

Then we run `database_code/merge_job_cleaned_description.sql` to merge all of job cleaned description tables


### 3-1. Job-Job Matching Tool
Run `python3 code/ select_top_10_related_jid.py`, which return a top 10 related jobs for each job in our database. The output table is `select_top_10`. We merge top_10 tables by title and get a general table by running `database_code/merge_top_10_table.sql`

### 3-2. Resume-Job Matching Tool
Open and run `input.ipynb`, and enter Job Title, Location, Date Posted, your Highest Education, Experience Level, and your resume/keywords you want to search. It will return a top 50 related job in our database. The output table is `cosine_similarity_matrix`.


### 4. Tableau Dashboard
Use Tableau to better achieve storytelling with visualization in interaction. The brief introduction is as follows.

### 4-1. Data Transformation
Run `code/Dashboard_py/skills_transforms.py` and `code/Dashboard_py/top_10_sql_transform.py` to transform the table format for easily processing and calculation in Tableau.

### 4-2. Build a Database in Tableau
![This is an image](https://github.com/Yangxi-Yu/Eco395m-Army-Ants-finalproject/blob/main/image/Dashboard%20-%20Tableau%20Database.png)
The graph above illustrates the structure of built-in database in Tableau. The primary table is `t_city_date_all`, which stores the all job-posting with dimension of city and date. The primary key between `t_city_date_all` and `merge_company_name_industry` is `Company Name` while others are `jid`. Here are the table for the relation between each table and the function.


|Tables|Linked Key|Function|
|--------------|------------------|------------------|
|t_city_date_all|jid, Company Name|Main info with City, Date Prime Table|
|cosine_similarity_matrix|jid|recommendated job_title, url and cos_similarity|
|job_degree|jid|includes degree|
|merge_company_name_industry|Company Name|includes Company Name and Industry|
|merge_job_cleaned_description|jid|includes experience_level|
|merge_job_skills_counts_transformed|jid|includes skill frequency|
|t_categorized_rating|jid|includes rating and rating scale|
|t_job_type|jid|includes remote/in-person/hybrid|
|t_salary|jid|includes avg_salary and salary_scale|
|top_10_transformed_sql|jid|includes top 10 job posting in similarity matrix |

### 4-3. Overview Dashboard
The goal of **Dashboard Overview** is to brifly introduce the data-related job-market. Here is a brief introduction of how to build these graph.

**(1)Map**: Use `t_city_date` to build layer of map and `count(jid)` as size of the point. 

**(2)Job_posting**: Use `t_city_date` to build the stacked chart. Specifically, we use `date` in week dimension to construct the timeline, the `count(jid)` as the shaded area and `title` for 3 different data-related jobs. The graph is connected with the selection of different city in the **map**.

**(3)Salary**: Use `t_city_date` and `t_salary` to build Salary table. The numeric is average number of the salary in different city. The graph is connected with the selection of different city in the **map**.

**(4)Industry** Use `t_city_date` and `merge_company_name_industry` to construct industry stacked chart, which includes the dimension of `date`,`title`. Use count(jid) to illustrate the shaded arer. The graph is connected with the selection of different city in the **map**.

**(5)Comopany** Use `merge_company_name_industry` for **treemap**. The color represents industry and the size for `count(jid)` of job-postings for differenct companys.The graph is connected with the selection of different city in the **map**.

### 4-4. Searching Dashboard
The goal of **Searching Overview** is to simulate the job-seeking process with interaction. Besides, the dashboard involves recommendation function. Here is a brief introduction of how to build these graph.

**1.Graph**:

(1) Company-Most Post: Use `company name` and `count(jid)` in `t_city_date` to build with top 10 ranking.(Under All filters)  
(2) Job_Postiing Number: Use `count(jid)` in `t_city_date` to show the total number of posted job.(Under All filters)  
(3) Skills-Most posted: Use `skill` in `merge_job_skills_counts_transformed` and `sum(count)` to calculate the frequency of skills. The graph is only linked to `job type` filter.     
(4) job title: Use `count(jid)` and `title` in `t_city_date` to contruct bar chart.(Under All filters)  
(5) job type: Use `count(jid)` and `job_type`in `t_job_type` to contruct bar chart.(Under All filters)  
(6) rating scale: Use `count(jid)` and `rating scale` in `t_salary` to contruct bar chart.(Under All filters)  
(7) Salary:  Use `count(jid)` and `salary scale` in `t_categorized_rating` to contruct bar chart.(Under All filters)  
(8) exp_level: Use `count(jid)` and `Exp_Level` in 'merge_job_cleaned_description' to contruct bar chart.(Under All filters)  
(9) bachelor: Use `count(jid)` and `Degree` in `job_degree` to contruct bar chart.(Under All filters)  

**2.Text Tables**:

(1) job posting tables: Shows all job_pistings with url_links in 't_city_date_all'. Click the url to the job_posting website in Indeed.(Under All filters)  
(2) Similarity Matrix: Linked to selection of `job posting tables`. Recommend top 10 correlated job postings with url_links in `top_10_transformed_sql`. Click to exact job-posting website in Indeed.
(3) Recommendation: Shows recommended `jid`,`job_postings` and `url`after submitting resume. Click to exact website with hyperlink. 

**3.Button**:
Click Icon to hyperlink to Jupyter and start the job-recommendation.

**4.Filter**: 
Include `city`, `Salary Range`, `Exp Level`, `Degree`, `Salary Float`, `Job Type`, `Date`, `title` and `rating `, which all linked with `job-posingts number` and selection linked with other graph and charts mentioned before.




 
