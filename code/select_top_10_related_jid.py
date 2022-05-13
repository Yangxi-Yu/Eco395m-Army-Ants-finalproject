from msilib import schema
from database import engine
from sqlalchemy.types import String, Numeric
import pandas as pd
import numpy as np
from numpy.linalg import norm
from sklearn.feature_extraction.text import CountVectorizer


def extract_features(data_source_df, data_source_column):
    """""Extract input data features, save and return a dataframe.""" ""
    vectorizer = CountVectorizer()
    vectorizer.fit(data_source_df[data_source_column].tolist())
    vector = vectorizer.transform(data_source_df[data_source_column].tolist())

    np_array = vector.toarray()
    np_index = data_source_df["jid"].tolist()
    np_columns = vectorizer.get_feature_names()

    features_df = pd.DataFrame(data=np_array, index=np_index, columns=np_columns)

    features_df["jid"] = features_df.index
    return features_df


def calculate_cosine_similarity(array_A, array_B):
    """calculate cosine similarity"""
    cosine = np.dot(array_A, array_B) / (norm(array_A, axis=1) * norm(array_B))
    return cosine


def create_job_description_cosine_similarity_matrix(job_description_features_df):
    """Calculate cosine similarity between every jid and return a matrix."""
    cosine_similarity_df = pd.DataFrame(index=job_description_features_df["jid"])
    n_jid = 1
    for i in range(0, len(cosine_similarity_df)):
        jid = cosine_similarity_df.index[i]
        cosine_df_one_jid = pd.DataFrame(index=cosine_similarity_df.index)
        array_df = job_description_features_df.loc[
            :, job_description_features_df.columns != "jid"
        ]
        array_A = array_df.to_numpy()
        array_B = array_df.to_numpy()[i]
        cosine_df_one_jid[jid] = calculate_cosine_similarity(array_A, array_B)
        cosine_similarity_df = pd.concat(
            [cosine_similarity_df, cosine_df_one_jid], axis=1, join="inner"
        )
        print(f"{n_jid} completed.")
        n_jid += 1
    cosine_similarity_df["jid"] = cosine_similarity_df.index
    return cosine_similarity_df


def jid_top_10_related_job(job_description_cosine_similarity_df):
    """Find top 10 related jod."""
    job_description_cosine_similarity_df = job_description_cosine_similarity_df.set_index(
        "jid"
    )
    top_25_jid_df = pd.DataFrame()
    for jid in job_description_cosine_similarity_df.index:
        top_25_jid_list = (
            job_description_cosine_similarity_df[jid]
            .sort_values(ascending=False)
            .index[1:11]
        )
        df_one_row = pd.DataFrame(data=top_25_jid_list)
        df_one_row.rename(columns={"jid": jid}, inplace=True)
        df_one_row = df_one_row.T
        top_25_jid_df = pd.concat([top_25_jid_df, df_one_row])
    top_25_jid_df["jid"] = top_25_jid_df.index
    return top_25_jid_df


def top_10_to_sql(df):
    schema = {
        "top_1": String,
        "top_2": String,
        "top_3": String,
        "top_4": String,
        "top_5": String,
        "top_6": String,
        "top_7": String,
        "top_8": String,
        "top_9": String,
        "top_10": String,
        "jid": String,
    }

    create_table_cmd = """
    create table if not exists select_top_10 (
        top_1 varchar,
        top_2 varchar,
        top_3 varchar,
        top_4 varchar,
        top_5 varchar,
        top_6 varchar,
        top_7 varchar,
        top_8 varchar,
        top_9 varchar,
        top_10 varchar,
        jid varchar
        );


        """
    df.to_sql("select_top_10", engine, if_exists="replace", dtype=schema, index=False)
    engine.connect().exec_driver_sql(create_table_cmd)


if __name__ == "__main__":
    clean_job_des_df = pd.read_sql_table("merge_job_cleaned_description", engine)
    clean_job_des_df = clean_job_des_df.replace(np.nan, "")

    job_description_features_df = extract_features(
        clean_job_des_df, "clean_description_n_v_j_only"
    )

    job_description_cosine_similarity_df = create_job_description_cosine_similarity_matrix(
        job_description_features_df
    )

    top_10_jid_df = jid_top_10_related_job(job_description_cosine_similarity_df)
    top_10_jid_df = top_10_jid_df.rename(
        columns={
            0: "top_1",
            1: "top_2",
            2: "top_3",
            3: "top_4",
            4: "top_5",
            5: "top_6",
            6: "top_7",
            7: "top_8",
            8: "top_9",
            9: "top_10",
        }
    )
    top_10_to_sql(top_10_jid_df)
