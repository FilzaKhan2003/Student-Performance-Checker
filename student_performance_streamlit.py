import streamlit as st
import numpy as np
import pickle
import joblib


st.title("Student's Performance Checker")

file = open('performance.pkl', 'rb')
model = joblib.load(file)

hr_std = st.number_input("Studied hour")
pr_scr = st.number_input("Previous score")
hr_slp = st.number_input("Sleep hours")
sp_ppr = st.number_input("No. of sample paper solved")
activi = st.radio('Activity',['Yes','No'])

act_num_1 = 1 if activi == "Yes" else 0
act_num_0 = 0 if activi == "No" else 1
input_data = np.array([hr_std,pr_scr,hr_slp,sp_ppr,act_num_0, act_num_1])
if st.button("Check Performance"):
    prediction = model.predict([input_data])
    
    st.write(f'Prediction : {round(prediction[0],2)}')


