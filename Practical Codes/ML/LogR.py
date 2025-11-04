# ==== Logistic Regression ====
# Formula:
# P(y=1|x) = 1 / (1 + e^-(b0 + b1*x1 + b2*x2 + ... + bn*xn))
# The model predicts probabilities using the sigmoid function.

# ---- Imports ----
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score
# ---- Load dataset ----
iris = datasets.load_iris()
X = iris.data[:, :2]   # use first two features (Sepal length, Sepal width)
y = iris.target

# ---- Convert to Binary Problem (Setosa vs Versicolor only) ----
mask = y != 2          # exclude class 2 (Virginica)
X = X[mask]
y = y[mask]

df = pd.DataFrame(X, columns=iris.feature_names[:2])
df['target'] = y
print(df.head())

# ---- Split data ----
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ---- Train Logistic Regression Model ----
model = LogisticRegression()
model.fit(X_train, y_train)

# ---- Predict ----
y_pred = model.predict(X_test)

# ---- Evaluate ----
acc = accuracy_score(y_test, y_pred)
prec = precision_score(y_test, y_pred)
rec = recall_score(y_test, y_pred)

print(f"Accuracy  : {acc:.3f}")
print(f"Precision : {prec:.3f}")
print(f"Recall    : {rec:.3f}")

# ---- Decision Boundary Visualization ----
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.linspace(x_min, x_max, 200),
                     np.linspace(y_min, y_max, 200))

Z = model.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)

plt.contourf(xx, yy, Z, alpha=0.3, cmap='coolwarm')
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='coolwarm', edgecolor='k')
plt.title("Logistic Regression Decision Boundary")
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.show()

