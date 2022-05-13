import requests
from bs4 import BeautifulSoup
import numpy as np
import time
from re import A
import pandas as pd
from sqlalchemy.types import String, Numeric
from database import engine


def get_jid_url(position, location, fromage, sort):
    """Generate a url from position, location, date and sort."""

    template = "https://www.indeed.com/jobs?q={}&l={}&fromage={}&sort={}"
    url = template.format(position, location, fromage, sort)

    return url


def sleeper(min_sleep_sec, max_sleep_sec):
    """Give a random sleep time between min_sleep_sec and max_sleep_sec."""

    time_splits = np.linspace(min_sleep_sec, max_sleep_sec, num=60)
    alarm = np.random.choice(time_splits)
    rounding = np.random.choice(list(range(2, 6)))

    return time.sleep(round(alarm, rounding))


def get_searched_job_html():
    """Find all results that match the 4 search conditions and upload results to database."""

    position = input("Please enter a position: ")
    location = input("Please enter a location: ")
    fromage = input("Please enter a date range (0 - 30): ")
    sort = input("Please choose date/relevance: ")

    page_html_dict = {}
    page_number = 1
    url = get_jid_url(position, location, fromage, sort)

    while True:
        response = requests.get(url)
        html = BeautifulSoup(response.text, "html.parser")

        page_html_dict[page_number] = str(html)
        print("Page " + str(page_number) + " completed")

        try:
            url = "https://www.indeed.com" + html.find("a", {"aria-label": "Next"}).get(
                "href"
            )
            page_number += 1
            sleeper(10.166, 50.233)

        except AttributeError:
            break

    df1 = pd.DataFrame(page_html_dict.items())
    df1.columns = ["page", "html"]
    df1["title"] = position
    df1["location"] = location
    
    schema = {
        "page": Numeric,
        "html": String,
        "title": String,
        "location": String,
    }

    table_name = f"{position}_{location}_{fromage}".lower().replace(" ", "_")

    create_table_cmd = f"""
    create table if not exists {table_name} (
        page numeric,
        html varchar,
        title varchar,
        location varchar
    );
"""

    engine.connect().exec_driver_sql(create_table_cmd)
    df1.to_sql(table_name, engine, if_exists="replace", dtype=schema, index=False)


if __name__ == "__main__":

    get_searched_job_html()
