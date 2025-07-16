import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv("Brdige Course/deliveries.csv")  # <-- Replace with your actual path

# Show data summary
print("Head:\n", df.head())
print("\nTail:\n", df.tail())
print("\nDescribe:\n", df.describe())
print("\nMean:\n", df.mean(numeric_only=True))
print("\nMax:\n", df.max(numeric_only=True))
print("\nMin:\n", df.min(numeric_only=True))
print("\nMedian:\n", df.median(numeric_only=True))

# Create a 2x3 grid for 6 different plot types
fig, axs = plt.subplots(2, 3, figsize=(18, 10))
fig.suptitle("IPL Dataset - Visual Summary", fontsize=16)

# 1. Line Plot – Cumulative total_runs across first 50 balls
axs[0, 0].plot(df['ball'][:50], df['total_runs'][:50].cumsum(), marker='o', color='blue')
axs[0, 0].set_title("Line Plot - Cumulative Runs")
axs[0, 0].set_xlabel("Ball")
axs[0, 0].set_ylabel("Total Runs")

# 2. Scatter Plot – total_runs vs batsman_runs (first 200 balls)
axs[0, 1].scatter(df['batsman_runs'][:200], df['total_runs'][:200], alpha=0.7, color='green')
axs[0, 1].set_title("Scatter Plot - Batsman vs Total Runs")
axs[0, 1].set_xlabel("Batsman Runs")
axs[0, 1].set_ylabel("Total Runs")

# 3. Bar Plot – Average runs per over
avg_runs_per_over = df.groupby('over')['total_runs'].mean()
axs[0, 2].bar(avg_runs_per_over.index, avg_runs_per_over.values, color='orange')
axs[0, 2].set_title("Bar Plot - Avg Runs per Over")
axs[0, 2].set_xlabel("Over")
axs[0, 2].set_ylabel("Average Runs")

# 4. Pie Chart – Wicket types (first 300 deliveries only for brevity)
wicket_types = df[df['is_wicket'] == 1]['dismissal_kind'].value_counts()
axs[1, 0].pie(wicket_types.values, labels=wicket_types.index, autopct='%1.1f%%', startangle=140)
axs[1, 0].set_title("Pie Chart - Wicket Types")

# 5. Histogram – Distribution of batsman runs
axs[1, 1].hist(df['batsman_runs'], bins=10, color='purple', edgecolor='black')
axs[1, 1].set_title("Histogram - Batsman Runs")
axs[1, 1].set_xlabel("Runs")
axs[1, 1].set_ylabel("Frequency")

# 6. Box Plot – total_runs distribution by over
df_box = df[df['over'] <= 10]  # Limiting to first 10 overs for cleaner plot
box_data = [df_box[df_box['over'] == i]['total_runs'] for i in sorted(df_box['over'].unique())]
axs[1, 2].boxplot(box_data, labels=sorted(df_box['over'].unique()))
axs[1, 2].set_title("Box Plot - Total Runs per Over")
axs[1, 2].set_xlabel("Over")
axs[1, 2].set_ylabel("Total Runs")

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.get_current_fig_manager().resize(2560, 1600)
plt.show()
