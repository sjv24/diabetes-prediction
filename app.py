import streamlit as st
import numpy as np
import pickle

# Loading my model
classifier = pickle.load(open('diabetes_model.sav', 'rb'))
scaler = pickle.load(open('scaler.sav', 'rb'))

st.title("🩺 Diabetes Prediction System")

# BMI Calculation
with st.expander("💡 Don't know your BMI?"):
    height = st.number_input("Enter your height (in meters):", min_value=0.0, format="%.2f")
    weight = st.number_input("Enter your weight (in kilograms):", min_value=0.0, format="%.1f")
    if height > 0:
        bmi = weight / (height ** 2)
        st.success(f"Your BMI is: {bmi:.2f}")
    else:
        bmi = None

st.markdown("## 🔢 Enter Patient Information")

# Form inputs
pregnancies = st.number_input("How many times have you been pregnant?", min_value=0.0, step=1.0)
glucose = st.number_input("Glucose measurement:", min_value=0.0)
bp = st.number_input("Blood Pressure:", min_value=0.0)
skin_thickness = st.number_input("Skin Thickness:", min_value=0.0)
insulin = st.number_input("Insulin:", min_value=0.0)
bmi_input = st.number_input("What is your BMI?", value=bmi if bmi else 0.0)
dpf = st.number_input("Diabetes Pedigree Function:", min_value=0.0)
age = st.number_input("Age:", min_value=0.0, step=1.0)

# Predict
if st.button("🔍 Predict"):
    input_data = [pregnancies, glucose, bp, skin_thickness, insulin, bmi_input, dpf, age]
    input_np = np.asarray(input_data).reshape(1, -1)
    std_input = scaler.transform(input_np)
    prediction = classifier.predict(std_input)

    if prediction[0] == 1:
        st.error("⚠️ The patient is likely to have diabetes.")
    else:
        st.success("✅ The patient is not likely to have diabetes.")
