# Salary Prediction

# Aim:
This project intends to predict salary based on features.

# Dataset:
The dataset has been acquired from Kaggle.com and uploaded in repositiory as "Salary Data.csv"
It has Age, Gender, Education, Job title and Salary of different employees.
I have used Age, Gender and Education as Independent Variables and Salary as dependent variable.

# Data Preparation:
I have used pandas library to load mu csv file into code. Employed various data cleaning techniques from pandas library. 
I have checked for null values and dropped them using "dropna" function in pandas library.

# Training:
Steps to train the model:
1. Take an instance of Linear Regression model from scikit-learn
2. Fit the model with seperated Independent and dependent variables (Input and output features).
3. Check R2 score to see how accurate the model is.

# Testing and deployment
Test the model by giving age, Educational level and Gender as Input. 

# Saving the model
Used joblib library to save the model for future use.

# Deploying of Stream-lit App
Created an app.py file which loads the saved model, acquires user information and predicts the salary.
This app.py file has been deployed using Streamlit.io from Github repository.
The libraries that are required for the code to work are listed in "requirements.txt" file.
