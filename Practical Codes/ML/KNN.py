# ==== K-Nearest Neighbors (KNN) ====
# Formula:
# Distance(x, xi) = √Σ (xj - xij)²   →  Euclidean distance
# Class(x) = majority class among K nearest neighbors

# ---- Imports ----
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score

# ---- Load dataset ----
iris = datasets.load_iris()
X = iris.data
y = iris.target

# ---- Split data ----
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ---- Train KNN Model ----
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

# ---- Predict ----
y_pred = knn.predict(X_test)

# ---- Evaluate ----
acc = accuracy_score(y_test, y_pred)
prec = precision_score(y_test, y_pred, average='macro')
rec = recall_score(y_test, y_pred, average='macro')

print(f"Accuracy  : {acc:.3f}")
print(f"Precision : {prec:.3f}")
print(f"Recall    : {rec:.3f}")
