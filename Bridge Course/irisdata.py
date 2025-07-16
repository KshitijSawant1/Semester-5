from sklearn.datasets import load_iris
import pandas as pd
print()
print("Load Dataset")
data = load_iris()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target
print()
print("Head of Dataset")
print(df.head(10))

print()
print("Tail of Dataset")
print(df.tail(10))

print()
print("Shape of Dataset")
print(df.shape)

print()
print("Describe of Dataset")
print(df.describe)

print()
print("iloc of Dataset")
print(df.iloc[0])
print(df.iloc[0:3,0:2])

print()
print("Max of Dataset")
print(df.max)

print()
print("Min of Dataset")
print(df.min)

print()
print("Apply function on of Dataset")
print("Before")
print(df.head(10))
def half(s):
    return s*0.5
print(df.head(10).apply(half))

print()
print("Count on Dataset")
print(df.value_counts())

print()
print("Sort on Dataset")
print(df.sort_values(by="sepal length (cm)"))
