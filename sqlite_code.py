import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the dataset
df = pd.read_csv("Housing.csv")  # Change path if needed

# Step 2: Set up SQLite in-memory DB
conn = sqlite3.connect(":memory:")
df.to_sql("housing_data", conn, index=False, if_exists="replace")

# Step 3: Basic Sales Summary
summary_query = """
SELECT 
    COUNT(*) AS total_quantity_sold,
    SUM(price) AS total_revenue
FROM housing_data
"""
summary_df = pd.read_sql_query(summary_query, conn)

# Step 4: Group by Furnishing Status
furnish_query = """
SELECT 
    [furnishing status] AS furnishing_status,
    COUNT(*) AS quantity_sold,
    SUM(price) AS revenue
FROM housing_data
GROUP BY [furnishing status]
"""
furnish_df = pd.read_sql_query(furnish_query, conn)

# Step 5: Group by Bedrooms
bedroom_query = """
SELECT 
    bedrooms,
    COUNT(*) AS quantity_sold,
    SUM(price) AS revenue
FROM housing_data
GROUP BY bedrooms
ORDER BY bedrooms
"""
bedroom_df = pd.read_sql_query(bedroom_query, conn)

conn.close()

# Step 6: Print Basic Summary
total_quantity = summary_df.loc[0, 'total_quantity_sold']
total_revenue = summary_df.loc[0, 'total_revenue']

print(f"Total Quantity Sold: {total_quantity}")
print(f"Total Revenue: ₹{total_revenue:,.2f}")

# Step 7: Set Plot Style
sns.set(style="whitegrid")

# Step 8: Plot 1 - Total Sales Summary
plt.figure(figsize=(6, 4))
plt.bar(['Total Quantity Sold', 'Total Revenue (₹)'], [total_quantity, total_revenue], color=['skyblue', 'salmon'])
plt.title("Overall Sales Summary")
plt.ylabel("Values")
plt.tight_layout()
plt.show()

# Step 9: Plot 2 - Revenue by Furnishing Status
plt.figure(figsize=(6, 4))
sns.barplot(data=furnish_df, x='furnishing_status', y='revenue', palette='Set2')
plt.title("Total Revenue by Furnishing Status")
plt.ylabel("Revenue (₹)")
plt.xlabel("Furnishing Status")
for index, row in furnish_df.iterrows():
    plt.text(index, row['revenue'], f"₹{int(row['revenue']):,}", ha='center', va='bottom')
plt.tight_layout()
plt.show()

# Step 10: Plot 3 - Quantity Sold by Number of Bedrooms
plt.figure(figsize=(6, 4))
sns.barplot(data=bedroom_df, x='bedrooms', y='quantity_sold', palette='coolwarm')
plt.title("Quantity Sold by Number of Bedrooms")
plt.x
