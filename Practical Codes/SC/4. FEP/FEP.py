import numpy as np

# Original fuzzy set
x = np.linspace(0, 5, 11)
mu_x = np.array([0.0, 0.1, 0.4, 0.7, 0.9, 1.0, 0.9, 0.7, 0.4, 0.1, 0.0])

# Extend domain [0,10] using linear interpolation
new_x = np.linspace(0, 10, 21)
mu_new = np.interp(new_x, x, mu_x)
print("Original μA(x):", mu_x)
print("Extended μA(x):", np.round(mu_new, 3))

# Fuzzy extension principle for f(x) = x²
def fuzzy_extension(x, mu, f, y_grid, bin_w=0.5):
    y = f(x)
    mu_y = np.zeros_like(y_grid)
    for i, y0 in enumerate(y_grid):
        mask = (y >= y0 - bin_w/2) & (y <= y0 + bin_w/2)
        mu_y[i] = np.max(mu[mask]) if np.any(mask) else 0
    return mu_y

f = lambda t: t**2
y_grid = np.linspace(0, 100, 201)
mu_B = fuzzy_extension(x, mu_x, f, y_grid)

print("\nSample (y, μB(y)) values:")
for yv, mv in zip(y_grid[::40], mu_B[::40]):
    print(f"{yv:.1f} -> {mv:.3f}")
