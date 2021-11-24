import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#from pandas_profiling import ProfileReport
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle as pkl

df = pd.read_csv('diabetes.csv')
print('Dataset is....:\n', df.head())

#print('Cheching the profile report')
#report = ProfileReport(df)
#print(report.to_widgets())

print("Checking the null values \n",df.isnull().sum())
print(df.describe())

"""
from the visualization we can see that maximum of my data lie between 0 so we need to replace it 
"""

df['BMI'] = df['BMI'].replace(0, df['BMI'].mean())
df['BloodPressure'] = df['BloodPressure'].replace(0, df['BloodPressure'].mean())
df['Glucose'] = df['Glucose'].replace(0, df['Glucose'].mean())
df['Insulin'] = df['Insulin'].replace(0, df['Insulin'].mean())
df['Pregnancies'] = df['Pregnancies'].replace(0, df['Pregnancies'].mean())
df['SkinThickness'] = df['SkinThickness'].replace(0, df['SkinThickness'].mean())
df['DiabetesPedigreeFunction'] = df['DiabetesPedigreeFunction'].replace(0, df['DiabetesPedigreeFunction'].mean())

print(df.head())
print("The describe function \n",df.describe())

"""
From the visualization we can see that their exit an outlier we need to handle it.
"""

q = df['Pregnancies'].quantile(0.98) # removing 2% of data from Pregnancies column
df_clean = df[df['Pregnancies']<q]
q = df_clean['BMI'].quantile(0.99) # removing 1% of data from BMI
df_clean = df_clean[df_clean['BMI']<q]
q = df_clean['SkinThickness'].quantile(0.99) # removing 1% of data from skinthickness
df_clean = df_clean[df_clean['SkinThickness']<q]
q = df_clean['Insulin'].quantile(0.95) # removing 5% of data from Insuline
df_clean = df_clean[df_clean['Insulin']<q]
q = df_clean['DiabetesPedigreeFunction'].quantile(0.99) # removing 1% of data
df_clean = df_clean[df_clean['DiabetesPedigreeFunction']<q]
q = df_clean['Age'].quantile(0.99)
df_clean = df_clean[df_clean['Age']<q]

print('The cleaned data is \n', df_clean)
print('Describe function is \n', df_clean.describe())


# seperation 
x = df.drop(columns= ['Outcome'])
print(x.head())
y = df['Outcome']
print(y.head())

# Preprocessing
scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)
print(x_scaled)

# converting the array to pandas dataframe
df_scaled = pd.DataFrame(x_scaled, columns=x.columns)
print(df_scaled)

# checking the multicolinearity
vif = pd.DataFrame()
vif['VIF factor'] = [variance_inflation_factor(x_scaled, i) for i in range(x_scaled.shape[1])]
vif['features'] = x.columns
print('The variance influence factor is \n', vif)

# spliting the dataset into train_test_split
x_train, x_test , y_train, y_test = train_test_split(x_scaled, y, test_size=0.2, random_state=30)

# model building
from sklearn.linear_model import LogisticRegression
logistic_regression = LogisticRegression()
logistic_regression.fit(x_train,y_train)

pred = logistic_regression(x_test)

# once the model is built we need to dump it.
with open('Diabetic.pkl', 'wb') as f:
    pkl.dump(logistic_regression, f)

with open('sandardscaler.sav', 'wb') as f:
    pkl.dump(scaler, f)

