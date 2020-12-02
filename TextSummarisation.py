import streamlit as st
from transformers import pipeline
def summary(text):
    summarizer = pipeline("summarization")
    summary = summarizer(text[:1024], max_length=120, min_length=30, do_sample=False)
    return summary[0]['summary_text']
st.title('Text Summarisation by Yulei')
text = st.text_area('Please type the texts you want to summarise here.')
if not text:
    st.stop()

st.header('Please see your summarisation below:')
st.write(summary(text))

from deep_translator import GoogleTranslator
translated = GoogleTranslator(source='auto', target='zh-cn').translate(summary(text))
st.write(translated)
