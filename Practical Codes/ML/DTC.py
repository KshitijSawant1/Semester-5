# ==== Decision Tree Classifier ====
# Formula (conceptual):
# The tree splits data using features that maximize Information Gain:
# IG = Entropy(parent) - [Σ ( (n_child / n_total) * Entropy(child) )]

# ---- Imports ----

import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, precision_score, recall_score

# ---- Load dataset ----
iris = datasets.load_iris()
X = iris.data
y = iris.target
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = iris.target

# Display first 5 rows
print(df.head())
# ---- Split data ----
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ---- Train Decision Tree ----
clf = DecisionTreeClassifier(criterion='entropy', random_state=42)
clf.fit(X_train, y_train)

# ---- Predict ----
y_pred = clf.predict(X_test)

# ---- Evaluate ----
acc = accuracy_score(y_test, y_pred)
prec = precision_score(y_test, y_pred, average='macro')
rec = recall_score(y_test, y_pred, average='macro')

print(f"Accuracy  : {acc:.3f}")
print(f"Precision : {prec:.3f}")
print(f"Recall    : {rec:.3f}")

# ---- Visualize Tree ----
plt.figure(figsize=(8,6))
plot_tree(clf, feature_names=iris.feature_names, class_names=iris.target_names, filled=True)
plt.title("Decision Tree for Iris Dataset")
plt.show()
