import re

def clean_input_text(input_text):
    resume_string_without_punctuation = re.sub(r'[^\w\s]', '', input_text)
    remove_line_break = re.sub('\n', ' ', resume_string_without_punctuation)
    remove_tab = re.sub('\t', '', remove_line_break)
    remove_extra_white_space = re.sub('\s+', ' ', remove_tab)
    cleaned_input_text = remove_extra_white_space.lower()
    return cleaned_input_text

