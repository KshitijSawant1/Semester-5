# 1. Import Required Libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# 2. Load Dataset
df = sns.load_dataset('titanic')  # For CSV, use: pd.read_csv('titanic.csv')
print("Initial Shape:", df.shape)

# 3. Data Cleaning
df.drop(columns=['deck', 'embark_town', 'alive', 'class', 'who', 'adult_male'], inplace=True)
df.dropna(subset=['embarked', 'age'], inplace=True)

# Convert categorical to numerical
df['sex'] = df['sex'].map({'male': 0, 'female': 1})
df['embarked'] = df['embarked'].map({'S': 0, 'C': 1, 'Q': 2})
df['alone'] = df['alone'].astype(int)

# 4. Preview Cleaned Data
print("\nCleaned DataFrame Head:")
print(df.head())

# 5. EDA - Exploratory Data Analysis
plt.figure(figsize=(12, 6))
sns.countplot(x='survived', hue='sex', data=df)
plt.title("Survival Count by Gender")
plt.xlabel("Survived")
plt.ylabel("Count")
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()

# 6. Feature Selection
features = ['pclass', 'sex', 'age', 'sibsp', 'parch', 'fare', 'embarked', 'alone']
X = df[features]
y = df['survived']

# 7. Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 8. Logistic Regression Model
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# 9. Evaluation
y_pred = model.predict(X_test)
print("\n📈 Evaluation Report:")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# 10. Logistic Regression Curve (Age vs Survival)
# Use 'age' only for this simple visualization
age_df = df[['age', 'survived']].dropna()
X_age = age_df['age'].values.reshape(-1, 1)
y_age = age_df['survived'].values

# Fit model on 'age' only
model_age = LogisticRegression()
model_age.fit(X_age, y_age)

# Predict probabilities across age range
age_range = np.linspace(X_age.min(), X_age.max(), 300).reshape(-1, 1)
predicted_prob = model_age.predict_proba(age_range)[:, 1]

# Plot Logistic Curve
plt.figure(figsize=(10, 6))
sns.scatterplot(x='age', y='survived', data=age_df, alpha=0.4, label='Actual Data')
plt.plot(age_range, predicted_prob, color='red', linewidth=2, label='Logistic Regression Curve')
plt.xlabel("Age")
plt.ylabel("Survival Probability")
plt.title("Logistic Regression Curve: Survival vs Age")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
