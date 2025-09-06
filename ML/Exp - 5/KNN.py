# 1. Import Required Libraries
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix

# 2. Load Dataset
df = sns.load_dataset('iris')
print(df.head())

# 3. Feature & Label Selection
X = df.drop('species', axis=1)
y = df['species']

# 4. Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 5. Feature Scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 6. KNN Classifier
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train_scaled, y_train)

# 7. Predictions
y_pred = knn.predict(X_test_scaled)

# 8. Evaluation
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# 9. Visualization with PCA (2D)
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Apply PCA to reduce to 2 dimensions
pca = PCA(n_components=2)
X_train_pca = pca.fit_transform(X_train_scaled)
X_test_pca = pca.transform(X_test_scaled)

# Re-train KNN on PCA-transformed data
knn_pca = KNeighborsClassifier(n_neighbors=3)
knn_pca.fit(X_train_pca, y_train)

# Plotting
plt.figure(figsize=(10, 6))
colors = {'setosa': 'red', 'versicolor': 'green', 'virginica': 'blue'}

for i, target in enumerate(knn.classes_):
    idx = y_test == target
    plt.scatter(
        X_test_pca[idx, 0], X_test_pca[idx, 1],
        c=colors[target], label=target, edgecolors='k', s=80
    )

plt.title("KNN Classification (After PCA)")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.legend()
plt.grid(True)
plt.show()
