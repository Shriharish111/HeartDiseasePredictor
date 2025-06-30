import streamlit as st
import pandas as pd
import numpy as np
import joblib
import google.generativeai as genai

#  Load Gemini API Key from Streamlit Secrets
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

#  Load model and scaler
model = joblib.load("heart_disease_model.pkl")
scaler = joblib.load("heart_scaler.pkl")

#  Streamlit page config
st.set_page_config(page_title="Heart Disease Predictor", page_icon="💓")
st.title("💓 Heart Disease Predictor")
st.markdown("Predict the **risk of heart disease** and get **AI health advice** with Gemini.")

#  User input form
def user_input():
    age = st.number_input("Age", 18, 100, 45)
    sex = st.selectbox("Sex", ("Male", "Female"))
    cp = st.selectbox("Chest Pain Type (0–3)", [0, 1, 2, 3])
    trestbps = st.number_input("Resting Blood Pressure (mm Hg)", 80, 200, 120)
    chol = st.number_input("Serum Cholesterol (mg/dl)", 100, 600, 200)
    fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1])
    restecg = st.selectbox("Resting ECG Results", [0, 1, 2])
    thalach = st.number_input("Max Heart Rate Achieved", 70, 210, 150)
    exang = st.selectbox("Exercise-Induced Angina", [0, 1])
    oldpeak = st.slider("ST Depression (Oldpeak)", 0.0, 6.0, 1.0)
    slope = st.selectbox("Slope of ST Segment", [0, 1, 2])
    ca = st.selectbox("Major Vessels Colored (0–3)", [0, 1, 2, 3])
    thal = st.selectbox("Thalassemia (0 = Normal, 1 = Fixed Defect, 2 = Reversible Defect)", [0, 1, 2])

    sex = 1 if sex == "Male" else 0

    data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg,
                      thalach, exang, oldpeak, slope, ca, thal]])
    return data

#  Gemini AI Advice Generator
def get_health_advice(prediction: int) -> str:
    prompt = f"""
You are a friendly AI health assistant. A patient was predicted to have {"high" if prediction == 1 else "no significant"} risk of heart disease.

1. Explain clearly what this result means.
2. Mention common causes or risk factors.
3. Give basic prevention tips (diet, lifestyle).
4. Recommend if/when they should consult a doctor.

Make your tone reassuring and simple.
"""
    model = genai.GenerativeModel("models/chat-bison-001")
    chat = model.start_chat()
    response = chat.send_message(prompt)
    return response.text.strip()

# 🚦 Run Prediction
input_data = user_input()

if st.button(" Predict"):
    scaled = scaler.transform(input_data)
    prediction = model.predict(scaled)[0]
    proba = model.predict_proba(scaled)[0]
    confidence = round(proba[prediction] * 100, 2)

    if prediction == 1:
        st.error(" **High risk of heart disease detected.**")
    else:
        st.success(" **No significant risk of heart disease detected.**")

    st.markdown(f"### Model Confidence: `{confidence}%`")
    st.progress(int(confidence))

    #  Risk Chart
    st.markdown("### Risk Probability")
    df = pd.DataFrame([proba], columns=["No Disease", "Disease"])
    st.bar_chart(df.T)

    # 💡 Gemini Health Advice
    if st.button(" Get AI Health Advice"):
        with st.spinner(" Gemini is preparing your health guidance..."):
            advice = get_health_advice(prediction)
            st.markdown("###  AI-Generated Health Advice")
            st.write(advice)
