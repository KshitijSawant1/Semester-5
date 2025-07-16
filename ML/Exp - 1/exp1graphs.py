import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load the dataset
df = pd.read_csv("ML/Exp - 1/Diabetes Dataset.csv")

# Optional: Check if the data is loaded correctly
print("Dataset Shape:", df.shape)
print(df.head())

## 1. Bar Plot (Average Glucose by Outcome)
avg_values = df.groupby("Outcome")[["Glucose", "BMI", "Age"]].mean()

# Create grouped bar plot
avg_values.plot(kind='bar', figsize=(8, 5), width=0.7)

plt.title("Average Glucose, BMI, and Age by Outcome")
plt.xlabel("Outcome (0 = No Diabetes, 1 = Diabetes)")
plt.ylabel("Average Value")
plt.legend(title="Features")
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

## 2. Horizontal Bar Plot (Average Age by Outcome)
# Calculate average age by diabetes outcome
avg_age = df.groupby("Outcome")["Age"].mean()
avg_age.index = ['No Diabetes', 'Diabetes']

# Set up the plot
fig, ax = plt.subplots(figsize=(8, 4))
colors = ['#76c7c0', '#f27c7c']
bars = ax.barh(avg_age.index, avg_age.values, color=colors, edgecolor='black', height=0.5)

# Add data labels
for bar in bars:
    width = bar.get_width()
    ax.text(width + 0.8, bar.get_y() + bar.get_height()/2,
            f'{width:.1f} yrs',
            va='center', ha='left', fontsize=10, fontweight='bold')

# Title and labels
ax.set_title("Average Age by Diabetes Outcome", fontsize=14, fontweight='bold')
ax.set_xlabel("Average Age (in years)", fontsize=12)
ax.set_ylabel("Outcome", fontsize=12)

# Grid and aesthetic adjustments
ax.grid(axis='x', linestyle='--', alpha=0.5)
ax.set_axisbelow(True)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.tight_layout()
plt.show()


## 3. Histogram (BMI Distribution)
n, bins, patches = plt.hist(df["BMI"], bins=20, color='#8e44ad', edgecolor='black', alpha=0.85)

# Add titles and labels
plt.title("Distribution of BMI Among Patients", fontsize=14, fontweight='bold')
plt.xlabel("BMI (Body Mass Index)", fontsize=12)
plt.ylabel("Number of Patients", fontsize=12)

# Annotate bars with frequencies
for i in range(len(patches)):
    height = patches[i].get_height()
    if height > 0:
        plt.text(patches[i].get_x() + patches[i].get_width()/2,
                 height + 0.5,
                 f'{int(height)}',
                 ha='center', fontsize=9, rotation=0)

# Add grid and style tweaks
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.tight_layout()
plt.show()


## 4. Pie Chart (Outcome Distribution)
outcome_counts = df["Outcome"].value_counts()
plt.pie(outcome_counts, labels=["No Diabetes", "Diabetes"], autopct="%1.1f%%", startangle=90, colors=['lightblue', 'salmon'])
plt.title("Diabetes Outcome Distribution")
plt.axis("equal")
plt.show()

## 5. Scatter Plot (Glucose vs Insulin)
plt.scatter(df["Glucose"], df["Insulin"], alpha=0.6, c=df["Outcome"], cmap="coolwarm")
plt.title("Glucose vs Insulin")
plt.xlabel("Glucose")
plt.ylabel("Insulin")
plt.colorbar(label="Outcome")
plt.show()

## 6. Line Plot (Age vs Blood Pressure for First 50 Entries)
plt.plot(df["Age"][:50], df["BloodPressure"][:50], marker='o', linestyle='-', color='teal')
plt.title("Age vs Blood Pressure (First 50)")
plt.xlabel("Age")
plt.ylabel("Blood Pressure")
plt.grid(True)
plt.show()

## 7. Box Plot (BMI Distribution by Outcome)
sns.boxplot(x="Outcome", y="BMI", data=df, palette="Set2")
plt.title("BMI Distribution by Outcome")
plt.xlabel("Outcome")
plt.ylabel("BMI")
plt.show()

## 8. Stacked Bar Plot (Pregnancies Count by Outcome)
preg_outcome = df.groupby(["Pregnancies", "Outcome"]).size().unstack().fillna(0)
preg_outcome.plot(kind='bar', stacked=True, colormap='Pastel1')
plt.title("Pregnancies vs Outcome (Stacked)")
plt.xlabel("Pregnancies")
plt.ylabel("Count")
plt.legend(["No Diabetes", "Diabetes"])
plt.show()


## 9. Radar Chart (Compare Mean Features for 0 vs 1 Outcome)
# Compute mean for each class
grouped = df.groupby("Outcome").mean()
labels = grouped.columns
# Data for outcome 0 and 1
stats0 = grouped.loc[0].values
stats1 = grouped.loc[1].values

# Radar setup
angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
stats0 = np.concatenate((stats0, [stats0[0]]))
stats1 = np.concatenate((stats1, [stats1[0]]))
angles += angles[:1]
fig, ax = plt.subplots(figsize=(8, 6), subplot_kw=dict(polar=True))
ax.plot(angles, stats0, label="No Diabetes", linewidth=2)
ax.fill(angles, stats0, alpha=0.25)
ax.plot(angles, stats1, label="Diabetes", linewidth=2)
ax.fill(angles, stats1, alpha=0.25)
ax.set_thetagrids(np.degrees(angles[:-1]), labels)
plt.title("Radar Chart: Feature Comparison by Outcome")


plt.legend()
plt.show()
