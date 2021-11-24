import optuna
import xgboost as xgb
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

df = pd.read_csv('Admission_Predict.csv')
print(df.head())

x = df.iloc[:,1:8]
print('The feature column is: \n', x.head())
y = df.iloc[:,-1]
print('The label column is: \n', y.head())