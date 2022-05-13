import pandas as pd
from bs4 import BeautifulSoup
import re
import requests
import numpy as np
import time
import os
from sqlalchemy.types import String
from database import engine


JOB_TITLE = input(
    "Please enter a job title (Data Analyst/ Data Scientist/ Data Engineer): "
)


def get_sql_table():
    """get the final page html table from database"""
    df_merged_tables_sql = pd.read_sql_table("merge_searched_job_html", engine)
    return df_merged_tables_sql


def get_jid_list(df_merge):
    """Get and return a dataframe contains jid, location, job title from merged_searched_job_html"""
    find_jid = re.compile(r"(jobKeysWithInfo\[([a-zA-z0-9]{16})\])")
    jid_lo_dic = {}
    jid_title_dic = {}

    for row in range(len(df_merge)):
        html = BeautifulSoup(df_merge["html"][row], "html.parser")
        script = html.find(
            "script", text=lambda text: text and "var jobKeysWithInfo" in text
        ).text
        for line in script.split("\n"):
            if line.startswith("jobKeysWithInfo"):
                if find_jid.search(line.replace("'", "")):
                    jid = find_jid.search(line.replace("'", "")).group(2)

                    jid_lo_dic[jid] = df_merge["location"][row]
                    jid_title_dic[jid] = df_merge["title"][row]

    jid_lo_df = pd.DataFrame(list(jid_lo_dic.items()))
    jid_lo_df.columns = ["jid", "location"]

    jid_title_df = pd.DataFrame(list(jid_title_dic.items()))
    jid_title_df.columns = ["jid", "title"]

    jid_lo_title_df = pd.merge(jid_lo_df, jid_title_df, how="inner", on="jid")

    return jid_lo_title_df


def select_job_postings():
    """Return a dataframe among 3 different jobs(DA,DS,DE)."""

    df_ramdom = jid_lo_title_df.loc[jid_lo_title_df["title"] == JOB_TITLE]

    return df_ramdom.reset_index()


def sleeper(min_sleep_sec, max_sleep_sec):
    """Give a random sleep time between min_sleep_sec and max_sleep_sec."""
    time_splits = np.linspace(min_sleep_sec, max_sleep_sec, num=60)
    alarm = np.random.choice(time_splits)
    rounding = np.random.choice(list(range(2, 6)))

    return time.sleep(round(alarm, rounding))


def get_job_des_html(df_merge):
    """Get every job description from the jid_list, and save it into database."""
    job_des_html_dic = {}
    success_counts = 1
    for jid in list(df_merge["jid"]):
        job_des_url = "https://www.indeed.com/viewjob?jk=" + jid
        job_des_response = requests.get(job_des_url)
        job_des_html = BeautifulSoup(job_des_response.text, "html.parser")
        job_des_html_dic[jid] = str(job_des_html)

        print(str(success_counts) + " job(s) succeeded.")

        sleeper(10.9866, 20.99999)

        success_counts += 1

    df_job_des_html = pd.DataFrame(list(job_des_html_dic.items()))
    df_job_des_html.columns = ["jid", "jidhtml"]
    df_job_des_html["title"] = JOB_TITLE

    return df_job_des_html


def jid_html_sql_db(df_job_des_html):
    """Upload job html tables with the same title to database"""

    schema = {
        "jid": String,
        "jidhtml": String,
        "title": String,
    }

    jid_db_name = f"job_des_html_{JOB_TITLE}".lower().replace(" ", "_")
    template_cmd = """
    create table if not exists {} (
        jid varchar,
        jidhtml varchar,
        title varchar
    );"""
    create_table_cmd = template_cmd.format(jid_db_name, jid_db_name)

    df_job_des_html.to_sql(
        jid_db_name, engine, if_exists="replace", dtype=schema, index=False
    )
    engine.connect().exec_driver_sql(create_table_cmd)


if __name__ == "__main__":
    df_merge = get_sql_table()
    jid_lo_title_df = get_jid_list(df_merge)
    df_merge_html = select_job_postings()
    df_job_des_html = get_job_des_html(df_merge_html)
    jid_html_sql_db(df_job_des_html)
