import streamlit as st
from transformers import pipeline
summarizer = pipeline("summarization")

st.title('Text Summarisation by Yulei')
text = st.text_area('Please type the texts you want to summarise here.')
if not text:
    st.stop()
summary = summarizer(text[:1024], max_length=120, min_length=30, do_sample=False)

st.header('Please see your summarisation below:')
st.write(summary[0]['summary_text'])

from deep_translator import GoogleTranslator
translated = GoogleTranslator(source='auto', target='de').translate("keep it up, you are awesome")
st.write(translated)
