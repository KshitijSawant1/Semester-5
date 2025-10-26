import numpy as np

# Function to train using Hebb's rule
def hebb_train(patterns):
    n_features = patterns.shape[1]
    W = np.zeros((n_features, n_features))

    for p in patterns:
        p = p.reshape(-1, 1)              # Column vector
        W += np.dot(p, p.T)               # Outer product
    np.fill_diagonal(W, 0)                # No self-connections
    return W / patterns.shape[0]          # Optional normalization

# Function to recall a pattern
def hebb_recall(W, pattern):
    out = np.dot(pattern, W)
    return np.where(out >= 0, 1, -1)      # Sign function

# Example patterns (binary: 1 or -1)
patterns = np.array([
    [1, -1,  1, -1],
    [1,  1, -1, -1],
])

# Train weights
W = hebb_train(patterns)
print("Weight matrix:\n", W)

# Test recall
test_pattern = np.array([1, -1, 1, -1])   # Same as first pattern
recalled = hebb_recall(W, test_pattern)
print("Input pattern:   ", test_pattern)
print("Recalled pattern:", recalled)
