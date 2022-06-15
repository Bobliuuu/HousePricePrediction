from asyncore import write
try:
    import StringIO
except ImportError:
    from io import StringIO 
import streamlit as st
import math
import pandas as pd
import pickle

a = st.selectbox("Table Of Contents: ", ["Introduction", "Linear Regression", "Quadratic Regression", "Exponential Regression", "Machine Learning"])

if a == "Linear Regression":
    st.title('Linear Regression')
    st.write('A linear regression model was created based on the sample data.')
    st.latex("y_1 \sim ax_1 + b ")
    st.latex("r^2 = 0.294")
    x = int(st.number_input('Size of Living Area:', 0, 1000000, 0, 1))
    st.write('Price of House: ' + str(60.40067407*x + 80101.1986))
elif a == "Quadratic Regression":
    st.title('Quadratic Regression')
    st.write('A quadratic regression model was created based on the sample data.')
    st.latex("y_1 \sim a{x_1}^2 + bx_1 + c ")
    st.latex("R^2 = 0.407")
    x = int(st.number_input('Size of Living Area:', 0, 1000000, 0, 1))
    st.write('Price of House: ' + str(-13459 + 168*x + -0.026*math.pow(x, 2)))
elif a == "Exponential Regression":
    st.title('Exponential Regression')
    st.write('A exponential regression model was created based on the sample data.')
    st.latex("y_1 \sim ae^{bx_1} ")
    st.latex("R^2 = 0.067")
    x = int(st.number_input('Size of Living Area:', 0, 1000000, 0, 1))
    st.write('Price of House: ' + str(103852*math.exp(0.000348*x)))
elif a == "Machine Learning":
    st.title('Machine Learning')
    st.write('A number of machine learning models were trained on the dataset, in a Google Colab notebook.')
    with open("notebooks/Machine_Learning.ipynb", "rb") as file:
        btn = st.download_button(
            label="Download Machine Learning Notebook",
            data=file,
            file_name="Machine_Learning.ipynb",
            mime="application/octet-stream" # Converts file data to byte stream, parsing to cout
        )
    st.write("From an analysis of the machine learning models, (see report), I decided to use the ensemble prediction method,",
    "with a stacked averaging meta-model, and XGBoost and Light GBM gradient boosting.")
    st.code("stacked_models = StackingAveragedModels(base_models = (enet_model, xgb_model, kri_model),"+
                                                 "meta_model = lasso_model")
    st.code("xgb_model = xgb.XGBRegressor(colsample_bytree=0.4603, gamma=0.0468,"+
                             "learning_rate=0.05, max_depth=3, "+
                             "min_child_weight=1.7817, n_estimators=2200, "+
                             "reg_alpha=0.4640, reg_lambda=0.8571, "+
                             "subsample=0.5213, silent=1, "+
                             "random_state=7, nthread=-1")
    st.code("lgb_model = lgb.LGBMRegressor(objective='regression', num_leaves=5,"
                              "learning_rate=0.05, n_estimators=720, "+
                              "max_bin=55, bagging_fraction=0.8, "+
                              "bagging_freq=5, feature_fraction=0.2319, "+
                              "feature_fraction_seed=9, bagging_seed=9, "+
                              "min_data_in_leaf=6, min_sum_hessian_in_leaf=11)")
    st.code("# After training each individual model\nensemble = stacked_pred*0.50 + xgb_pred*0.25 + lgb_pred*0.25")
    st.write("This code gave us the lowest RMSLE score of 1.1009.")

    with open('models/ensemble.pkl', 'rb') as f:
        ensemble = pickle.load(f)

    uploaded_file = st.file_uploader("Upload Testing Dataset")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        result = pd.DataFrame()
        result['Id'] = df['Id']
        result['SalePrice'] = ensemble
        s = StringIO()
        result.to_csv(s)
        csv_data = s.getvalue()
        btn = st.download_button(
            label="Sale Price Prediction Results",
            data=csv_data,
            file_name="result.csv",
            mime="text/csv" 
        )

    
elif a == "Introduction":
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
    st.write('To view pages, click on the dropdown bar at the top!')
