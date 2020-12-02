import streamlit as st
from transformers import pipeline
import pydeepl

sentence = 'I like turtles.'
from_language = 'EN'
to_language = 'ES'

translation = pydeepl.translate(sentence, to_language, from_lang=from_language)
print(translation)

# Using auto-detection
translation = pydeepl.translate(sentence, to_language)
print(translation)
summarizer = pipeline("summarization")

st.title('Text Summarisation by Yulei')
text = st.text_area('Please type the texts you want to summarise here.')
if not text:
    st.stop()
summary = summarizer(text[:1024], max_length=120, min_length=30, do_sample=False)

st.header('Please see your summarisation below:')
st.write(summary[0]['summary_text'])

sentence = 'I like turtles.'
to_language = 'CH'

translation = pydeepl.translate(sentence, to_language)
st.write(translation)
