import re
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import numpy as np
from numpy.linalg import norm

def calculate_cosine_similarity(array_A, array_B):
    cosine = np.dot(array_A,array_B)/(norm(array_A)*norm(array_B))
    return cosine

def extract_features(data_source_df, data_source_column):
    vectorizer = CountVectorizer()
    vectorizer.fit(data_source_df[data_source_column].tolist())
    vector = vectorizer.transform(data_source_df[data_source_column].tolist())
    
    np_array = vector.toarray()
    np_index = data_source_df['jid'].tolist()
    np_columns = vectorizer.get_feature_names_out()


    features_df = pd.DataFrame(data = np_array, index = np_index, columns = np_columns)
    
    return features_df


def clean_input_text(input_text):
    resume_string_without_punctuation = re.sub(r'[^\w\s]', '', input_text)
    remove_line_break = re.sub('\n', ' ', resume_string_without_punctuation)
    remove_tab = re.sub('\t', '', remove_line_break)
    remove_extra_white_space = re.sub('\s+', ' ', remove_tab)
    cleaned_input_text = remove_extra_white_space.lower()
    return cleaned_input_text

