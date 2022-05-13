from database import engine


def merge_all_tables():
    """Merge all output tables from get_searched_job_html.py, return a dataframe in sql."""
    cmd = """
    create table merge_searched_job_html
    as
    select * from data_analyst_texas_30
    union
    select * from data_scientist_texas_30
    union
    select * from data_engineer_texas_30
    union
    select * from data_analyst_new_york_state_30
    union
    select * from data_scientist_new_york_state_30
    union
    select * from data_engineer_new_york_state_30
    union
    select * from data_analyst_California_30
    union
    select * from data_scientist_California_30
    union
    select * from data_engineer_California_30
    order by title, location, page;
    """

    with engine.connect() as connection:
        connection.exec_driver_sql(cmd)


if __name__ == "__main__":
    merge_all_tables()
