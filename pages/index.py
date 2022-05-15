import streamlit as st
from pages import index, problem, cleaning, processing, analysis, polate, advanced, prediction, conclude, references, code

def load_view():
    st.title('House Price Prediction 🏘️📈📉')
    st.header("Table Of Contents")
    st.subheader("1. The Problem")
    if st.button('link'):
        problem.load_view()