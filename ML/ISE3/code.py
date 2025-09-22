# 1. Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# 2. Load Dataset
df = pd.read_csv("ML/ISE3/spam.csv", encoding="latin-1")

# 3. Keep only important columns
df = df[['v1', 'v2']]
df.columns = ['label', 'message']

# 4. Convert labels: ham=0, spam=1
df['label_num'] = df['label'].map({'ham': 0, 'spam': 1})

# 5. Feature: message length
df['msg_length'] = df['message'].apply(len)

# 6. Prepare data for regression
X = df[['msg_length']]
y = df['label_num']

# 7. Train Linear Regression model
lin_reg = LinearRegression()
lin_reg.fit(X, y)

# 8. Predictions
y_pred = lin_reg.predict(X)

# 9. Plot Regression Line
plt.figure(figsize=(8,6))
plt.scatter(df['msg_length'], y, color="gold", alpha=0.6, label="Actual Data")
plt.plot(df['msg_length'], y_pred, color="red", linewidth=2, label="Regression Line")
plt.xlabel("Message Length")
plt.ylabel("Spam (1) or Ham (0)")
plt.title("Linear Regression on Spam Dataset")
plt.legend()
plt.grid(True)
plt.show()

# 10. Print Coefficients
print("Slope (Coefficient):", lin_reg.coef_[0])
print("Intercept:", lin_reg.intercept_)
