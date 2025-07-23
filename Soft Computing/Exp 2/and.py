def mcculloch_pitts_and(x1, x2):
    # Define weights and threshold
    weight1 = 1
    weight2 = 1
    threshold = 2

    # Compute weighted sum
    weighted_sum = x1 * weight1 + x2 * weight2

    # Apply threshold function (activation)
    output = 1 if weighted_sum >= threshold else 0

    return output

# Test cases
print("AND(0, 0):", mcculloch_pitts_and(0, 0))  # Output: 0
print("AND(0, 1):", mcculloch_pitts_and(0, 1))  # Output: 0
print("AND(1, 0):", mcculloch_pitts_and(1, 0))  # Output: 0
print("AND(1, 1):", mcculloch_pitts_and(1, 1))  # Output: 1
