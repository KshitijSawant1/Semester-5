def mcculloch_pitts_or(x1, x2):
    # Define weights and threshold
    weight1 = 1
    weight2 = 1
    threshold = 1  # Lower threshold because OR activates if either input is 1

    # Compute weighted sum
    weighted_sum = x1 * weight1 + x2 * weight2

    # Apply threshold logic
    output = 1 if weighted_sum >= threshold else 0

    return output

# Test cases
print("OR(0, 0):", mcculloch_pitts_or(0, 0))  # Output: 0
print("OR(0, 1):", mcculloch_pitts_or(0, 1))  # Output: 1
print("OR(1, 0):", mcculloch_pitts_or(1, 0))  # Output: 1
print("OR(1, 1):", mcculloch_pitts_or(1, 1))  # Output: 1
