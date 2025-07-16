import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset (replace with your actual path)
df = pd.read_csv("Brdige Course/matches.csv")

# === Basic Dataset Summary ===
# === Basic Dataset Summary ===
print("Head:\n", df.head())
print("\nTail:\n", df.tail())

# Describe only numeric columns manually (alternative to numeric_only=True)
numeric_df = df.select_dtypes(include='number')

print("\nDescribe:\n", numeric_df.describe())
print("\nMean:\n", numeric_df.mean())
print("\nMax:\n", numeric_df.max())
print("\nMin:\n", numeric_df.min())
print("\nMedian:\n", numeric_df.median())


# === Grid Visualizations ===
fig, axs = plt.subplots(2, 3, figsize=(18, 10))
fig.suptitle("IPL Match Dataset - Visual Summary", fontsize=16)

# 1. Line Plot – Target Runs by Match ID
axs[0, 0].plot(df['id'][:50], df['target_runs'][:50], color='blue', marker='o')
axs[0, 0].set_title("Line Plot - Target Runs (First 50 Matches)")
axs[0, 0].set_xlabel("Match ID")
axs[0, 0].set_ylabel("Target Runs")

# 2. Scatter Plot – Target Runs vs Result Margin
axs[0, 1].scatter(df['target_runs'], df['result_margin'], alpha=0.7, color='green')
axs[0, 1].set_title("Scatter Plot - Target Runs vs Result Margin")
axs[0, 1].set_xlabel("Target Runs")
axs[0, 1].set_ylabel("Result Margin")

# 3. Bar Plot – Match Count per Season
season_counts = df['season'].value_counts().sort_index()
axs[0, 2].bar(season_counts.index.astype(str), season_counts.values, color='orange')
axs[0, 2].set_title("Bar Plot - Matches per Season")
axs[0, 2].set_xlabel("Season")
axs[0, 2].set_ylabel("Match Count")
axs[0, 2].tick_params(axis='x', rotation=45)

# 4. Pie Chart – Toss Decision Distribution
toss_decision_counts = df['toss_decision'].value_counts()
axs[1, 0].pie(toss_decision_counts.values, labels=toss_decision_counts.index, autopct='%1.1f%%', startangle=90)
axs[1, 0].set_title("Pie Chart - Toss Decision")
axs[1, 0].axis('equal')

# 5. Histogram – Target Runs Distribution
axs[1, 1].hist(df['target_runs'].dropna(), bins=15, color='purple', edgecolor='black')
axs[1, 1].set_title("Histogram - Target Runs")
axs[1, 1].set_xlabel("Target Runs")
axs[1, 1].set_ylabel("Frequency")

# 6. Box Plot – Result Margin by Match Type
match_types = df['match_type'].dropna().unique()
box_data = [df[df['match_type'] == t]['result_margin'].dropna() for t in match_types]
axs[1, 2].boxplot(box_data, labels=match_types)
axs[1, 2].set_title("Box Plot - Result Margin by Match Type")
axs[1, 2].tick_params(axis='x', rotation=45)
axs[1, 2].set_ylabel("Result Margin")

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()

# === Top 10 Players with Most Player of the Match Awards ===
top_players = df['player_of_match'].value_counts().head(10)
print("\nTop 10 Players with Most 'Player of the Match' Awards:")
print(top_players)

# Plot Top Players
plt.figure(figsize=(10, 6))
top_players.sort_values().plot(kind='barh', color='teal')
plt.title("Top 10 'Player of the Match' Award Winners")
plt.xlabel("Number of Awards")
plt.ylabel("Player Name")
plt.grid(axis='x')
plt.tight_layout()
plt.show()

# === Result Column Frequency ===
print("\nFrequency of values in 'result' column:")
print(df['result'].value_counts())

# === Records Where Team Won Batting First ===
batting_first_wins = df[df['winner'] == df['team1']]
print("\nMatches won by team batting first:", batting_first_wins.shape[0])
print(batting_first_wins[['team1', 'team2', 'winner', 'result', 'result_margin']].head())

# Plot: Teams that won while batting first
bat_first_counts = batting_first_wins['winner'].value_counts()
plt.figure(figsize=(10, 6))
bat_first_counts.plot(kind='bar', color='purple')
plt.title("Matches Won Batting First (Team1)")
plt.xlabel("Team")
plt.ylabel("Wins")
plt.grid(axis='y')
plt.tight_layout()
plt.show()
