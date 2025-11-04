# ==== PCA (Principal Component Analysis) with Classifier ====
# Formula:
# Z = X * W
# where W = matrix of top k eigenvectors of (XᵀX)
# PCA reduces dimensionality by projecting data onto directions of maximum variance.

# ---- Imports ----
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score

# ---- Load dataset ----
iris = datasets.load_iris()
X = iris.data
y = iris.target
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = iris.target
print(df.head())
# ---- Split data ----
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ---- Apply PCA (reduce to 2 components) ----
pca = PCA(n_components=2)
X_train_pca = pca.fit_transform(X_train)
X_test_pca = pca.transform(X_test)

# ---- Train Logistic Regression ----
model = LogisticRegression(max_iter=200)
model.fit(X_train_pca, y_train)

# ---- Predict ----
y_pred = model.predict(X_test_pca)

# ---- Evaluate ----
acc = accuracy_score(y_test, y_pred)
prec = precision_score(y_test, y_pred, average='macro')
rec = recall_score(y_test, y_pred, average='macro')

print(f"Accuracy  : {acc:.3f}")
print(f"Precision : {prec:.3f}")
print(f"Recall    : {rec:.3f}")

# ---- Simple Visualization ----
plt.scatter(X_test_pca[:, 0], X_test_pca[:, 1], c=y_pred, cmap='viridis', s=60)
plt.title('PCA (2D) + Logistic Regression Classification')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.show()
