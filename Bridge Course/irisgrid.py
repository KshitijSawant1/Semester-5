from sklearn.datasets import load_iris
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
print("\nLoad Dataset")
data = load_iris()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target

target_counts = df['target'].value_counts().sort_index()
labels = data.target_names

# Create subplots (2 rows x 3 columns)
fig, axs = plt.subplots(2, 3, figsize=(18, 10), dpi=120)

fig.suptitle("Iris Dataset Visualizations", fontsize=16)

# ----------------------------------------
# 1. Bar Plot
axs[0, 0].bar(labels, target_counts, color='skyblue')
axs[0, 0].set_title("Bar Plot - Class Count")
axs[0, 0].set_xlabel("Species")
axs[0, 0].set_ylabel("Count")

# ----------------------------------------
# 2. Line Plot (Sepal Length for first 20 samples)
axs[0, 1].plot(df['sepal length (cm)'][:20], marker='o', color='green')
axs[0, 1].set_title("Line Plot - Sepal Length (First 20)")
axs[0, 1].set_xlabel("Sample Index")
axs[0, 1].set_ylabel("Sepal Length (cm)")

# ----------------------------------------
# 3. Pie Chart - Class Distribution
axs[0, 2].pie(target_counts, labels=labels, autopct='%1.1f%%', startangle=140,
              colors=['red', 'blue', 'green'])
axs[0, 2].set_title("Pie Chart - Class Distribution")
axs[0, 2].axis('equal')  # Equal aspect ratio for pie

# ----------------------------------------
# 4. Scatter Plot (Sepal Length vs Width)
scatter = axs[1, 0].scatter(df['sepal length (cm)'], df['sepal width (cm)'],
                            c=df['target'], cmap='viridis')
axs[1, 0].set_title("Scatter Plot - Sepal Length vs Width")
axs[1, 0].set_xlabel("Sepal Length (cm)")
axs[1, 0].set_ylabel("Sepal Width (cm)")
fig.colorbar(scatter, ax=axs[1, 0], ticks=[0, 1, 2], label='Class')

# ----------------------------------------
# 5. Histogram (Petal Length)
axs[1, 1].hist(df['petal length (cm)'], bins=20, color='orange', edgecolor='black')
axs[1, 1].set_title("Histogram - Petal Length")
axs[1, 1].set_xlabel("Petal Length (cm)")
axs[1, 1].set_ylabel("Frequency")

# ----------------------------------------
# 6. Box Plot (All Numeric Features)
axs[1, 2].boxplot([df[col] for col in data.feature_names], labels=data.feature_names)
axs[1, 2].set_title("Box Plot - All Features")
axs[1, 2].tick_params(axis='x', rotation=45)

# Adjust layout
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Resize the figure window (this works only in certain backends like TkAgg)
plt.get_current_fig_manager().resize(2560, 1600)

# Display the figure
plt.show()
