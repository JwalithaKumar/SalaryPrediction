#importing libraries
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import pandas as pd
#load the data
sald = pd.read_csv("/content/Salary Data.csv")
#view data
sald.head()
#check for null values
sald.isnull().sum()
#drop the nulls
sald.dropna(inplace = True)
#check for null values
sald.isnull().sum()
#preprocessing data
le = LabelEncoder()
le1 = LabelEncoder()
sald['Gender'] = le.fit_transform(sald['Gender'])
sald['Education Level'] = le1.fit_transform(sald['Education Level'])
#male-1, female =0
#0= bach, 1=master , 2 =Phd
#prepare data
inde = sald[['Age','Gender','Education Level','Years of Experience']]
dep = sald['Salary']
#create empty model
LR = LinearRegression()
#fit the model
LR.fit(inde,dep)
age = float(input("Enter your age: "))
gen = input("Enter Gender: ")
el = input("Enter Education levelm: ")
exp = float(input("Enter you experience in years: "))
gen = le.transform([gen])[0]
el = le1.transform([el])[0]
out = LR.predict([[age,gen,el,exp]])
print("You predicted salary is", out[0])
from sklearn.metrics import mean_squared_error
pval = LR.predict(inde)
mse = mean_squared_error(dep, pval)
print("Mean Squared Error:", mse)
import joblib
joblib.dump(LR, 'salary_model.joblib')
