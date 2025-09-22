import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

# Dataset
data = {
   'Age': [25, 45, 35, 50, 23, 36, 52],
   'BMI': [18, 25, 22, 30, 17, 24, 28],
   'Glucose': [70, 85, 78, 90, 68, 79, 88]
}
df = pd.DataFrame(data)

# Features and target
X = df[['Age', 'BMI']]
y = df['Glucose']

# Train model
model = LinearRegression()
model.fit(X, y)

# Evaluate
y_pred = model.predict(X)
print("MSE:", mean_squared_error(y, y_pred))
print("R² Score:", r2_score(y, y_pred))

# Ranges and means
age_range = np.linspace(df['Age'].min(), df['Age'].max(), 100)
bmi_range = np.linspace(df['BMI'].min(), df['BMI'].max(), 100)

bmi_mean = df['BMI'].mean()
age_mean = df['Age'].mean()

# Predictions
age_effect = model.predict(pd.DataFrame({'Age': age_range, 'BMI': [bmi_mean]*100}))
bmi_effect = model.predict(pd.DataFrame({'Age': [age_mean]*100, 'BMI': bmi_range}))

# Plot setup
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Plot 1: Age vs Glucose
axes[0].plot(age_range, age_effect, label='Predicted Glucose (BMI fixed)', color='blue')
axes[0].scatter(df['Age'], df['Glucose'], color='blue', marker='o', edgecolor='black', label='Actual Data (Age)')
axes[0].set_title("Effect of Age on Glucose")
axes[0].set_xlabel("Age")
axes[0].set_ylabel("Glucose Level")
axes[0].legend()
axes[0].grid(True)

# Plot 2: BMI vs Glucose
axes[1].plot(bmi_range, bmi_effect, label='Predicted Glucose (Age fixed)', color='green')
axes[1].scatter(df['BMI'], df['Glucose'], color='green', marker='s', edgecolor='black', label='Actual Data (BMI)')
axes[1].set_title("Effect of BMI on Glucose")
axes[1].set_xlabel("BMI")
axes[1].set_ylabel("Glucose Level")
axes[1].legend()
axes[1].grid(True)

plt.tight_layout()
plt.show()
