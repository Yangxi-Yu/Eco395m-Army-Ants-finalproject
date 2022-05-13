import pandas as pd
from bs4 import BeautifulSoup
import re
import numpy as np
import os
from database import engine
from sqlalchemy.types import String

TIME = input(" Please enter scraping time of data (Midterm/ Final/ All): ")


def get_sql_table():
    """read the merged html table from database into pandas dataframe"""
    if TIME == "Midterm":
        df_merged_tables_sql = pd.read_sql_table("old_merge_searched_job_html", engine)
    if TIME == "Final":
        df_merged_tables_sql = pd.read_sql_table("merge_searched_job_html", engine)
    if TIME == "All":
        df_merged_tables_sql = pd.read_sql_table("merge_searched_html_all", engine)
    return df_merged_tables_sql


def job_rating(card):
    """add rating column"""
    try:
        job_rating = card.find("span", "ratingsDisplay").a.text
    except AttributeError:
        job_rating = ""
    return job_rating


def job_salary(card):
    """add salary column"""
    try:
        job_salary = card.find(class_="salary-snippet-container").text
    except AttributeError:
        job_salary = ""
    if job_salary == "":
        try:
            job_salary = card.find(class_="metadata estimated-salary-container").text
        except AttributeError:
            job_salary = ""
    return job_salary


def clean_salary(df_basic):
    """add two more columns of salary range and mean values of salary"""
    resultlist = []
    mean_list = []
    for i in df_basic["salary"]:
        x = re.sub(",", "", i)
        result = re.findall("[0-9.]+", x)
        time_measure = re.findall("[A-Za-z]+", x)
        result = [float(r) for r in result]
        if "K" in time_measure:
            result = [1000 * r for r in result]
        else:
            result = result
        if "year" in time_measure:
            result = result
            mean = np.mean(result)
        elif "month" in x:
            result = [12 * i for i in result]
            mean = np.mean(result)
        else:
            result = []
            mean = ""
        resultlist.append(result)
        mean_list.append(mean)
    df_basic["salary_scale"] = resultlist
    df_basic["salary_mean"] = mean_list
    return df_basic


def find_jid(card):
    """add one column of jid"""
    try:
        result = card.find("a")["data-jk"]
    except (TypeError, KeyError) as error:

        try:
            result = str(card.parent.parent.parent.parent["data-jk"])
        except (TypeError, KeyError) as error:
            result = ""

    return result


def find_job_title(card):
    """add one column of job titles"""
    raw_title = card.h2.text
    if "new" in raw_title:
        title = raw_title[3:]
    else:
        title = raw_title
    return title


def df_basic(raw):
    """Set the structual of dataframe"""
    df = raw
    df_basic = pd.DataFrame(
        columns=(
            "job_title",
            "company_name",
            "location_in_detail",
            "salary",
            "rating",
            "jid",
            "title",
            "location",
        )
    )

    for index, row in df.iterrows():
        soup = BeautifulSoup(row[1], "html.parser")
        script = soup.find(
            "script", text=lambda text: text and "var jobKeysWithInfo" in text
        ).text
        cards = soup.find_all("div", class_="job_seen_beacon")
        result = [
            [
                card.h2.text,
                card.find("div", "heading6").contents[0].text,
                card.find("div", "companyLocation").text,
                job_salary(card),
                job_rating(card),
                find_jid(card),
            ]
            for card in cards
        ]
        """Add title """
        [result[i].append(row[2]) for i in range(len(result))]
        """Add location """
        [result[i].append(row[3]) for i in range(len(result))]

        for r in range(len(result)):
            df_basic = df_basic.append(
                pd.Series(
                    result[r],
                    index=[
                        "job_title",
                        "company_name",
                        "location_in_detail",
                        "salary",
                        "rating",
                        "jid",
                        "title",
                        "location",
                    ],
                ),
                ignore_index=True,
            )
        """return into dataframe with order"""
        df_basic = df_basic[
            [
                "job_title",
                "company_name",
                "location_in_detail",
                "salary",
                "rating",
                "jid",
                "title",
                "location",
            ]
        ]
        """clean salary """
        df_basic = clean_salary(df_basic).drop_duplicates(subset=["jid"])
    return df_basic


def job_info_sql_db(df_basic):
    """upload job basic information dataframe to database"""

    schema = {
        "job_title": String,
        "company_name": String,
        "location_in_detail": String,
        "salary": String,
        "rating": String,
        "jid": String,
        "title": String,
        "location": String,
        "salary_scale": String,
        "salary_mean": String,
    }

    db_table_name = f"job_basic_information_{TIME}".lower()

    create_table_cmd = """
    create table if not exists {} (
        job_title varchar,
        company_name varchar,
        location_in_detail varchar,
        salary varchar,
        rating varchar,
        jid varchar,
        title varchar,
        location varchar,
        salary_scale varchar,
        salary_mean varchar
    );""".format(
        db_table_name
    )

    df_basic.to_sql(
        db_table_name, engine, if_exists="replace", dtype=schema, index=False
    )
    engine.connect().exec_driver_sql(create_table_cmd)


if __name__ == "__main__":
    merged_searched_job_html = get_sql_table()
    df_basicinfo = df_basic(merged_searched_job_html)
    job_info_sql_db(df_basicinfo)
