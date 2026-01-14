# 🏥 Medical Insurance Cost Prediction

## 📌 Project Overview
This project predicts **individual medical insurance costs** based on demographic and health-related factors such as age, gender, BMI, smoking status, number of dependents, and region.  
It demonstrates an **end-to-end machine learning workflow**, including data preprocessing, exploratory data analysis (EDA), regression modeling, MLflow experiment tracking, and deployment using Streamlit.

---

## 🎯 Objective
- Analyze key factors influencing medical insurance charges
- Train and evaluate multiple regression models
- Track experiments and models using MLflow
- Deploy a Streamlit application for real-time cost prediction

---

## 🧠 Domain
- Healthcare  
- Insurance  
- Machine Learning  

---

## 🛠 Skills & Technologies
- Python  
- Data Cleaning & Preprocessing  
- Exploratory Data Analysis (EDA)  
- Regression Models  
- MLflow (Experiment Tracking)  
- Streamlit  

---

## 📂 Dataset Description
**Dataset:** `medical_insurance.csv`

### Features
- `age` – Age of the individual  
- `sex` – Gender (male/female)  
- `bmi` – Body Mass Index  
- `children` – Number of dependents  
- `smoker` – Smoking status (yes/no)  
- `region` – Residential region  
- `charges` – Medical insurance cost (Target)

---

## 🔍 Approach

### 1️⃣ Data Preprocessing
- Checked for missing and duplicate values
- Encoded categorical variables
- Performed feature engineering

### 2️⃣ Exploratory Data Analysis (EDA)
- Distribution of charges
- Impact of smoking, age, and BMI on insurance cost
- Correlation analysis between numerical features
- Outlier detection

### 3️⃣ Model Development
Trained and evaluated multiple regression models:
- Linear Regression  
- Ridge Regression  
- Lasso Regression  
- Random Forest Regressor  
- XGBoost Regressor  

### 4️⃣ Model Evaluation
- RMSE
- MAE
- R² Score

### 5️⃣ MLflow Integration
- Logged experiments, metrics, and parameters
- Tracked model performance
- Registered best-performing model

### 6️⃣ Streamlit Application
- User inputs personal and health details
- Predicts estimated insurance cost
- Displays EDA insights

---

## 🖥 Streamlit App Features
- Interactive user input form
- Real-time insurance cost prediction
- Visual insights from EDA
- Simple and user-friendly UI

---

## 🚀 How to Run the Application

### 🔧 Install Dependencies
```bash
pip install -r requirements.txt
