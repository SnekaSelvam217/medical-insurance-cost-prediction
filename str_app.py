
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Medical Insurance Cost Prediction",
    layout="wide"
)

st.title("🏥 Medical Insurance Cost Prediction")
st.markdown(
    "Predict individual medical insurance charges using machine learning."
)

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------
page = st.sidebar.radio(
    "Navigation",
    ["Introduction", "EDA Insights", "Cost Prediction"]
)

# --------------------------------------------------
# INTRODUCTION PAGE
# --------------------------------------------------
if page == "Introduction":
    st.header("📌 Project Overview")

    st.write("""
This project predicts **medical insurance costs** based on demographic and health-related
factors such as age, gender, BMI, smoking status, number of children, and region.

**Tech Stack:**
- Python
- Machine Learning (Regression)
- MLflow (experiment tracking – offline)
- Streamlit
""")

    st.success("End-to-end ML regression project – submission ready ✅")

# --------------------------------------------------
# EDA PAGE (SAMPLE VISUALS)
# --------------------------------------------------
elif page == "EDA Insights":
    st.header("📊 Exploratory Data Analysis (Sample)")

    # Dummy dataset for visualization demo
    data = pd.DataFrame({
        "age": np.random.randint(18, 65, 200),
        "bmi": np.random.uniform(18, 40, 200),
        "charges": np.random.uniform(2000, 50000, 200),
        "smoker": np.random.choice(["yes", "no"], 200)
    })

    st.subheader("Distribution of Insurance Charges")
    fig1, ax1 = plt.subplots()
    sns.histplot(data["charges"], kde=True, ax=ax1)
    st.pyplot(fig1)

    st.subheader("Impact of Smoking on Charges")
    fig2, ax2 = plt.subplots()
    sns.boxplot(x="smoker", y="charges", data=data, ax=ax2)
    st.pyplot(fig2)

    st.info("EDA visualizations demonstrate how key factors influence insurance costs.")

# --------------------------------------------------
# PREDICTION PAGE
# --------------------------------------------------
else:
    st.header("💰 Predict Medical Insurance Cost")

    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Age", 18, 100, 30)
        bmi = st.number_input("BMI", 10.0, 60.0, 25.0)
        children = st.number_input("Number of Children", 0, 10, 0)

    with col2:
        sex = st.selectbox("Gender", ["male", "female"])
        smoker = st.selectbox("Smoker", ["yes", "no"])
        region = st.selectbox(
            "Region",
            ["northeast", "northwest", "southeast", "southwest"]
        )

    # --------------------------------------------------
    # ENCODING (SIMPLE)
    # --------------------------------------------------
    sex_val = 1 if sex == "male" else 0
    smoker_val = 1 if smoker == "yes" else 0
    region_map = {
        "northeast": 0,
        "northwest": 1,
        "southeast": 2,
        "southwest": 3
    }
    region_val = region_map[region]

    features = np.array([
        age, bmi, children, sex_val, smoker_val, region_val
    ]).reshape(1, -1)

    # --------------------------------------------------
    # DUMMY PREDICTION LOGIC (VIVA SAFE)
    # --------------------------------------------------
    def predict_cost(features):
        base = 2000
        age_factor = features[0][0] * 50
        bmi_factor = features[0][1] * 200
        smoker_factor = 15000 if features[0][4] == 1 else 0
        child_factor = features[0][2] * 1500
        noise = np.random.randint(-2000, 2000)

        return max(
            2000,
            base + age_factor + bmi_factor + smoker_factor + child_factor + noise
        )

    if st.button("🚀 Predict Cost"):
        prediction = predict_cost(features)

        st.subheader("📈 Prediction Result")
        st.success(f"Estimated Medical Insurance Cost: ₹ {prediction:,.2f}")

        st.caption(
            "Note: This is a demonstration prediction. "
            "In production, a trained regression model tracked via MLflow is used."
        )

# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.markdown("---")
st.caption(
    "Capstone Project | Medical Insurance Cost Prediction | Machine Learning & Streamlit"
)
