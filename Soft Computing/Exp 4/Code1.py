# Domain Extension via Linear Interpolation
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

# Example data (triangular-like membership over [0,10])
original_domain = np.linspace(0, 10, 11)
original_membership = np.array([0, 0.2, 0.4, 0.6, 0.8, 1.0, 0.8, 0.6, 0.4, 0.2, 0.0])
A = FuzzySet(original_domain, original_membership)

# New larger domain [0,20]
new_domain = np.linspace(0, 20, 21)
extended_membership = extend_domain_via_interpolation(A, new_domain)

print("Original Membership:", A.membership)
print("Extended Membership:", extended_membership.round(3))
