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

def mcculloch_pitts_xnor(x1, x2):
    xor_result = mcculloch_pitts_xor(x1, x2)
    xnor_output = mcculloch_pitts_not(xor_result)
    return xnor_output

# Test cases
print("XNOR(0, 0):", mcculloch_pitts_xnor(0, 0))  # Output: 1
print("XNOR(0, 1):", mcculloch_pitts_xnor(0, 1))  # Output: 0
print("XNOR(1, 0):", mcculloch_pitts_xnor(1, 0))  # Output: 0
print("XNOR(1, 1):", mcculloch_pitts_xnor(1, 1))  # Output: 1
