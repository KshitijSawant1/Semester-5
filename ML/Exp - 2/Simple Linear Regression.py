import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Sample data
data = {
    'Age': [43, 21, 25, 42, 57, 59, 55],
    'Glucose': [99, 65, 79, 75, 87, 81, 0]  # Last value can be predicted
}

df = pd.DataFrame(data)

# Separate variables
X = df[['Age']][:-1]  # Independent variable
y = df['Glucose'][:-1]  # Dependent variable

# Model
model = LinearRegression()
model.fit(X, y)

# Prediction for last Age (55)
predicted = model.predict([[55]])
print(f"Predicted Glucose Level for Age 55: {predicted[0]:.2f}")

# Visualization
plt.scatter(X, y, color='blue', label='Data')
plt.plot(X, model.predict(X), color='red', label='Regression Line')
plt.xlabel("Age")
plt.ylabel("Glucose Level")
plt.title("Simple Linear Regression")
plt.legend()
plt.grid(True)
plt.show()

# Evaluation
y_pred = model.predict(X)
print("MSE:", mean_squared_error(y, y_pred))
print("R² Score:", r2_score(y, y_pred))
