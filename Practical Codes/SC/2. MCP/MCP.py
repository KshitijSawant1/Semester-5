# ==========================================
# McCulloch-Pitts Neural Model – Logic Gates
# ==========================================

def AND(x1, x2):
    return 1 if (x1 + x2) >= 2 else 0

def OR(x1, x2):
    return 1 if (x1 + x2) >= 1 else 0

def NOT(x):
    return 1 if x == 0 else 0

def NAND(x1, x2):
    return NOT(AND(x1, x2))

def NOR(x1, x2):
    return NOT(OR(x1, x2))

def XOR(x1, x2):
    return AND(OR(x1, x2), NOT(AND(x1, x2)))

def XNOR(x1, x2):
    return NOT(XOR(x1, x2))

# ======================
# Test using input string list
# ======================

print("McCulloch-Pitts Logic Gate Simulation\n")
print("Inputs :")
x = [0, 0, 1, 1]
y = [0, 1, 0, 1]
print(x)
print(y)

print("\nNOT Gate:")
for p in [0, 1]:
    print(f"{p} -> {NOT(p)}")

print("AND Gate:")
for p, q in zip(x, y):
    print(f"{p},{q} -> {AND(p, q)}")


print("\nOR Gate:")
for p, q in zip(x, y):
    print(f"{p},{q} -> {OR(p, q)}")

print("\nNAND Gate:")
for p, q in zip(x, y):
    print(f"{p},{q} -> {NAND(p, q)}")

print("\nNOR Gate:")
for p, q in zip(x, y):
    print(f"{p},{q} -> {NOR(p, q)}")

print("\nXOR Gate:")
for p, q in zip(x, y):
    print(f"{p},{q} -> {XOR(p, q)}")

print("\nXNOR Gate:")
for p, q in zip(x, y):
    print(f"{p},{q} -> {XNOR(p, q)}")

