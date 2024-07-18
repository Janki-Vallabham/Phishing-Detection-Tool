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
st.title('Phishing Detection')

z1 = st.text_input('Enter the features')

if st.button('Predict'):
    result = predict(z1)
    if result == "bad":
        st.error('This is a phishing site')
    else:
        st.success('This is not a phishing site')
