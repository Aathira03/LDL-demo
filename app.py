import streamlit as st

st.set_page_config(page_title="PrediScan", layout="wide")

st.title("PrediScan - CVD Risk Prediction")

st.header("Step 1: Enter Basic Details")

name = st.text_input("Patient Name")
age = st.number_input("Age", 0, 120)

gender = st.selectbox("Gender", ["Male", "Female"])

alcohol = st.selectbox("Alcoholic Status", ["Yes", "No"])

smoking = st.selectbox("Smoking Status", ["Yes", "No"])

st.header("Step 2: Upload Fundus Images")

right_img = st.file_uploader("Upload Right Fundus Image", type=["jpg","png"])
left_img = st.file_uploader("Upload Left Fundus Image", type=["jpg","png"])

if st.button("Predict CVD Risk"):
    st.success("Prediction: Moderate Risk (Demo)")