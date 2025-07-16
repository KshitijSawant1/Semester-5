import pandas as pd

# Step 1: Load the dataset
df = pd.read_csv("ML/Exp - 1/Diabetes Dataset.csv")  # Replace with your actual file path

# Step 2: Display basic information
print("Dataset Shape:", df.shape)

print("\nBasic Info:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

# Step 3: First and Last Rows
print("\nHead (First 5 rows):")
print(df.head())

print("\nTail (Last 5 rows):")
print(df.tail())

# Step 4: Basic Statistical Operations
print("\nMinimum Values:")
print(df.min(numeric_only=True))

print("\nMaximum Values:")
print(df.max(numeric_only=True))

print("\nCount of Non-Null Entries:")
print(df.count())

print("\nMedian Values:")
print(df.median(numeric_only=True))

print("\nVariance:")
print(df.var(numeric_only=True))

print("\nUnique Value Counts:")
print(df.nunique())
