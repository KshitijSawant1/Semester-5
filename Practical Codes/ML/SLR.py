# ==== Simple Linear Regression ====
# Formula:  y = mX + c
# where,
# y = dependent variable (target)
# X = independent variable (feature)
# m = slope / coefficient
# c = intercept

# ==== Step 1: Import Libraries ====
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# ==== Step 2: Load Dataset ====
# Using the Diabetes dataset from sklearn
diabetes = datasets.load_diabetes()

# Take only one feature (for simple linear regression)
X = diabetes.data[:, np.newaxis, 2]  # use only the 3rd feature (BMI)
y = diabetes.target

# ==== Step 3: Split Dataset ====
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ==== Step 4: Train the Model ====
model = LinearRegression()
model.fit(X_train, y_train)

# ==== Step 5: Make Predictions ====
y_pred = model.predict(X_test)

# ==== Step 6: Evaluate Performance ====
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Formula: y = mX + c")
print("Slope (m):", model.coef_[0])
print("Intercept (c):", model.intercept_)
print("Mean Squared Error:", round(mse, 2))
print("R² Score:", round(r2, 2))

# ==== Step 7: Visualize ====
plt.scatter(X_test, y_test, color="blue", label="Actual Data")
plt.plot(X_test, y_pred, color="red", linewidth=2, label="Regression Line")
plt.title("Simple Linear Regression on Diabetes Dataset")
plt.xlabel("BMI Feature (X)")
plt.ylabel("Disease Progression (y)")
plt.legend()
plt.grid(True)
plt.show()
