import streamlit as st
from utils import use_regex, remove_unwanted

import joblib

model = joblib.load('clf_rfc_model.joblib')

st.title('Sentiment Analyzer: Positive or Negative')
text_input = st.text_input("Enter text below. Please make sure that the text has atleast 15 words")


def predict():
    cleaned_text = use_regex(text=text_input)
    cleaned_text = remove_unwanted(text=cleaned_text)
    prediction = model.predict([cleaned_text])
    
    if prediction == 0:
        st.error('This looks like a negative text 😯')
    elif prediction == 1:
        st.success('This looks like a positive text 😊')

st.button('Predict', on_click=predict)

st.write('Example of positive text')
st.code(
    "I am grateful for the opportunities that come my way. Every day brings new possibilities and chances for growth. I embrace positivity and radiate happiness to those around me."
)
st.write('Example of negative text')
st.code(
    "I feel overwhelmed by the constant stress and pressure. It seems like nothing ever goes right, and I struggle to find any joy in my daily life. The future feels uncertain, and it's hard to stay motivated."
)