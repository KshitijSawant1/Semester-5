# ==== K-Means Clustering ====
# Formula:
# J = Σ Σ || x_i - μ_j ||²   → Minimize the sum of squared distances 
# between each data point (x_i) and its assigned cluster centroid (μ_j)

# ---- Imports ----
from sklearn import datasets
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score, precision_score, recall_score
import numpy as np

# ---- Load dataset ----
iris = datasets.load_iris()
X = iris.data
y_true = iris.target  # True labels (for evaluation only)

# ---- Apply K-Means ----
kmeans = KMeans(n_clusters=3, random_state=42)
y_pred = kmeans.fit_predict(X)

# ---- Adjust cluster labels to match true labels ----
# (Because KMeans assigns arbitrary cluster numbers)
from scipy.stats import mode

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
