import streamlit as st

a = st.selectbox("View Page: ", ["intro", "linear", "quadratic", "exponential", "machine"])

if a == "linear":
    st.title('Linear Regression')
elif a == "quadratic":
    st.title('Cleaning The Data')
elif a == "exponential":
    st.title('Initial Processing Of Data')
elif a == "machine":
    st.title('Exploratory Data Analysis')
elif a == "intro":
    st.title('House Price Prediction 🏘️🏙️📈📉')
    st.write('A web application demonstrating the results and conclusions of the House Price Prediction report.')
    st.write('This applet is part of the the final project for the MDM4U course, hosted under the GNU General Public LIcense.')
    with open("House_Price_Prediction_Report.pdf", "rb") as file:
        btn = st.download_button(
            label="Download Report",
            data=file,
            file_name="House_Price_Prediction_Report.pdf",
            mime="application/octet-stream" # Converts file data to byte stream, parsing to cout
        )