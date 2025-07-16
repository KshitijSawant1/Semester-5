import pandas as pd

# ----------------------------------------
print("\n Importing Pandas and Creating a Basic Series")
s1 = pd.Series([1, 2, 3, 4, 5])
print(s1)

# ----------------------------------------
print("\n Changing Index")
s1 = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
print(s1)

# ----------------------------------------
print("\n Creating Series from Dictionary")
s1 = pd.Series({'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50})
print(s1)

# ----------------------------------------
print("\n Extracting Element Using Positive Indexing")
s1 = pd.Series([1, 2, 3, 4, 5])
print("Element at index 3:", s1[3])

# ----------------------------------------
print("\n Extracting Element Using Negative Indexing")
s1 = pd.Series([1, 2, 3, 4, 5])
print("Element at index -3:", s1.iloc[-3])  # Correct way to use negative index


# ----------------------------------------
print("\n Extracting a Slice of the Series")
s1 = pd.Series([1, 2, 3, 4, 5])
print("Last 3 elements:\n", s1[-3:])

# ----------------------------------------
print("\n Arithmetic Operation: Add 5 to each element")
s1 = pd.Series([1, 2, 3, 4, 5])
print(s1 + 5)

# ----------------------------------------
print("\n Arithmetic Operation: Adding Two Series")
s1 = pd.Series([1, 2, 3, 4, 5])
s2 = pd.Series([1, 2, 3, 4, 5])
print(s1 + s2)

# ----------------------------------------
print("\n Creating a DataFrame")
df = pd.DataFrame({
    'Name': ['A', 'B', 'C'],
    'Marks': [10, 20, 30]
})
print(df)
