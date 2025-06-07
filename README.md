# sqlite_sales_summary:
**Task Summary: Sales Analysis from Housing Dataset using SQL in Python**

1. **Loaded the `Housing.csv` file** into a Pandas DataFrame.
2. **Created an in-memory SQLite database** and inserted the dataset.
3. **Used SQL queries** to:

   * Calculate **total quantity sold** (number of houses sold).
   * Compute **total revenue** (sum of all house prices).
   * Group and analyze sales by **furnishing status** and **bedroom count**.
4. **Displayed results using `print()`** for quick inspection.
5. **Visualized the sales data** with `matplotlib` and `seaborn`:

   * Bar chart for **total quantity vs revenue**.
   * Bar chart of **revenue by furnishing status**.
   * Bar chart of **quantity sold by number of bedrooms**.
