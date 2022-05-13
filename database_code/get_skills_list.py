import pandas as pd
from bs4 import BeautifulSoup
from database import engine
from sqlalchemy.types import Numeric, String
import re
import os

JOB_TITLE = input(
    "Please enter a job title (Data Analyst/ Data Scientist/ Data Engineer): "
)
TIME = input("Please enter scraping time of data (Midterm/ Final): ")


def get_sql_db(JOB_TITLE, TIME):
    """Load a certain job database from database"""

    if TIME == "Midterm":
        df_job_des_html = pd.read_sql_table(
            f"job_des_html_{TIME}_{JOB_TITLE}".lower().replace(" ", "_"), engine
        )
    if TIME == "Final":
        df_job_des_html = pd.read_sql_table(
            f"job_des_html_{JOB_TITLE}".lower().replace(" ", "_"), engine
        )

    return df_job_des_html


def get_lowercase_skill_list():
    """Lowercase all the words in skill list."""
    df_skill_list = pd.read_sql_table("skill_list", engine)
    skill_list = df_skill_list["skills"].tolist()

    cleaned_skill_list = []
    for skill in skill_list:
        cleaned_skill_list.append(skill.lower())

    return cleaned_skill_list


def get_job_des_scripts(JOB_TITLE, TIME):
    """Clean html file and generate the job description part, return a dataframe that contains job id and job description."""
    df_job_des_html = get_sql_db(JOB_TITLE, TIME)
    jid_scripts_dict = {}

    for row in range(len(df_job_des_html)):
        html = BeautifulSoup(df_job_des_html["jidhtml"][row], "html.parser")
        script = html.find_all(id="jobDescriptionText")
        jid = df_job_des_html["jid"][row]
        jid_scripts_dict[jid] = script

    jid_scripts_df = pd.DataFrame(list(jid_scripts_dict.items()))
    jid_scripts_df.columns = ["jid", "scripts"]

    return jid_scripts_df


def job_des_lines(jid_scripts_df):
    """Generate a datadrame that contains jid and corresponding cleaned jobe description."""
    job_des_lines_dic = {}

    for row in range(len(jid_scripts_df)):
        script = jid_scripts_df["scripts"][row]

        cleaned_script_lines = []
        for line in str(script).split("\n"):
            line_pre = re.sub("<", " ", line)
            line_post = re.sub(">", " ", line_pre)
            clean_line = re.sub("[^A-Za-z\s]", "", line_post)

            cleaned_script_lines.append(clean_line.lower().strip())

        job_des_lines_dic[jid_scripts_df["jid"][row]] = cleaned_script_lines

    job_des_lines_df = pd.DataFrame(list(job_des_lines_dic.items()))
    job_des_lines_df.columns = ["jid", "cleaned_description"]

    return job_des_lines_df


def count_job_des_skills(cleaned_skill_list, job_des_lines_df):
    """Count the number of words in each job description, return a dataframe that contains job id and all skill counts."""

    df = pd.DataFrame(columns=cleaned_skill_list + ["jid"])

    for row in range(len(job_des_lines_df)):

        cleaned_skill_dict = dict.fromkeys(cleaned_skill_list, 0)

        for line in job_des_lines_df["cleaned_description"][row]:
            for word in line.split():
                if word in cleaned_skill_dict:
                    cleaned_skill_dict[word] = cleaned_skill_dict[word] + 1

        cleaned_skill_df = pd.DataFrame(list(cleaned_skill_dict.items()))
        transpose_cleaned_skill_df = cleaned_skill_df.transpose()
        transpose_cleaned_skill_df.columns = transpose_cleaned_skill_df.iloc[0]
        transpose_cleaned_skill_df = transpose_cleaned_skill_df[1:]
        transpose_cleaned_skill_df["jid"] = job_des_lines_df["jid"][row]

        df = pd.concat([transpose_cleaned_skill_df, df], ignore_index=True, sort=False)

    return df


