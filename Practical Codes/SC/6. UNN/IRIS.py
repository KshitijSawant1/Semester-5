import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error

# Data
X = load_iris().data.astype(np.float32)
X = StandardScaler().fit_transform(X)
X_train, X_test = train_test_split(X, test_size=0.2, random_state=42)

# Autoencoder: 4 -> 8 -> 2 -> 8 -> 4
ae = MLPRegressor(hidden_layer_sizes=(8, 2, 8),
                  activation='relu', solver='adam',
                  max_iter=800, random_state=42)
ae.fit(X_train, X_train)

# Reconstructions + MSE
X_recon = ae.predict(X_test)
print("Test MSE:", round(mean_squared_error(X_test, X_recon), 4))

# Show a few samples
for i in range(3):
    print(f"\nSample {i}:")
    print("Original:     ", np.round(X_test[i], 3))
    print("Reconstructed:", np.round(X_recon[i], 3))
