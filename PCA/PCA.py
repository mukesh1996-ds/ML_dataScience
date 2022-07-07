import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

# Laoding the data = cancer dataset
from sklearn.datasets import load_breast_cancer
cancer = load_breast_cancer()
print(cancer)
print(cancer.keys())
print(cancer['DESCR'])

# Data frame
df = pd.DataFrame(cancer['data'],columns=cancer['feature_names'])
#(['DESCR', 'data', 'feature_names', 'target_names', 'target'])

print(df.head())

# step 1 
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(df)
scaled_data = scaler.transform(df)

# applying PCA
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
pca.fit(scaled_data)

x_pca = pca.transform(scaled_data)
print(x_pca)
print(scaled_data.shape)
print(x_pca.shape)

# Visualization
plt.figure(figsize=(8,6))
plt.scatter(x_pca[:,0],x_pca[:,1],c=cancer['target'],cmap='plasma')
plt.xlabel('First principal component')
plt.ylabel('Second Principal Component')
plt.show()

print(pca.components_)
df_comp = pd.DataFrame(pca.components_,columns=cancer['feature_names'])
print(df_comp)

plt.figure(figsize=(12,6))
sns.heatmap(df_comp,cmap='plasma',)






