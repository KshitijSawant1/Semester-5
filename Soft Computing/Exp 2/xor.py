def mcculloch_pitts_and(x1, x2):
    return 1 if (x1 + x2) >= 2 else 0

def mcculloch_pitts_or(x1, x2):
    return 1 if (x1 + x2) >= 1 else 0

def mcculloch_pitts_not(x):
    return 1 if x == 0 else 0

def mcculloch_pitts_xor(x1, x2):
    or_result = mcculloch_pitts_or(x1, x2)
    and_result = mcculloch_pitts_and(x1, x2)
    not_and = mcculloch_pitts_not(and_result)
    xor_output = mcculloch_pitts_and(or_result, not_and)
    return xor_output

# Test cases
print("XOR(0, 0):", mcculloch_pitts_xor(0, 0))  # Output: 0
print("XOR(0, 1):", mcculloch_pitts_xor(0, 1))  # Output: 1
print("XOR(1, 0):", mcculloch_pitts_xor(1, 0))  # Output: 1
print("XOR(1, 1):", mcculloch_pitts_xor(1, 1))  # Output: 0
