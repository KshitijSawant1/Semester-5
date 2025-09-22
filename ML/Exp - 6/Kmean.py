
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

ks = range(2, 10)
wcss = []
sil_scores = []

for k in ks:
    km = KMeans(n_clusters=k, n_init=10, random_state=42)
    km.fit(X_scaled)
    wcss.append(km.inertia_)
    labels = km.labels_
    sil_scores.append(silhouette_score(X_scaled, labels))

plt.figure(figsize=(6,4))
plt.plot(ks, wcss, marker='o')
plt.xlabel('k (number of clusters)')
plt.ylabel('WCSS (inertia)')
plt.title('Elbow Method')
plt.tight_layout()
plt.show()

plt.figure(figsize=(6,4))
plt.plot(ks, sil_scores, marker='s')
plt.xlabel('k (number of clusters)')
plt.ylabel('Silhouette Score')
plt.title('Silhouette vs k')
plt.tight_layout()
plt.show()

best_k = ks[int(np.argmax(sil_scores))]
print(f"Best k by silhouette: {best_k}")

k = best_k  
kmeans = KMeans(n_clusters=k, n_init=10, random_state=42)
labels = kmeans.fit_predict(X_scaled)

print("\nCluster sizes:", np.bincount(labels))
print("Cluster centroids (in scaled space):\n", kmeans.cluster_centers_)

pca = PCA(n_components=2, random_state=42)
X_2d = pca.fit_transform(X_scaled)

plt.figure(figsize=(8,5))
for c in range(k):
    plt.scatter(X_2d[labels==c, 0], X_2d[labels==c, 1], s=40, label=f'Cluster {c}')
centroids_2d = pca.transform(kmeans.cluster_centers_)
plt.scatter(centroids_2d[:,0], centroids_2d[:,1], c='black', s=120, marker='X', label='Centroids')
plt.title(f'K-Means (k={k}) on Iris (PCA 2D)')
plt.xlabel('PC1'); plt.ylabel('PC2'); plt.legend(); plt.tight_layout(); plt.show()

sil = silhouette_score(X_scaled, labels)
print(f"Silhouette Score (k={k}): {sil:.3f}")

true = iris.target
ct = pd.crosstab(pd.Series(labels, name='Cluster'), pd.Series(true, name='TrueSpecies'))
print("\nCluster vs True Species (for reference only):\n", ct)
