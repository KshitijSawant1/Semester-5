# 1. Import Required Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# 2. Load Dataset
data = load_breast_cancer()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target  # Add target column

print("Initial DataFrame:")
print(df.head())
print()
print(df.info())

# 3. EDA – Target distribution
sns.countplot(x='target', data=df)
plt.title("Distribution of Benign (1) and Malignant (0) Cases")
plt.xlabel("Target")
plt.ylabel("Count")
plt.grid(True)
plt.show()

# 4. Correlation Heatmap
plt.figure(figsize=(15, 10))
sns.heatmap(df.corr(), cmap='coolwarm', annot=False)
plt.title("Correlation Heatmap of Features")
plt.show()

# 5. Feature Selection
X = df[['mean radius', 'mean texture', 'mean perimeter', 'mean area', 'mean smoothness']]
y = df['target']

# 6. Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 7. Train Logistic Regression Model
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# 8. Evaluate the Model
y_pred = model.predict(X_test)

print("\nEvaluation Report:")
print("Accuracy:", round(accuracy_score(y_test, y_pred), 2))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# 9. Plot Logistic Regression Curve (only for 1 feature for 2D plotting)
X_radius = df[['mean radius']]
y_target = df['target']

model_radius = LogisticRegression()
model_radius.fit(X_radius, y_target)

# Create range and predict probabilities
radius_range = np.linspace(X_radius.min(), X_radius.max(), 300).reshape(-1, 1)
probabilities = model_radius.predict_proba(radius_range)[:, 1]

# 10. Plot the Curve
plt.figure(figsize=(10, 6))
sns.scatterplot(x='mean radius', y='target', data=df, alpha=0.4, label='Actual')
plt.plot(radius_range, probabilities, color='red', label='Logistic Regression Curve')
plt.xlabel("Mean Radius")
plt.ylabel("Probability of Being Benign")
plt.title("Logistic Regression Curve – Cancer Prediction by Radius")
plt.legend()
plt.grid(True)
plt.show()
