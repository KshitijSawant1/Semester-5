# ==== K-Means Clustering ====
# Formula:
# J = Σ Σ || x_i - μ_j ||²   → Minimize the sum of squared distances 
# between each data point (x_i) and its assigned cluster centroid (μ_j)

# ---- Imports ----
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score, precision_score, recall_score
from scipy.stats import mode

# ---- Load dataset ----
iris = datasets.load_iris()
X = iris.data[:, :2]  # only first two features for 2D visualization
y_true = iris.target
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = iris.target
print(df.head())
# ---- Apply K-Means ----
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
y_pred = kmeans.fit_predict(X)

# ---- Adjust cluster labels to match true labels ----
labels = np.zeros_like(y_pred)
for i in range(3):
    mask = (y_pred == i)
    labels[mask] = mode(y_true[mask], keepdims=True)[0]

# ---- Evaluate ----
acc = accuracy_score(y_true, labels)
prec = precision_score(y_true, labels, average='macro')
rec = recall_score(y_true, labels, average='macro')

print(f"Accuracy  : {acc:.3f}")
print(f"Precision : {prec:.3f}")
print(f"Recall    : {rec:.3f}")

# ---- Simple Cluster Visualization ----
plt.scatter(X[:, 0], X[:, 1], c=y_pred, cmap='viridis', s=50)
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1],
            c='red', marker='*', s=200, label='Centroids')
plt.title('K-Means Clustering (Iris Data)')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.legend()
plt.show()
