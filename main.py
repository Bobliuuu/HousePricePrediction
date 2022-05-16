import streamlit as st

a = st.selectbox("View Page: ", ["problem", "cleaning", "processing", "analysis", "polate", "advanced", "prediction"
                                 "conclude", "references", "code"])

if a == "problem":
    st.title('The Problem')
elif a == "cleaning":
    st.title('Cleaning The Data')
elif a == "processing":
    st.title('Initial Processing Of Data')
elif a == "analysis":
    st.title('Exploratory Data Analysis')
elif a == "polate":
    st.title('Interpolate and Extrapolate')
elif a == "advanced":
    st.title('Advanced Regression: Machine Learning')
elif a == "prediction":
    st.title('Machine Learning Prediction')
elif a == "conclude":
    st.title('Conclusions and Reflection')
elif a == "references":
    st.title('References: Works Cited')
elif a == "code":
    st.title('Code Snippets')
elif a == None:
    st.title('House Price Prediction 🏘️🏙️📈📉')