# Experiment No. 3
# Aim: To implement fuzzy operations and relations (Union, Intersection, Complement, Algebraic Product, Algebraic Sum)

# Define fuzzy sets A and B with 8 elements
A = {"a": 0.1, "b": 0.3, "c": 0.5, "d": 0.8, "e": 0.6, "f": 0.4, "g": 0.2, "h": 0.9}
B = {"a": 0.7, "b": 0.4, "c": 0.6, "d": 0.2, "e": 0.5, "f": 0.8, "g": 0.1, "h": 0.3}

print()
print("Fuzzy Set A:", A)
print("Fuzzy Set B:", B)
print()

# -------------------- Union --------------------
union = {}
for key in A:
    union[key] = max(A[key], B[key])
print("Fuzzy Set Union (A ∪ B):", union)
print()

# -------------------- Intersection --------------------
intersection = {}
for key in A:
    intersection[key] = min(A[key], B[key])
print("Fuzzy Set Intersection (A ∩ B):", intersection)
print()

# -------------------- Complement --------------------
complement_A = {}
for key in A:
    complement_A[key] = 1 - A[key]
print("Fuzzy Set Complement (¬A):", complement_A)
print()

# -------------------- Algebraic Product --------------------
algebraic_product = {}
for key in A:
    algebraic_product[key] = round(A[key] * B[key], 4)
print("Fuzzy Set Algebraic Product (A · B):", algebraic_product)
print()

# -------------------- Algebraic Sum --------------------
algebraic_sum = {}
for key in A:
    a_val = A[key]
    b_val = B[key]
    algebraic_sum[key] = round(a_val + b_val - (a_val * b_val), 4)
print("Fuzzy Set Algebraic Sum (A + B):", algebraic_sum)
print()
