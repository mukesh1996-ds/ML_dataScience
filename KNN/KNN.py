import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import cluster

df = pd.read_csv('Mall_Customers.csv')
print(df.head())

x = df.iloc[:,3:]
print(x)

from sklearn.cluster import KMeans
wcss = []
for i in range(1,15):
    kean = KMeans(n_clusters=i, init='k-means++', random_state=30)
    kean.fit(x)
    wcss.append(kean.inertia_)

print(wcss)

plt.plot(range(1,15), wcss)
plt.show()

k = KMeans(n_clusters=5,init='k-means++', random_state=30)
print(k.fit_predict(x))

x['cluster number'] = k.fit_predict(x)
print(x)

print(x[x['cluster number'] == 0])
print(x[x['cluster number'] == 1])
print(x[x['cluster number'] == 2])
print(x[x['cluster number'] == 3])
print(x[x['cluster number'] == 4])

print("new value:",k.predict([[55,31]]))

from sklearn.cluster import MiniBatchKMeans
mini = MiniBatchKMeans(n_clusters=5)
print(mini.fit(x))
#print(mini.predict([[55,32]]))

from sklearn.cluster import DBSCAN
dbscan = DBSCAN(eps=0.5, min_samples=5)
print(dbscan.fit(x))
print(dbscan.labels_)
print(set(dbscan.labels_))
print(len(set(dbscan.labels_)))
x['cluster number'] = dbscan.labels_
print(x.head())
from sklearn import metrics
print(metrics.adjusted_rand_score(mini, dbscan.labels_))
metrics.jaccard_score()




