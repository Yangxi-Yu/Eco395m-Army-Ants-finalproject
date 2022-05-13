import pandas as pd
from database import engine
from sqlalchemy.types import String, Numeric

def transform_similarity_matrix(variable):
    df_1=pd.read_sql_table(variable, engine)
    df_x=[]
    for index,row in df_1.iterrows():
        for i in range(1,len(row)):
            df_x.append([row["jid"],row[i],i])
    df_result=pd.DataFrame(df_x, columns = ["jid","jid_sim","top"])
    return df_result


def top_10_transform_sql(df):
    schema = {
        "jid" : String,
        "jid_sim" : String,
        "top" : Numeric,
    }

    create_table_cmd = """
    create table if not exists top_10_transform_sql (
        jid varchar,
        jid_sim varchar,
        top numeric
        );
        """
    df.to_sql("top_10_transform_sql", engine, if_exists = "replace", dtype = schema, index = False)
    engine.connect().exec_driver_sql(create_table_cmd)

    if __name__ == '__main__':
        transformed_sim=transform_similarity_matrix('top_10')
        top_10_transform_sql(transformed_sim)