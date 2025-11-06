import numpy as np

# Hebbian Learning
def hebb_train(X):
    W = X.T @ X
    np.fill_diagonal(W, 0)
    return W / len(X)

def hebb_recall(W, x):
    return np.where(x @ W >= 0, 1, -1)

# Patterns (1 and -1)
X = np.array([[1, -1, 1, -1],
              [1,  1,-1, -1]])

W = hebb_train(X)
print("Weight Matrix:\n", W)

test = np.array([1, -1, 1, -1])
print("Input:   ", test)
print("Recalled:", hebb_recall(W, test))
