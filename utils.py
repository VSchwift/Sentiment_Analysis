import re
import spacy

nlp = spacy.load('en_core_web_sm')


def use_regex(text):
    # remove username
    text = re.sub(r'@[\w_]+', '', text) 
    # remove hashtag
    text = re.sub(r'#[\w]+', '', text) 
    # remove extra spaces
    text = re.sub('  +', ' ', text)
    return text

def remove_unwanted(text):
    doc = nlp(text)
    base_words = []
    final_base_words = ''
    for token in doc:
        if token.is_stop or token.is_punct or token.is_digit or token.like_email or token.like_url:
            continue
        base_words.append(token.lemma_)
        final_base_words = ' '.join(base_words)
    return final_base_words.lower().strip()