def job_skill_sql_db(df):

    schema = {
        "statistics": Numeric,
        "etl": Numeric,
        "snowflake": Numeric,
        "cloud": Numeric,
        "ml": Numeric,
        "pytorch": Numeric,
        "linux": Numeric,
        "sql": Numeric,
        "excel": Numeric,
        "python": Numeric,
        "r": Numeric,
        "office": Numeric,
        "pandas": Numeric,
        "numpy": Numeric,
        "scipy": Numeric,
        "fortran": Numeric,
        "julia": Numeric,
        "c": Numeric,
        "java": Numeric,
        "javascript": Numeric,
        "html": Numeric,
        "perl": Numeric,
        "css": Numeric,
        "c++": Numeric,
        "kubernetes": Numeric,
        "docker": Numeric,
        "jenkins": Numeric,
        "apache": Numeric,
        "hadoop": Numeric,
        "scala": Numeric,
        "pig": Numeric,
        "kinesis": Numeric,
        "kafka": Numeric,
        "mapreduce": Numeric,
        "hbase": Numeric,
        "storm": Numeric,
        "flink": Numeric,
        "oracle": Numeric,
        "sap": Numeric,
        "salesforce": Numeric,
        "mysql": Numeric,
        "nosql": Numeric,
        "access": Numeric,
        "postgresql": Numeric,
        "mongodb": Numeric,
        "redis": Numeric,
        "aws": Numeric,
        "azure": Numeric,
        "bigquery": Numeric,
        "tableau": Numeric,
        "powerbi": Numeric,
        "bi": Numeric,
        "powerpoint": Numeric,
        "looker": Numeric,
        "matplotlib": Numeric,
        "rapidminer": Numeric,
        "nlp": Numeric,
        "tensorflow": Numeric,
        "sas": Numeric,
        "spss": Numeric,
        "stata": Numeric,
        "matlab": Numeric,
        "xml": Numeric,
        "json": Numeric,
        "jira": Numeric,
        "scrum": Numeric,
        "anaconda": Numeric,
        "jupyter": Numeric,
        "github": Numeric,
        "agile": Numeric,
        "jid": String,
    }

    table_name = f"job_skill_counts_{JOB_TITLE}_{TIME}".lower().replace(" ", "_")
    template_cmd = """
        create table if not exists {} (
            statistics numeric,
            etl numeric,
            snowflake numeric,
            cloud numeric,
            ml numeric,
            pytorch numeric,
            linux numeric,
            sql numeric,
            excel numeric,
            python numeric,
            r numeric,
            office numeric,
            pandas numeric,
            numpy numeric,
            scipy numeric,
            fortran numeric,
            julia numeric,
            c numeric,
            java numeric,
            javascript numeric,
            html  numeric,
            perl numeric,
            css numeric,
            "c++" numeric,
            kubernetes numeric,
            docker numeric,
            jenkins numeric,
            apache numeric, 
            hadoop numeric,
            scala numeric,
            pig numeric,
            kinesis numeric,
            kafka numeric,
            mapreduce numeric,
            hbase numeric,
            storm numeric,
            flink numeric,
            oracle numeric,
            sap numeric,
            salesforce numeric,
            mysql numeric,
            nosql numeric,
            access numeric,
            postgresql numeric,
            mongodb numeric,
            redis numeric,
            aws numeric,
            azure numeric,
            bigquery numeric,
            tableau numeric,
            powerbi numeric,
            bi numeric,
            powerpoint numeric,
            looker numeric,
            matplotlib numeric,
            rapidminer numeric,
            nlp numeric,
            tensorflow numeric,
            sas numeric,
            spss numeric,
            stata numeric,
            matlab numeric,
            xml numeric,
            json numeric,
            jira numeric, 
            scrum numeric,
            anaconda numeric,
            jupyter numeric,
            github numeric,
            agile numeric,
            jid varchar);
    """
    create_table_cmd = template_cmd.format(table_name)
    df.to_sql(table_name, engine, if_exists="replace", dtype=schema, index=False)
    engine.connect().exec_driver_sql(create_table_cmd)


if __name__ == "__main__":
    cleaned_skill_list = get_lowercase_skill_list()
    jid_scripts_df = get_job_des_scripts(JOB_TITLE, TIME)
    job_des_lines_df = job_des_lines(jid_scripts_df)
    df = count_job_des_skills(cleaned_skill_list, job_des_lines_df)
    job_skill_sql_db(df)
