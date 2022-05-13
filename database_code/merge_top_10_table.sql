--Merge top 10 tables by title
create table if not exists top_10_data_analyst as (
select distinct * from (
select * from top_10_final_data_analyst
union
select * from top_10_midterm_data_analyst)as top_10_data_analyst);

create table if not exists top_10_data_engineer as (
select distinct * from(
select * from top_10_final_data_engineer
union
select * from top_10_midterm_data_engineer)as top_10_data_engineer);

create table if not exists top_10_data_scientist as (
select distinct * from (
select * from top_10_midterm_data_scientist
union
select * from top_10_final_data_scientist)as top_10_data_scientist);

--Create a total top 10 table
create table if not exists top_10 as (
select distinct * from(
select * from top_10_data_analyst
union
select * from top_10_data_engineer
union
select * from top_10_data_scientist) as top_10);