import pandas as pd
import numpy as np
import streamlit as st 
import pickle as pk

# Load the model
model = pk.load(open(r'C:\Users\USER\Downloads\fdssss\_Heart_disease_model (1).pkl', 'rb'))

# Load the data
data = pd.read_csv(r'C:\Users\USER\Downloads\fdssss\heartprediction.csv')

st.header('Heart Disease Predictor')

# Create the select box for gender
gender = st.selectbox('Choose Gender', data['Gender'].unique())
gen = 1 if gender == 'Male' else 0

# Input fields for user data
age = st.number_input("Enter Age", min_value=0)
currentSmoker = st.number_input("Is Patient currentSmoker (0 for No, 1 for Yes)", min_value=0, max_value=1)
cigsPerDay = st.number_input("Enter cigsPerDay", min_value=0)
BPmeds = st.number_input("Is Patient on BPMeds (0 for No, 1 for Yes)", min_value=0, max_value=1)
prevalentStroke = st.number_input("Has patient had stroke (0 for No, 1 for Yes)", min_value=0, max_value=1)
prevalentHyp = st.number_input("Enter prevalentHyp status (0 for No, 1 for Yes)", min_value=0, max_value=1)
diabetes = st.number_input("Enter diabetes status (0 for No, 1 for Yes)", min_value=0, max_value=1)
totChol = st.number_input("Enter totChol", min_value=0)
sysBP = st.number_input("Enter sysBP", min_value=0)
diaBP = st.number_input("Enter diaBP", min_value=0)
BMI = st.number_input("Enter BMI", min_value=0.0)
heartRate = st.number_input("Enter heartRate", min_value=0)
glucose = st.number_input("Enter glucose", min_value=0)

# Predict button
if st.button('Predict'):
    input_data = np.array([[gen, age, currentSmoker, cigsPerDay, BPmeds, prevalentStroke, prevalentHyp, diabetes, totChol, sysBP, diaBP, BMI, heartRate, glucose]]) 
    
    st.write("Input data:", input_data)  # Print the input data for debugging
    
    output = model.predict(input_data)
    
    st.write("Model output:", output)  # Print the output for debugging
    
    if output[0] == 0:
        stn = 'Patient is Healthy, No heart disease'
    else:
        stn = 'Patient may have heart disease'
    
    st.markdown(stn)
