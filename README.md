# 💓 Heart Disease Predictor

A machine learning web app that helps predict the **risk of heart disease** based on patient medical data.  
This tool aims to provide early insights using clinical metrics like blood pressure, cholesterol, heart rate, and more.

Built entirely using **Streamlit** and trained with classical machine learning techniques.

---

## 🔍 Features

- 🧠 Heart disease risk prediction using trained ML model
- 📊 Confidence score and probability chart
- 🖥️ Deployed with **Streamlit Cloud**
- 🔐 No external API calls – fully standalone
- 💾 Model serialized using `joblib` for efficient deployment

---

## 🚀 How It Works

1. The user enters their health metrics (age, sex, blood pressure, cholesterol, etc.)
2. The model processes this input using a **Random Forest Classifier**
3. The app returns:
   - ✅ Risk prediction (`Disease` / `No Disease`)
   - 🎯 Model confidence (in %)
   - 📈 Probability distribution bar chart

---

## 🧠 Tech Stack

| Tool              | Purpose                          |
|-------------------|----------------------------------|
| `Streamlit`       | UI & web app deployment          |
| `scikit-learn`    | Model training & prediction      |
| `joblib`          | Model + Scaler serialization     |
| `pandas` & `numpy`| Data wrangling                   |

---

## 📁 Project Structure

HeartDiseasePredictor/
│
├── app.py ← Main Streamlit web app
├── heart_disease_model.pkl← Trained Random Forest model
├── heart_scaler.pkl ← StandardScaler for inputs
├── requirements.txt ← All project dependencies
└── README.md ← You're here!

yaml
Copy
Edit

---

## 🛠️ Local Setup

1. **Clone the repository:**

```
bash
git clone https://github.com/Shriharish111/HeartDiseasePredictor.git
cd HeartDiseasePredictor
Create and activate a virtual environment:

bash
Copy
Edit
python -m venv venv
venv\Scripts\activate        # On Windows
# OR
source venv/bin/activate     # On Linux/Mac
Install all dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the app locally:

bash
Copy
Edit
streamlit run app.py
```
🌐 Live Demo
🔗 Click here to launch the app on Streamlit Cloud

## 📊 Dataset Information
 - Source: UCI Heart Disease Dataset

 - Attributes Used:
      Age, Sex, Chest Pain Type, Resting Blood Pressure, Cholesterol, Fasting Blood Sugar, Resting ECG, Max Heart Rate, Exercise-induced Angina, ST Depression, Slope, Number     of Major Vessels, Thalassemia

 - Target Label:
   1 = Disease present, 0 = No disease

## 👨‍💻 Author
Made with ❤️ by Shri Harish
 - 🎓 Final Year CSE (AIML) Student
 - 🎮 Passionate about Single-Player Games & Game Development
 - 🚀 Building real-world projects in AI & Python

## ⚠️ Disclaimer
 - This tool is for educational and informational purposes only.
 - It does not provide medical diagnosis and should not be used as a substitute for professional healthcare advice.

