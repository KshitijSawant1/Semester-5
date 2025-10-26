import numpy as np

class FuzzySet:
    def __init__(self, domain: np.ndarray, membership: np.ndarray):
        assert domain.ndim == 1 and membership.ndim == 1
        assert len(domain) == len(membership)
        assert np.all(np.diff(domain) >= 0), "Domain must be sorted."
        self.domain = domain
        self.membership = membership

def extend_domain_via_interpolation(original_set: FuzzySet, new_domain: np.ndarray) -> np.ndarray:
    """Extend membership from original_set.domain to new_domain using linear interpolation."""
    return np.interp(new_domain, original_set.domain, original_set.membership)

# Define the original fuzzy set (bell-shaped)
original_domain = np.linspace(0, 5, 11)
original_membership = np.array([0.0, 0.1, 0.4, 0.7, 0.9, 1.0, 0.9, 0.7, 0.4, 0.1, 0.0])
original_set = FuzzySet(original_domain, original_membership)

# New domain [0, 10]
new_domain = np.linspace(0, 10, 21)
extended_membership = extend_domain_via_interpolation(original_set, new_domain)

print("Original Membership:", original_set.membership)
print("Extended Membership:", extended_membership.round(3))


def fuzzy_image_via_extension(A: FuzzySet, f, y_grid: np.ndarray, bin_width: float = 0.25) -> np.ndarray:
    """
    Compute μ_B(y) = sup_{x: f(x)=y} μ_A(x) via discretization/bucketing.
    For numerical stability, assign x->y = f(x) and take max μ_A over x whose f(x) falls in the bin around y.
    """
    x = A.domain
    mu_x = A.membership
    y_vals = f(x)

    mu_y = np.zeros_like(y_grid, dtype=float)
    half = bin_width / 2.0

    for k, y0 in enumerate(y_grid):
        mask = (y_vals >= y0 - half) & (y_vals <= y0 + half)
        if np.any(mask):
            mu_y[k] = np.max(mu_x[mask])
        else:
            mu_y[k] = 0.0
    return mu_y

# Define f(x) = x^2 and output grid
f = lambda t: t**2
y_grid = np.linspace(0, 100, 201)  # dense output grid
mu_B = fuzzy_image_via_extension(original_set, f, y_grid, bin_width=0.5)

print("\nSample (y, μ_B(y)) pairs:")
for yi, mui in zip(y_grid[::40], mu_B[::40]):
    print(f"{yi:.1f} -> {mui:.3f}")
