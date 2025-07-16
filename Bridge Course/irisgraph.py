from sklearn.datasets import load_iris
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
print("\nLoad Dataset")
data = load_iris()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target

# ----------------------------------------
# Bar Plot: Count of each class
print("\nBar Plot")
target_counts = df['target'].value_counts().sort_index()
labels = data.target_names
plt.bar(labels, target_counts, color='skyblue')
plt.title("Bar Plot - Count of Each Iris Class")
plt.xlabel("Iris Species")
plt.ylabel("Count")
plt.show()

# ----------------------------------------
# Line Plot: Sepal Length for first 20 samples
print("\nLine Plot")
plt.plot(df['sepal length (cm)'][:20], marker='o', linestyle='-', color='green')
plt.title("Line Plot - Sepal Length (First 20 Samples)")
plt.xlabel("Sample Index")
plt.ylabel("Sepal Length (cm)")
plt.show()

# ----------------------------------------
# Pie Chart: Proportion of Iris classes
print("\nPie Chart")
plt.pie(target_counts, labels=labels, autopct='%1.1f%%', startangle=140, colors=['red', 'blue', 'green'])
plt.title("Pie Chart - Iris Class Distribution")
plt.axis('equal')  # Keeps the pie circular
plt.show()

# ----------------------------------------
# Scatter Plot: Sepal Length vs Sepal Width
print("\nScatter Plot")
plt.scatter(df['sepal length (cm)'], df['sepal width (cm)'], c=df['target'], cmap='viridis')
plt.title("Scatter Plot - Sepal Length vs Sepal Width")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Sepal Width (cm)")
plt.colorbar(ticks=[0, 1, 2], label='Class')
plt.show()

# ----------------------------------------
# Histogram: Petal Length distribution
print("\nHistogram")
plt.hist(df['petal length (cm)'], bins=20, color='orange', edgecolor='black')
plt.title("Histogram - Petal Length Distribution")
plt.xlabel("Petal Length (cm)")
plt.ylabel("Frequency")
plt.show()

# ----------------------------------------
# Separate Box Plot
plt.figure(figsize=(10, 5))
plt.boxplot([df[col] for col in data.feature_names], labels=data.feature_names)
plt.title("Box Plot - All Numeric Features")
plt.xticks(rotation=45)
plt.show()