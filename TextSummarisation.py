import streamlit as st
from transformers import pipeline
import wikipediaapi
keyword = st.text('Anything you want to look up?')
if not keyword:
    st.stop()
wiki_wiki = wikipediaapi.Wikipedia('en')
page_py = wiki_wiki.page(keyword)
if page_py.exists()==False:
    st.stop()
st.write(page_py)


summarizer = pipeline("summarization")

st.title('Text Summarisation by Yulei')
text = st.text_area('Please type the texts you want to summarise here.')
if not text:
    st.stop()
summary = summarizer(text[:1024], max_length=120, min_length=30, do_sample=False)

st.header('Please see your summarisation below:')
st.write(summary[0]['summary_text'])
