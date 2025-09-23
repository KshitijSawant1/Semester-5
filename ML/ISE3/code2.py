# financial_lr.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

# 1) Load data
df = pd.read_csv("ML/ISE3/financial_regression.csv", parse_dates=["date"])

# 2) Keep only what we need and sort by time
df = df[["date", "gold close", "sp500 close"]].sort_values("date")

# 3) Handle missing values (forward-fill over time)
df[["gold close", "sp500 close"]] = df[["gold close", "sp500 close"]].ffill()

# 4) Features/target
X = df[["gold close"]].values  # shape (n, 1)
y = df["sp500 close"].values   # shape (n,)

# 5) Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 6) Pipeline: impute (safety) + linear regression
model = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("lr", LinearRegression())
])

# 7) Fit
model.fit(X_train, y_train)

# 8) Evaluate
y_pred = model.predict(X_test)
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print(f"R^2:  {r2:.4f}")
print(f"MAE:  {mae:.4f}")
print(f"RMSE: {rmse:.4f}")

# 9) Coefficients (from the 'lr' step inside the pipeline)
lr_step = model.named_steps["lr"]
print("Intercept:", lr_step.intercept_)
print("Coefficients:", lr_step.coef_)  # one value since we have one feature

# 10) Plot
plt.figure(figsize=(8, 6))
plt.scatter(X_test, y_test, alpha=0.5, label="Test points")
x_line = np.linspace(X_test.min(), X_test.max(), 200).reshape(-1, 1)
y_line = model.predict(x_line)
plt.plot(x_line, y_line, lw=2, color="crimson", label="Fitted line")
plt.xlabel("Gold Close")
plt.ylabel("S&P 500 Close")
plt.title("Linear Regression: S&P 500 vs Gold")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
