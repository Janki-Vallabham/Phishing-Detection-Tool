# import numpy as np
# from flask import Flask, request, jsonify, render_template
# import pickle

# app = Flask(__name__)


# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/predict',methods=['POST'])
# def predict():
#     '''
#     For rendering results on HTML GUI
#     '''
#     data=[]
#     features = request.form["z1"]
#     data.append(features)
    
#     model = pickle.load(open('phishing.pkl', 'rb'))
#     result = model.predict(data)
#     if result[0]=="bad":
#         return render_template('index.html', prediction_text="This is a phising site")
#     else:
#         return render_template('index.html', prediction_text="This is not a phising site")


# if __name__ == "__main__":
#     app.run(debug=True)

import streamlit as st
import pickle
import numpy as np

# Load the model
model = pickle.load(open('phishing.pkl', 'rb'))

# Define the prediction function
def predict(features):
    data = np.array([features])
    result = model.predict(data)
    return result[0]

# Streamlit app
st.set_page_config(page_title='Phishing Detection', page_icon='🔍', layout='wide')

# Title and description
st.title('🔍 Phishing Detection')
st.markdown("""
    Welcome to the Phishing Detection App. Enter the necessary features to determine whether a website is a phishing site or not. 
    This application uses a machine learning model to make predictions based on the input features.
""")

# Input form
st.sidebar.header('Input Features')
z1 = st.sidebar.text_input('Enter the features')

# Predict button
if st.sidebar.button('Predict'):
    result = predict(z1)
    if result == "bad":
        st.error('🚨 This is a phishing site')
    else:
        st.success('✅ This is not a phishing site')

# Sidebar information
st.sidebar.markdown("""
    ## About
    This application is designed to help users detect phishing websites based on the provided features. 
    Make sure to input valid and complete information to get accurate results.
    
    ## How to use
    1. Enter the features in the input box.
    2. Click on the 'Predict' button to get the result.
""")

# Footer
st.markdown("---")
st.markdown("Created by [Your Name]. © 2024")

# CSS for styling
st.markdown(
    """
    <style>
    .reportview-container {
        background: #f0f2f6;
    }
    .sidebar .sidebar-content {
        background: #f0f2f6;
    }
    .css-1aumxhk {
        background-color: #ffffff;
    }
    .css-1v3fvcr {
        background-color: #ffffff;
    }
    </style>
    """,
    unsafe_allow_html=True
)


