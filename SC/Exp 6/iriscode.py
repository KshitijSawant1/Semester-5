# Import Library 
import numpy as np
import tensorflow as tf
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


# 1) Reproducibility
np.random.seed(42)
tf.random.set_seed(42)
# Fixes the random seeds so that results are repeatable each time you run the code.
# Controls random initialization of weights and train/test split.

# 2) Load & prepare data (only features; labels unused for autoencoder)
iris = load_iris()
X = iris.data.astype(np.float32)          # shape: (150, 4)

# Standardize features (mean=0, std=1)
scaler = StandardScaler()
X_std = scaler.fit_transform(X).astype(np.float32)
# Why standardize? Neural nets converge faster when inputs are scaled so no feature dominates the others.
# fit_transform learns scaling parameters from data and applies it.

# Train / test split
X_train, X_test = train_test_split(X_std, test_size=0.2, random_state=42)
# Train/Test split → 80% training, 20% testing.

input_dim = X_train.shape[1]  # 4
encoding_dim = 2              # latent size
# input_dim = number of features in input = 4.
# encoding_dim = size of bottleneck latent space; we choose 2 so we can visualize it later.

# 3) Build encoder
encoder = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(input_dim,)),
    tf.keras.layers.Dense(8, activation="relu"),
    tf.keras.layers.Dense(encoding_dim, activation="linear", name="z")  # 2-D code
])
# Input Layer: Accepts vectors of length 4.
# Dense(8, relu): Expands features into 8 hidden neurons with ReLU activation.
# Dense(2, linear): Compresses into a 2D latent representation (z).
# Activation = linear here because we don’t want to squash values — let network decide range.

# 4) Build decoder
decoder = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(encoding_dim,)),
    tf.keras.layers.Dense(8, activation="relu"),
    tf.keras.layers.Dense(input_dim, activation="linear")               # reconstruct 4-D input
])
# Input Layer: Takes the 2-D latent vector.
# Dense(8, relu): Expands back to 8 neurons.
# Dense(4, linear): Outputs 4 values — the reconstruction of the original standardized features.

# 5) Full autoencoder = encoder ∘ decoder
inputs = tf.keras.Input(shape=(input_dim,))
z = encoder(inputs)
recon = decoder(z)
autoencoder = tf.keras.Model(inputs, recon, name="iris_autoencoder")
# Creates a functional API model: autoencoder(x) = decoder(encoder(x)).
# inputs → pass to encoder → get latent z → pass to decoder → get reconstruction.


autoencoder.compile(optimizer=tf.keras.optimizers.Adam(1e-3),
                    loss="mse")  # mean squared reconstruction error
# Optimizer: Adam with learning rate 0.001.
# Loss: Mean Squared Error (MSE) between original and reconstructed vectors.

# 6) Train
history = autoencoder.fit(
    X_train, X_train,
    validation_data=(X_test, X_test),
    epochs=100,
    batch_size=32,
    verbose=0
)
# Inputs = Targets: Autoencoders learn to reconstruct their own input.
# Validation Data: Checks reconstruction performance on unseen test set each epoch.
# epochs=100: Number of passes over training data.
# batch_size=32: Number of samples per gradient update.

# 7) Evaluate reconstruction error
test_mse = autoencoder.evaluate(X_test, X_test, verbose=0)
print(f"Test reconstruction MSE: {test_mse:.4f}")
# Measures how close reconstructions are to inputs on the test set.
# Lower MSE means better reconstruction.

# 8) Get latent codes and a few reconstructions
Z_test = encoder.predict(X_test)
X_recon = autoencoder.predict(X_test)
# Z_test → 2-D latent representation for each test sample.
# X_recon → reconstructed version of each test sample.

# Optional: quick look at original vs. reconstructed (first 5 rows)
for i in range(5):
    print(f"\nSample {i}:")
    print(" original (std):     ", X_test[i])
    print(" reconstructed (std):", X_recon[i])
    print(" per-feature error:  ", np.round((X_test[i]-X_recon[i])**2, 4))
