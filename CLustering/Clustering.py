import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('glass.data')
print(df.head())
print(df.isnull().sum())

#  for decomposition we only need to work with feature column

df = df.drop(labels=['index', 'Class'], axis=1)
print(df)

# Rule 1 for PCA: mean = 0 and SD = 1
print(df.describe())
# not equal then we need to convert 
from sklearn.preprocessing import StandardScaler
scalar = StandardScaler()
scaled_data = scalar.fit_transform(df)
print(scaled_data)
data = pd.DataFrame(scaled_data,columns=df.columns)
print(data)
print(data.describe())
# egain vectore and egan matrix
# spilt variance ratio

from sklearn.decomposition import PCA
pca = PCA()
data1 = pd.DataFrame(pca.fit_transform(data))
print(data1)
print(pca.explained_variance_ratio_)
plt.figure()
plt.plot(np.cumsum(pca.explained_variance_ratio_))
plt.xlabel('number of columns')
plt.ylabel('EVR')
plt.show()
print(data1)

