# ==========================================
# McCulloch-Pitts Neural Model – Logic Gates
# ==========================================

def AND(x1, x2):
    return 1 if (x1 + x2) >= 2 else 0

def OR(x1, x2):
    return 1 if (x1 + x2) >= 1 else 0

def NOT(x):
    return 1 if x == 0 else 0

def XOR(x1, x2):
    return AND(OR(x1, x2), NOT(AND(x1, x2)))

def XNOR(x1, x2):
    return NOT(XOR(x1, x2))

# ======================
# Test using input string list
# ======================

inputs = ["00", "01", "10", "11"]

print("McCulloch-Pitts Logic Gate Simulation\n")

print("Inputs :", inputs, "\n")

print("AND Gate:")
for p in inputs:
    a, b = int(p[0]), int(p[1])
    print(f"{p} -> {AND(a, b)}")

print("\nOR Gate:")
for p in inputs:
    a, b = int(p[0]), int(p[1])
    print(f"{p} -> {OR(a, b)}")

print("\nXOR Gate:")
for p in inputs:
    a, b = int(p[0]), int(p[1])
    print(f"{p} -> {XOR(a, b)}")

print("\nXNOR Gate:")
for p in inputs:
    a, b = int(p[0]), int(p[1])
    print(f"{p} -> {XNOR(a, b)}")

print("\nNOT Gate:")
for p in ["0", "1"]:
    a = int(p)
    print(f"{p} -> {NOT(a)}")
