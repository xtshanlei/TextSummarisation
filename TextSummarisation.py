import streamlit as st
import spacy_streamlit
texts = st.text_area('Please type your texts here')
models = ["en_core_web_trf"]
spacy_streamlit.visualize(models, texts)
