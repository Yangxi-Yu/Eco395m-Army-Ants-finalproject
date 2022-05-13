import pandas as pd
from bs4 import BeautifulSoup
import re
import requests
import numpy as np
import time
from database import engine
from sqlalchemy.types import String


JOB_TITLE = input(
    "Please enter a job title (Data Analyst/ Data Scientist/ Data Engineer): "
)
TIME = input("Please enter scraping time of data (Midterm/ Final): ")


def job_title_get_des_db():
    """Load certain job tables from database"""

    if TIME == "Midterm":
        df_job_des_html = pd.read_sql_table(
            f"job_des_html_{TIME}_{JOB_TITLE}".lower().replace(" ", "_"), engine
        )
    if TIME == "Final":
        df_job_des_html = pd.read_sql_table(
            f"job_des_html_{JOB_TITLE}".lower().replace(" ", "_"), engine
        )

    return df_job_des_html


def get_cmp_name():
    """Return a dataframe that list all jid and company name"""

    df_job_des_html = job_title_get_des_db()
    jid_cmp_dic = {}
    for row in range(len(df_job_des_html)):
        html = BeautifulSoup(df_job_des_html["jidhtml"][row], "html.parser")
        jid = df_job_des_html["jid"][row]
        cmp_names = html.find_all("div", "icl-u-lg-mr--sm icl-u-xs-mr--xs")
        for cmp_name in cmp_names:
            if cmp_name.text != "":
                jid_cmp_dic[jid] = cmp_name.text

    jid_cmp_df = pd.DataFrame(list(jid_cmp_dic.items()))
    jid_cmp_df.columns = ["jid", "company_name"]
    jid_cmp_df["title"] = JOB_TITLE

    return jid_cmp_df


def sleeper(min_sleep_sec, max_sleep_sec):
    """Give a random sleep time between min_sleep_sec and max_sleep_sec."""

    time_splits = np.linspace(min_sleep_sec, max_sleep_sec, num=60)
    alarm = np.random.choice(time_splits)
    rounding = np.random.choice(list(range(2, 6)))

    return time.sleep(round(alarm, rounding))


def get_com_industry(jid_cmp_df):
    """Return a dataframe that list all company name and industry"""
    industry = {}
    success_counts = 1
    for row in range(len(jid_cmp_df)):
        company = jid_cmp_df["company_name"][row]

        cmp_url = "https://www.indeed.com/cmp/" + company
        cmp_response = requests.get(cmp_url)
        cmp_html = BeautifulSoup(cmp_response.text, "html.parser")
        cmp_industry = cmp_html.find(
            "li", attrs={"data-testid": "companyInfo-industry"}
        )
        if cmp_industry != None:
            industry_name = cmp_industry.text
            industry[company] = industry_name[8:]
        else:
            industry[company] = ""

        print(str(success_counts) + " job(s) industry fetched.")
        sleeper(10.6666, 20.999)

        success_counts += 1

    cmp_industry_df = pd.DataFrame(list(industry.items()))
    cmp_industry_df.columns = ["company_name", "industry"]
    cmp_industry_df.drop_duplicates()

    return cmp_industry_df


def jid_cmp_sql_db(jid_cmp_df):
    """Upload table with job id and company name to database"""

    schema = {
        "jid": String,
        "company_name": String,
        "title": String,
    }

    jid_cmp_table_name = f"{JOB_TITLE}_{TIME}_jid_cmp".lower().replace(" ", "_")

    create_table_cmd = """
        create table if not exists {} (
        jid varchar,
        company_name varchar,
        title varchar)
        """.format(
        jid_cmp_table_name
    )

    jid_cmp_df.to_sql(
        jid_cmp_table_name, engine, if_exists="replace", dtype=schema, index=False
    )
    engine.connect().exec_driver_sql(create_table_cmd)


def cmp_industry_sql_db(cmp_industry_df):
    """Upload data of company name and industry to database"""

    schema = {
        "company_name": String,
        "industry": String,
    }

    cmp_industry_table_name = f"{JOB_TITLE}_{TIME}_cmp_industry".lower().replace(
        " ", "_"
    )

    create_table_cmd = """
    create table if not exists {} (
        industry varchar,
        company_name varchar);
        """.format(
        cmp_industry_table_name
    )

    cmp_industry_df.to_sql(
        cmp_industry_table_name, engine, if_exists="replace", dtype=schema, index=False
    )
    engine.connect().exec_driver_sql(create_table_cmd)


if __name__ == "__main__":

    jid_cmp_df = get_cmp_name()

    cmp_industry_df = get_com_industry(jid_cmp_df)

    jid_cmp_sql_db(jid_cmp_df)

    cmp_industry_sql_db(cmp_industry_df)
