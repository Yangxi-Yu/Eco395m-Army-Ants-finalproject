from database import engine
from sqlalchemy.types import String, Numeric
import pandas as pd


def merge_transform_skills(table):
    """pivot merge_job_skill_counts into Tableau-friendly form"""
    df = pd.read_sql_table(table, engine)
    skill_list = [column for column in df.keys()]
    skill_list
    df_1 = []
    for index, row in df.iterrows():
        for i in range(len(row) - 1):
            x = []
            if row[i] > 0:
                x = [row["jid"], row.index[i], row[i]]
                df_1.append(x)
    df_2 = pd.DataFrame(df_1, columns=["jid", "skill", "count"])
    return df_2


def job_skill_counts_sql_db(df_transform):
    """upload job basic information dataframe to database"""

    schema = {
        "jid": String,
        "skill": String,
        "count": Numeric,
    }

    create_table_cmd = """
    create table if not exists merge_job_skills_counts_transformed (
        jid varchar,
        skill varchar,
        count numeric,
        CONSTRAINT merge_job_skills_counts_transformed_key PRIMARY KEY (jid)
    );"""

    df_transform.to_sql(
        "merge_job_skills_counts_transformed",
        engine,
        if_exists="replace",
        dtype=schema,
        index=False,
    )
    engine.connect().exec_driver_sql(create_table_cmd)


if __name__ == "__main__":
    df_transform = merge_transform_skills("merge_job_skill_counts")
    job_skill_counts_sql_db(df_transform)
