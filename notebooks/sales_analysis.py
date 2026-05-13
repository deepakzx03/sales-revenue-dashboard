import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs('../screenshots', exist_ok=True)

# Force comma separator
df = pd.read_csv('../data/sales_data.csv')

print(df.head())
print(df.columns)

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
avg_sales = df["Sales"].mean()

print("Total Sales:", total_sales)
print("Total Profit:", total_profit)
print("Average Sales:", avg_sales)

region_sales = df.groupby("Region")["Sales"].sum()
product_sales = df.groupby("Product")["Sales"].sum().sort_values(ascending=False)

plt.figure(figsize=(8,5))
region_sales.plot(kind="bar")
plt.title("Sales by Region")
plt.tight_layout()
plt.savefig("../screenshots/sales_by_region.png")
plt.close()

plt.figure(figsize=(8,5))
product_sales.plot(kind="bar")
plt.title("Top Product Sales")
plt.tight_layout()
plt.savefig("../screenshots/top_products.png")
plt.close()

print("Project completed successfully.")