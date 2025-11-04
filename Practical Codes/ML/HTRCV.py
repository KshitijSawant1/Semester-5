# ==== Hyperparameter Tuning using RandomizedSearchCV ====
# Formula (Conceptual):
# Best_Params = argmax ( Mean_CV_Score(random_sample(params)) )
# RandomizedSearchCV tests random combinations from parameter distributions to find near-optimal hyperparameters.

# ---- Imports ----
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score
from scipy.stats import randint

# ---- Load dataset ----
iris = datasets.load_iris()
X = iris.data
y = iris.target
df = pd.DataFrame(X, columns=iris.feature_names)
df['target'] = y
print(df.head())

# ---- Split data ----
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ---- Define model and parameter distributions ----
model = RandomForestClassifier(random_state=42)
param_dist = {
    'n_estimators': randint(50, 200),
    'max_depth': randint(2, 10),
    'min_samples_split': randint(2, 10)
}

# ---- Apply RandomizedSearchCV ----
random_search = RandomizedSearchCV(
    model, param_distributions=param_dist, 
    n_iter=10, cv=5, scoring='accuracy', random_state=42
)
random_search.fit(X_train, y_train)

# ---- Best Parameters ----
print("Best Parameters:", random_search.best_params_)

# ---- Evaluate on Test Data ----
y_pred = random_search.predict(X_test)
acc = accuracy_score(y_test, y_pred)
prec = precision_score(y_test, y_pred, average='macro')
rec = recall_score(y_test, y_pred, average='macro')

print(f"Accuracy  : {acc:.3f}")
print(f"Precision : {prec:.3f}")
print(f"Recall    : {rec:.3f}")

# ---- Simple Visualization of Random Search Results ----
results = pd.DataFrame(random_search.cv_results_)
plt.figure(figsize=(6,4))
plt.scatter(range(len(results)), results['mean_test_score'], color='teal', s=70)
plt.title('RandomizedSearchCV Mean Accuracy per Iteration')
plt.xlabel('Random Parameter Combination Index')
plt.ylabel('Mean CV Accuracy')
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()
