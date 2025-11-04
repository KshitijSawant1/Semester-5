# ==== Hyperparameter Tuning using GridSearchCV ====
# Formula (Conceptual):
# Best_Params = argmax ( Mean_CV_Score(params) )
# GridSearchCV tests all parameter combinations and selects the one with highest cross-validation score.

# ---- Imports ----
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score, recall_score

# ---- Load dataset ----
iris = load_iris()
X = iris.data
y = iris.target

# ---- Split data ----
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ---- Define model and parameter grid ----
model = SVC()
param_grid = {
    'C': [0.1, 1, 10],
    'kernel': ['linear', 'rbf'],
    'gamma': ['scale', 0.1, 1]
}

# ---- Apply GridSearchCV ----
grid = GridSearchCV(model, param_grid, cv=5, scoring='accuracy')
grid.fit(X_train, y_train)

# ---- Best Parameters ----
print("Best Parameters:", grid.best_params_)

# ---- Evaluate on Test Data ----
y_pred = grid.predict(X_test)
acc = accuracy_score(y_test, y_pred)
prec = precision_score(y_test, y_pred, average='macro')
rec = recall_score(y_test, y_pred, average='macro')

print(f"Accuracy  : {acc:.3f}")
print(f"Precision : {prec:.3f}")
print(f"Recall    : {rec:.3f}")
