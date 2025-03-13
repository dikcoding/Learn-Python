"K-Means Clustering sering digunakan untuk pengelompokan data, tapi bisa lambat untuk dataset besar."

from sklearn.cluster import KMeans
import numpy as np

# Buat dataset dummy
data = np.random.rand(100, 2)

# K-Means Clustering (O(n^2))
kmeans = KMeans(n_clusters=3)
kmeans.fit(data)

print("Cluster Centers:", kmeans.cluster_centers_)