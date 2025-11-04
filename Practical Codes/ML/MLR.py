# ==== Multiple Linear Regression ====
# Formula:  y = β0 + β1 x1 + β2 x2 + ... + βp xp
# where,
# y  = dependent variable (target)
# xj = j-th independent feature
# β0 = intercept
# βj = coefficient for feature j

# ---- Imports ----
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score,accuracy_score, precision_score, recall_score

# ---- Load dataset (all features) ----
diabetes = datasets.load_diabetes()
X = diabetes.data                  # shape: (n_samples, n_features=10)
y = diabetes.target                # disease progression

feature_names = diabetes.feature_names
df = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
df['target'] = diabetes.target

# Display first 5 rows
print(df.head())

# ---- Train/test split ----
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ---- Fit model ----
model = LinearRegression()
model.fit(X_train, y_train)

# ---- Predict ----
y_pred = model.predict(X_test)

# ---- Evaluate ----
mse = mean_squared_error(y_test, y_pred)
r2  = r2_score(y_test, y_pred)

print("Multiple Linear Regression: y = β0 + Σ βj * xj")
print("Intercept (β0):", model.intercept_)
print("Coefficients (β):")
for name, coef in zip(feature_names, model.coef_):
    print(f"  {name}: {coef}")

print(f"\nMean Squared Error: {mse:.2f}")
print(f"R² Score: {r2:.3f}")
acc = accuracy_score(y_test, y_pred)
prec = precision_score(y_test, y_pred, average='macro')
rec = recall_score(y_test, y_pred, average='macro')

print(f"Accuracy  : {acc:.3f}")
print(f"Precision : {prec:.3f}")
print(f"Recall    : {rec:.3f}")

# ---- Quick visualization: Predicted vs Actual ----
plt.scatter(y_test, y_pred, alpha=0.7)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', linewidth=2)
plt.xlabel("Actual Target")
plt.ylabel("Predicted Target")
plt.title("Predicted vs Actual (Diabetes dataset)")
plt.grid(True)
plt.show()
