import pandas as pd
import numpy as np
from pandas.core.tools.datetimes import Scalar
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, roc_auc_score,roc_curve
import matplotlib.pyplot as plt

data = pd.read_csv('diabetes.csv')
print(data)

print(data.describe())

x = data.drop(columns=['Outcome'])
y = data.Outcome
print(x,y)

Scalar = StandardScaler()
x_scaled = Scalar.fit_transform(x)
print(x_scaled)

x_train, x_test, y_train, y_test = train_test_split(x,y , test_size=0.25, random_state=30)

naive_bayes = GaussianNB()
naive_bayes.fit(x_train, y_train)

yhat = naive_bayes.predict(x_test)
print(naive_bayes.score(x_test,y_test))

