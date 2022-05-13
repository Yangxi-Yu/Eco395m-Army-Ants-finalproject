import pandas as pd
from bs4 import BeautifulSoup
import re
import numpy as np
import os
from database import engine
from sqlalchemy.types import String, Numeric


def get_sql_table():
    """read the table of all htmls from database into dataframe"""
    df_table = pd.read_sql_table("merge_searched_job_html", engine)
    return df_table


def job_post_date(card):
    """add one column of job posted date"""
    try:
        fromage_set = card.find("span", class_="date").text[6:].split()

        if fromage_set[0].isdigit():
            before = int(fromage_set[0])
        else:
            before = 0
    except AttributeError:
        before = ""
    return before


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


def df_basic(raw):
    """Set the structual of dataframe"""
    df = raw
    df_basic = pd.DataFrame(
        columns=(
            "jid",
            "fromage",
        )
    )

    for index, row in df.iterrows():
        soup = BeautifulSoup(row[1], "html.parser")
        cards = soup.find_all("div", class_="job_seen_beacon")
        result = [
            [
                find_jid(card),
                job_post_date(card),
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
                        "jid",
                        "fromage",
                        "title",
                        "location",
                    ],
                ),
                ignore_index=True,
            )
        """return into dataframe with order"""
        df_basic = df_basic[
            [
                "jid",
                "fromage",
                "title",
                "location",
            ]
        ]

    return df_basic


def job_info_sql_db(df_basic):
    """upload job basic information dataframe to database"""

    schema = {
        "jid": String,
        "fromage": String,
        "title": String,
        "location": String,
    }

    create_table_cmd = """
    create table if not exists job_post_date(

        jid varchar,
        fromage varchar,
        title varchar,
        location varchar
        

    );"""

    df_basic.to_sql(
        "job_post_date", engine, if_exists="replace", dtype=schema, index=False
    )
    engine.connect().exec_driver_sql(create_table_cmd)


if __name__ == "__main__":
    merged_searched_job_html = get_sql_table()
    df = df_basic(merged_searched_job_html)
    job_info_sql_db(df)
