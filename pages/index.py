import streamlit as st
import webbrowser
from pages import index, problem, cleaning, processing, analysis, polate, advanced, prediction, conclude, references, code
from streamlit.components.v1 import html

def load_view():
    st.title('House Price Prediction 🏘️📈📉')
    st.header("Table Of Contents")
    st.subheader("1. The Problem")
    