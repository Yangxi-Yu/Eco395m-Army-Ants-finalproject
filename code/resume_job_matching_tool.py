from database import engine
import pandas as pd
import re
import numpy as np
from numpy.linalg import norm
from sklearn.feature_extraction.text import CountVectorizer
from datetime import date
from sqlalchemy.types import String, Numeric

def add_date_diff_column(job_posted_date_df):
    job_posted_date_df['date_diff'] = ''
    for i in range(0, len(job_posted_date_df)):
        if pd.isnull(job_posted_date_df.loc[i, 'date']):
            # in case of date is null
            job_posted_date_df.loc[i, 'date_diff'] = 100000000000
        else:
            job_posted_date_df.loc[i, 'date_diff'] = abs(job_posted_date_df['date'][i].date() - date.today()).days
    return job_posted_date_df


def data_source_filter(position, degree, location, exp_level, date_post):
    job_description_df = pd.read_sql_table("merge_job_cleaned_description", engine)
    job_basic_info_df = pd.read_sql_table("job_basic_information_all", engine)
    job_posted_date_df = pd.read_sql_table("merge_job_post_date", engine)
    
    
    job_description_df_part = job_description_df[['jid', 'title', 'clean_description_n_v_j_only', 'degree', 'exp_level']]
    job_basic_info_df_part = job_basic_info_df[['jid', 'location']]
    job_posted_date_df_part = job_posted_date_df[['jid', 'date']]
    
    data_source_df = job_description_df_part.merge(job_basic_info_df_part, how = 'left', on = 'jid')
    data_source_df = data_source_df.merge(job_posted_date_df_part, how = 'left', on = 'jid')
    data_source_df = add_date_diff_column(data_source_df)
    data_source_df = data_source_df.replace(np.nan, '')

    if position == 'All':
        position_da = 'Data Analyst'
        position_de = 'Data Engineer'
        position_ds = 'Data Scientist'
        positon_general = ''
    else:
        position_da = ''
        position_de = ''
        position_ds = ''
        positon_general = position
        
    if degree == 'phd':
        degree_phd = 'phd'
        degree_master = 'master'
        degree_bachelor = 'bachelor'
    elif degree == 'master':
        degree_phd = ''
        degree_master = 'master'
        degree_bachelor = 'bachelor'
    else:
        degree_phd = ''
        degree_master = ''
        degree_bachelor = 'bachelor'


    if location == 'All':
        location_ny = 'New York State'
        location_ca = 'California'
        location_tx = 'Texas'
        location = ''
    else:
        location_ny = ''
        location_ca = ''
        location_tx = ''
    
    data_source_filter_df = (data_source_df
                             .loc[data_source_df['title'] == (position_da or position_de or position_ds or positon_general)]
                             .loc[data_source_df['degree'] == (degree_phd or degree_master or degree_bachelor)]
                             .loc[data_source_df['exp_level'] == exp_level]
                             .loc[data_source_df['location'] == (location_ny or location_ca or location_tx or location)]
                             .loc[data_source_df['date_diff'] <= int(date_post)])
    
    
    return data_source_filter_df

def calculate_cosine_similarity(array_A, array_B):
    """calculate cosine similarity"""
    cosine = np.dot(array_A,array_B)/(norm(array_A)*norm(array_B))
    return cosine

def extract_features(data_source_df, data_source_column):
    """Extract input data features, save and return a dataframe."""
    vectorizer = CountVectorizer()
    vectorizer.fit(data_source_df[data_source_column].tolist())
    vector = vectorizer.transform(data_source_df[data_source_column].tolist())
    
    np_array = vector.toarray()
    np_index = data_source_df['jid'].tolist()
    np_columns = vectorizer.get_feature_names_out()


    features_df = pd.DataFrame(data = np_array, index = np_index, columns = np_columns)
    
    return features_df


def clean_input_text(input_text):
    """clean useless symbols in input text."""
    resume_string_without_punctuation = re.sub(r'[^\w\s]', '', input_text)
    remove_line_break = re.sub('\n', ' ', resume_string_without_punctuation)
    remove_tab = re.sub('\t', '', remove_line_break)
    remove_extra_white_space = re.sub('\s+', ' ', remove_tab)
    cleaned_input_text = remove_extra_white_space.lower()
    return cleaned_input_text

def convert_cleaned_input_to_array(cleaned_input_txt, job_description_features_df):
    """convert cleaned input text to an array."""
    input_feature = {}
    for feature in job_description_features_df.columns:
        if feature in cleaned_input_txt:
            input_feature[feature] = cleaned_input_txt.count(feature)
        else:
            input_feature[feature] = 0
    input_array = np.array(list(input_feature.values()))
    
    return input_array

def input_txt_return_top_50_related_job(job_description_features_df, cleaned_input_txt):
    """Find top 50 closest match job, return job ids and corresponding cosine similarity."""
    jid_cosine_similarity_dict = {}
    for jid in job_description_features_df.index:
        array_A = job_description_features_df.loc[jid].to_numpy()
        array_B = convert_cleaned_input_to_array(cleaned_input_txt, job_description_features_df)
        jid_cosine_similarity_dict[jid] = calculate_cosine_similarity(array_A, array_B)

    sorted_jid_cosine_similarity_dict = dict(sorted(jid_cosine_similarity_dict.items(), key=lambda item: item[1], reverse=True))
    jid_cosine_similarity_df = pd.DataFrame(sorted_jid_cosine_similarity_dict.items(), columns=['jid', 'cosine_similarity'])
    return jid_cosine_similarity_df.head(50)