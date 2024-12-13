import streamlit as st
import joblib
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load the trained model
model = joblib.load("salary_model.joblib")

# Define LabelEncoders to match the ones used during training
gender_encoder = LabelEncoder()
education_encoder = LabelEncoder()

# Fit the LabelEncoders with the original categories
gender_encoder.fit(["Male", "Female"])
education_encoder.fit(["Bachelor's", "Master's", "PhD"])

# Streamlit UI
def main():
    st.title("Salary Prediction App")
    st.write("""
    Provide the following details to predict the salary:
    """)

    # User inputs
    age = st.number_input("Age", min_value=18, max_value=100, value=25, step=1)
    experience = st.number_input("Years of Experience", min_value=0.0, max_value=50.0, value=2.0, step=0.5)

    gender = st.selectbox("Gender", ["Male", "Female"])
    education = st.selectbox("Education Level", ["Bachelor's", "Master's", "PhD"])

    # Convert categorical data to numerical (using LabelEncoder)
    gender_num = gender_encoder.transform([gender])[0]
    education_num = education_encoder.transform([education])[0]

    # Prediction button
    if st.button("Predict Salary"):
        # Prepare input features for the model
        features = np.array([[age, gender_num, education_num, experience]])

        # Predict salary
        predicted_salary = model.predict(features)[0]

        # Display the result
        st.success(f"Predicted Salary: ${predicted_salary:,.2f}")

# Run the main function
if __name__ == "__main__":
    main()
