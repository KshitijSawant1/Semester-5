# ==== K-Nearest Neighbors (KNN) ====
# Formula:
# Distance(x, xi) = √Σ (xj - xij)²   →  Euclidean distance
# Class(x) = majority class among K nearest neighbors

# ---- Imports ----
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score

# ---- Load dataset ----
iris = datasets.load_iris()
X = iris.data[:, :2]  # only first two features for 2D visualization
y = iris.target
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = iris.target

# Display first 5 rows
print(df.head())
# ---- Split data ----
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ---- Train KNN Model ----
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

# ---- Predict ----
y_pred = knn.predict(X_test)

# ---- Evaluate ----
acc = accuracy_score(y_test, y_pred)
prec = precision_score(y_test, y_pred, average='macro')
rec = recall_score(y_test, y_pred, average='macro')

print(f"Accuracy  : {acc:.3f}")
print(f"Precision : {prec:.3f}")
print(f"Recall    : {rec:.3f}")

# ---- Simple Visualization (no mesh grid) ----
plt.figure(figsize=(6,5))
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_pred, cmap='coolwarm', label='Predicted')
plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap='coolwarm', alpha=0.4, marker='x', label='Train')
plt.title('KNN Classification (K=5)')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.legend()
plt.show()
