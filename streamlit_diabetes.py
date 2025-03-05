import pickle
import streamlit as st

# Membaca model
diabetes_model = pickle.load(open("diabetes_model.sav", "rb"))

# Judul Web
st.title("Data Mining Prediksi Diabetes")

# Membagi kolom

col1, col2 = st.columns(2)

with col1:
    pregnancies = st.number_input("Masukan nilai Pregnancies", value=None)

with col2:
    glucose = st.number_input("Masukan nilai Glucose", value=None)

with col1:
    blood_pressure = st.number_input("Masukan nilai Blood Pressure", value=None)

with col2:
    skinthickness = st.number_input("Masukan nilai Skin Thickness", value=None)

with col1:
    insulin = st.number_input("Masukan nilai Insulin", value=None)

with col2:
    bmi = st.number_input("Masukan nilai BMI", value=None)

with col1:
    diabetes_pedigree_function = st.number_input("Masukan nilai Diabetes Pedigree Function", value=None)

with col2:
    age = st.number_input("Masukan nilai Age", value=None)


# Code prediksi
diagnosis = ''

# Membuat tombol prediksi
hitung = st.button("Test Prediksi Diabetes")

# Logika hitung
if hitung:
    diabetes_prediction = diabetes_model.predict([[pregnancies, glucose, blood_pressure, skinthickness, insulin, bmi, diabetes_pedigree_function, age]])
    if diabetes_prediction[0] == 1:
        diagnosis = 'Pasien terkena diabetes'
    else:
        diagnosis = 'Pasien tidak terkena diabetes'
    st.success(diagnosis)
    
