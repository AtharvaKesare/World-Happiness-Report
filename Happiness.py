import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


match_data = pd.read_csv(r"C:/Users/Dell/Downloads/deliveries/matches.csv")


print(match_data.head(10))

print("\nMissing values in each column:")
print(match_data.isnull().sum())


print("\nUnique seasons:")
print(match_data['season'].unique())

max_runs_won = match_data['win_by_runs'].max()
print(f'Match won by the maximum margin of runs: {match_data.iloc[match_data["win_by_runs"].idxmax()]}')


print(f'Matches won by maximum number of wickets: {match_data.iloc[match_data["win_by_wickets"].idxmax()]}')


print(f'Matches won by minimum margin of runs: {match_data.iloc[match_data[match_data["win_by_runs"].ge(1)].win_by_runs.idxmin()]}')


print(f'Number of matches won by minimum wickets: {match_data.iloc[match_data[match_data["win_by_wickets"].ge(1)].win_by_wickets.idxmin()]}')


print("\nMatches where D/L method was and wasn't applied:")
print(match_data['dl_applied'].value_counts())


dl_percentage = round(match_data['dl_applied'].value_counts() / match_data['dl_applied'].count() * 100, 2)
print(f'\n% of matches with and without D/L method:\n{dl_percentage}')


plt.figure(figsize=(10, 8))
sns.set(style="whitegrid")
ax = sns.countplot(y='city', data=match_data, palette="coolwarm")
plt.title('No. of Matches Held in Each City\n', fontsize=16, fontweight='bold')
plt.xlabel('\nNo. of Matches Held', fontsize=14)
plt.ylabel('Cities\n', fontsize=14)
plt.xlim([0, 120])
for container in ax.containers:
    ax.bar_label(container, padding=5, fmt='%d', fontsize=10, color='black')
plt.tight_layout()
plt.show()


print('Number of Matches won by each team:')
print(match_data['winner'].value_counts())


data = match_data['winner'].value_counts()
plt.figure(figsize=(12, 8))
sns.set(style="whitegrid")
ax = sns.barplot(y=data.index, x=data, palette="viridis", orient='h')
plt.title('No. of Matches Won by Each Team\n', fontsize=16, fontweight='bold')
plt.xlabel("\nNo. of Matches Won", fontsize=14)
plt.ylabel('Teams\n', fontsize=14)
ax.set_xlim([0, 120])
for container in ax.containers:
    ax.bar_label(container, fmt='%d', padding=5, fontsize=12, color='black')
plt.tight_layout()
plt.show()


plt.figure(figsize=(10, 6))
sns.set(style="whitegrid")
ax = sns.countplot(x='season', data=match_data, palette="coolwarm")
plt.title('No. of Matches Held Every Season\n', fontsize=16, fontweight='bold')
plt.xlabel('\nSeason', fontsize=14)
plt.ylabel('No. of Matches Held\n', fontsize=14)
for container in ax.containers:
    ax.bar_label(container, fmt='%d', padding=3, fontsize=10, color='black')
ax.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt