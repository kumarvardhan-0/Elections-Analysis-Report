import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('raw_data.csv')

# Insight 1: Total seats won by each party
total_seats = df['Seats Won'].sum()
print(f"Total seats: {total_seats}")

# Insight 2: Party with the highest number of seats
top_party = df.loc[df['Seats Won'].idxmax()]
print(f"Party with the highest number of seats: {top_party['Party Name']} with {top_party['Seats Won']} seats")

# Insight 3: Party with the lowest number of seats
bottom_party = df.loc[df['Seats Won'].idxmin()]
print(f"Party with the lowest number of seats: {bottom_party['Party Name']} with {bottom_party['Seats Won']} seats")

# Insight 4: Top 5 parties with the highest number of seats
top_5_parties = df.nlargest(5, 'Seats Won')
print("Top 5 parties with the highest number of seats:")
print(top_5_parties[['Party Name', 'Seats Won']])

# Insight 5: Percentage of total seats won by each party
df['Percentage of Total Seats'] = (df['Seats Won'] / total_seats) * 100
print(df[['Party Name', 'Seats Won', 'Percentage of Total Seats']])

# Insight 6: Comparison of top 3 parties
top_3_parties = df.nlargest(3, 'Seats Won')
print("Top 3 parties comparison:")
print(top_3_parties[['Party Name', 'Seats Won', 'Percentage of Total Seats']])

# Insight 7: Parties winning more than 10% of total seats
parties_above_10_percent = df[df['Percentage of Total Seats'] > 10]
print("Parties winning more than 10% of total seats:")
print(parties_above_10_percent[['Party Name', 'Seats Won', 'Percentage of Total Seats']])

# Insight 8: Distribution of seats among all parties (plot)
plt.figure(figsize=(10, 6))
plt.bar(df['Party Name'], df['Seats Won'])
plt.xticks(rotation=90)
plt.xlabel('Party Name')
plt.ylabel('Seats Won')
plt.title('Distribution of Seats among All Parties')
plt.tight_layout()
plt.savefig('distribution_of_seats.png')
plt.show()

# Insight 9: Median and Mean seats won by parties
median_seats = df['Seats Won'].median()
mean_seats = df['Seats Won'].mean()
print(f"Median seats won by parties: {median_seats}")
print(f"Mean seats won by parties: {mean_seats}")

# Insight 10: Insights on small parties (less than 5 seats)
small_parties = df[df['Seats Won'] < 5]
print("Parties with less than 5 seats:")
print(small_parties[['Party Name', 'Seats Won']])

# Save the insights to a CSV file
df.to_csv('election_insights.csv', index=False)
