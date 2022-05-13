"""import libraries and packages"""
from database import engine
import pandas as pd
from bs4 import BeautifulSoup
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk.tokenize import word_tokenize
from sqlalchemy.types import String, Numeric
import re

def add_cleaned_html_text_column(job_description_html_df):
    """clean the html text, and generate it into a column"""
    len_df = len(job_description_html_df)
    job_description_html_df['clean_description'] = ''
    for i in range(0,len_df):
        html = BeautifulSoup(job_description_html_df['jidhtml'][i],'html.parser')
        script = html.find_all(id = 'jobDescriptionText')
        if script != []:
            extract_text = script[0].text
            # make all lower, and remove unecessary contents
            text_remove_punctuation = re.sub('[^A-Za-z\s]', '', extract_text.lower())
            text_with_only_spaces = re.sub("\s+", " ", text_remove_punctuation)
            cleaned_text = re.sub('\n', ' ', text_with_only_spaces)
            job_description_html_df['clean_description'][i] = cleaned_text
    return job_description_html_df

def add_v_n_j_only_description(job_description_html_df, raw_column_name, new_column):
    """clean the job description, and remove all the unmeaningful soft words"""
    job_description_html_df[new_column] = ''
    len_train = len(job_description_html_df)
    for row in range(0, len_train):
        clean_description = job_description_html_df[raw_column_name][row]
        split_by_word = word_tokenize(clean_description)

        n_v_j_txt = ""
        find_part_of_speech = nltk.pos_tag(split_by_word)
        for val in find_part_of_speech:
            if re.search(r'^V',val[1]) or re.search(r'^N',val[1]) or re.search(r'^J',val[1]):
                n_v_j_txt += val[0] 
                n_v_j_txt += " "
        job_description_html_df[new_column][row] = n_v_j_txt
    return job_description_html_df

def add_degree_column(job_description_html_df):
    len_df = len(job_description_html_df)
    job_description_html_df['degree'] = ''
    for i in range(0,len_df):
        html = BeautifulSoup(job_description_html_df['jidhtml'][i],'html.parser')
        script = html.find_all(id = 'jobDescriptionText')
        if re.search('bachelor', str(script).lower()) or re.search(' ba ', str(script).lower()) or re.search(' bs ', str(script).lower()) or re.search('undergraduate', str(script).lower()) or re.search(' b.a. ', str(script).lower()) or re.search(' b.s. ', str(script).lower()):
            job_description_html_df['degree'][i] = 'bachelor'
        elif re.search('master', str(script).lower()) or re.search(' ms ', str(script).lower()) or re.search(' ma ', str(script).lower()) or re.search(' m.s. ', str(script).lower()) or re.search(' m.a. ', str(script).lower()):
            job_description_html_df['degree'][i] = 'master'
        elif re.search(' phd ', str(script).lower()) or re.search('ph.d', str(script).lower()):
            job_description_html_df['degree'][i] = 'phd'
    return job_description_html_df

def add_experience_column(job_description_html_df):
    """add the experience column"""
    len_df = len(job_description_html_df)
    job_description_html_df['required_experience'] = ''
    for i in range(0,len_df):
        html = BeautifulSoup(job_description_html_df['jidhtml'][i],'html.parser')
        script = html.find_all(id = 'jobDescriptionText')
        if re.search('[0-9](.*) years(.*)experience', str(script).lower()):
            find_sentence = re.search('[0-9](.*) years(.*)experience', str(script).lower()).group(0)
            job_description_html_df['required_experience'][i] = re.search('[0-9]', find_sentence).group(0)
    return job_description_html_df

def add_experience_level_column(job_description_html_df):
    """add the experience level column"""
    len_df = len(job_description_html_df)
    job_description_html_df['exp_level'] = ''
    # define the range of different experience levels
    for i in range(0,len_df):
        if job_description_html_df['required_experience'][i] == '':
            job_description_html_df['exp_level'][i] = '0-3'
        elif int(job_description_html_df['required_experience'][i]) <= 3:
            job_description_html_df['exp_level'][i] = '0-3'
        elif int(job_description_html_df['required_experience'][i]) <= 5:
            job_description_html_df['exp_level'][i] = '3-5'
        elif int(job_description_html_df['required_experience'][i]) > 5:
            job_description_html_df['exp_level'][i] = '5+'
    return job_description_html_df

if __name__ == '__main__':

    job_description_html_df = add_cleaned_html_text_column(job_description_html_df)
    job_description_html_df = add_v_n_j_only_description(job_description_html_df, 'clean_description', 'clean_description_n_v_j_only')
