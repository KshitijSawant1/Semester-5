# pca_classifier_iris.py
# ----------------------
# Implements: PCA for dimensionality reduction + classifier (Logistic Regression)
# Dataset: seaborn.load_dataset('iris')

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# 1) Load dataset
df = sns.load_dataset('iris')  # columns: sepal_length, sepal_width, petal_length, petal_width, species

# 2) Feature/label split
X = df.drop(columns=['species']).values
y = df['species'].values

# 3) Train/test split (stratify to preserve class balance)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

# 4) Standardize features (very important for PCA)
scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s  = scaler.transform(X_test)

# 5) Fit PCA
#    Choose n_components to keep ~95% variance (here we show both ways)
pca_full = PCA().fit(X_train_s)
cum_var = np.cumsum(pca_full.explained_variance_ratio_)

# auto-pick smallest k with >=95% variance
k = np.argmax(cum_var >= 0.95) + 1

# Or set manually, e.g., k = 2
# k = 2

pca = PCA(n_components=k)
X_train_pca = pca.fit_transform(X_train_s)
X_test_pca  = pca.transform(X_test_s)

print(f"Chosen components (k): {k}")
print("Explained variance ratio per PC:", np.round(pca.explained_variance_ratio_, 4))
print("Cumulative explained variance:", np.round(np.cumsum(pca.explained_variance_ratio_), 4))

# 6) Train classifier on PCA features
clf = LogisticRegression(max_iter=1000, multi_class='auto')
clf.fit(X_train_pca, y_train)

# 7) Evaluate
y_pred = clf.predict(X_test_pca)
acc = accuracy_score(y_test, y_pred)
print("\nAccuracy:", round(acc, 4))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# 8) Visualize explained variance (scree plot)
plt.figure(figsize=(7,4))
plt.plot(range(1, len(pca_full.explained_variance_ratio_)+1),
         np.cumsum(pca_full.explained_variance_ratio_), marker='o')
plt.xlabel("Number of Components")
plt.ylabel("Cumulative Explained Variance")
plt.title("PCA Scree Plot (Cumulative Variance)")
plt.grid(True)
plt.tight_layout()
plt.show()

# 9) Optional: 2D visualization if k >= 2
if X_train_pca.shape[1] >= 2:
    # Build a small DF for plotting
    Z = np.vstack([X_train_pca[:,0], X_train_pca[:,1]]).T
    plot_df = pd.DataFrame(Z, columns=['PC1','PC2'])
    plot_df['species'] = y_train

    plt.figure(figsize=(6,5))
    sns.scatterplot(data=plot_df, x='PC1', y='PC2', hue='species', s=60, alpha=0.8)
    plt.title("Iris (Train) in PCA Space")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# 10) Component loadings (which original features contribute to each PC)
loadings = pd.DataFrame(
    pca.components_.T,
    index=df.drop(columns=['species']).columns,
    columns=[f'PC{i+1}' for i in range(k)]
)
print("\nPCA Loadings (feature contributions):\n", loadings.round(4))
