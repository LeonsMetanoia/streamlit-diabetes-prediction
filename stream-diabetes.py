import pickle 
import streamlit as st

# membaca model
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

# Judul web
st.title('Diabetes Prediction Model using Python')

# Membagai Column
col1, col2 = st.columns(2)

with col1 :
    Pregnancies = st.text_input('Input value Pregnancies')

with col2 :
    Glucose = st.text_input('Input value Glucose')

with col1 :
    BloodPressure = st.text_input('Input value BloodPressure')

with col2 :
    SkinThickness = st.text_input('Input value SkinThicknes')

with col1 :
    Insulin = st.text_input('Input value Insulin')

with col2 :
    BMI = st.text_input('Input value BMI')

with col1 :
    DiabetesPedigreeFunction = st.text_input('Input value DiabetesPedigreeFunction')

with col2 :
    Age = st.text_input('Input value Age')

# Code untuk prediksi
diab_diagnosis = ''


# Membuat tombol untuk Prediksi 
if st.button('Diabetes Prediction Test') :
    diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure,SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])


    if(diab_prediction[0] == 1):
        diab_diagnosis = 'Patient have Diabetes'
    else :
        diab_diagnosis = 'Patient does not have Diabetes'
    st.success(diab_diagnosis)
