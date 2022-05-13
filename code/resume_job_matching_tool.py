import re
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import numpy as np
from numpy.linalg import norm

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

def resume_job_matching():
    """Concatenate all the functions above."""
    position = input('Job Title(Data Analyst/ Data Engineer/ Data Scientist/ All): ')
    location = input('Location(New York State/ California/ Texas/ All):')
    date_post = input('Date Posted: Last __ Days.(Please enter a number)')
    degree = input('Highest Education(bachelor/ master/ phd): ')
    exp_level = input('Experience Level(0-3/ 3-5/ 5+):')
    input_text = input('Search Keywords or paste your resume:')
    
    data_source_filter_df = data_source_filter(position, degree, location, exp_level, date_post)
    
    if data_source_filter_df.empty:
        return print("Sorry, no job matches in our database.")
    else:
        
        job_description_features_df = extract_features(data_source_filter_df, 'clean_description_n_v_j_only')
        cleaned_input_txt = clean_input_text(input_text)
        resume_job_matching_df = input_txt_return_top_50_related_job(job_description_features_df, cleaned_input_txt)
        return resume_job_matching_df