# Heart Disease Predictor

A machine learning web app that predicts the risk of heart disease using patient medical data.  
This tool provides early indicators based on clinical inputs like blood pressure, cholesterol, age, etc.

Built using Streamlit and powered by a Random Forest Classifier trained on the UCI Heart Disease dataset.

______________________________________________________________________

## Features

- Predicts heart disease risk based on medical data
- Shows model confidence and probability distribution
- No external API keys required (fully standalone)
- Deployed using Streamlit Cloud
- Uses scikit-learn and joblib for model management

______________________________________________________________________

## How It Works

1. The user provides input such as age, sex, blood pressure, cholesterol, etc.
2. The input is scaled and passed to a trained Random Forest model
3. The app returns:
   - Risk prediction (Disease / No Disease)
   - Model confidence (percentage)
   - Visual probability bar chart

______________________________________________________________________

## Tech Stack

| Tool           | Purpose                          |
|----------------|----------------------------------|
| Streamlit      | UI & Deployment                  |
| scikit-learn   | Machine Learning model           |
| joblib         | Saving and loading models        |
| pandas, numpy  | Data processing and manipulation |

______________________________________________________________________

## Project Structure

HeartDiseasePredictor/
│
├── app.py # Main Streamlit application
├── heart_disease_model.pkl# Trained Random Forest model
├── heart_scaler.pkl # Scaler used for preprocessing
├── requirements.txt # List of dependencies
└── README.md # Project documentation

markdown
Copy
Edit

______________________________________________________________________

## Local Setup

1. Clone the repository:

git clone https://github.com/Shriharish111/HeartDiseasePredictor.git
cd HeartDiseasePredictor

cpp
Copy
Edit

2. Create and activate a virtual environment:

python -m venv venv
venv\Scripts\activate # On Windows
source venv/bin/activate # On macOS/Linux

markdown
Copy
Edit

3. Install the required packages:

pip install -r requirements.txt

markdown
Copy
Edit

4. Run the Streamlit app:

streamlit run app.py

markdown
Copy
Edit

______________________________________________________________________

## Dataset Information

- Dataset: UCI Heart Disease Dataset
- Features include:
  Age, Sex, Chest Pain Type, Resting Blood Pressure, Cholesterol, Fasting Blood Sugar, ECG, Max Heart Rate, Angina, ST Depression, Slope, Major Vessels, Thalassemia
- Target: 1 = Heart Disease Present, 0 = No Disease

______________________________________________________________________

## Author

Developed by Shri Harish  
Final Year CSE (AIML) Student  
Passionate about Game Development and Real-World AI Projects

______________________________________________________________________

## Disclaimer

This application is intended for educational and informational use only.  
It is not a substitute for professional medical advice or diagnosis.
