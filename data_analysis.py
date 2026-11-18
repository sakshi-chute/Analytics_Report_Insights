
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create output directory
os.makedirs("outputs", exist_ok=True)

# Load dataset
df = pd.read_csv("sales_data.csv")

# Data cleaning
df = df.drop_duplicates()
df['Order_Date'] = pd.to_datetime(df['Order_Date'])

# Calculate profit
df['Profit'] = df['Revenue'] - df['Cost']

# Extract month
df['Month'] = df['Order_Date'].dt.strftime('%B')

# Executive summary metrics
total_revenue = df['Revenue'].sum()
total_cost = df['Cost'].sum()
total_profit = df['Profit'].sum()
total_units = df['Units_Sold'].sum()

profit_margin = (total_profit / total_revenue) * 100

print("SALES ANALYTICS REPORT")
print("----------------------------")
print("Total Revenue:", total_revenue)
print("Total Cost:", total_cost)
print("Total Profit:", total_profit)
print("Total Units Sold:", total_units)
print("Profit Margin:", round(profit_margin, 2), "%")

# Monthly sales analysis
monthly_sales = df.groupby('Month')['Revenue'].sum()
month_order = ['January', 'February', 'March']
monthly_sales = monthly_sales.reindex(month_order)

print("\nMonthly Sales:")
print(monthly_sales)

# Regional sales analysis
regional_sales = df.groupby('Region')['Revenue'].sum()

print("\nRegional Sales:")
print(regional_sales)

# Product sales analysis
product_sales = df.groupby('Product')['Revenue'].sum()

print("\nProduct Sales:")
print(product_sales)

# Best performing region
best_region = regional_sales.idxmax()

# Best selling product by revenue
best_product = product_sales.idxmax()

print("\nBest Performing Region:", best_region)
print("Best Performing Product:", best_product)

# Monthly sales chart
plt.figure(figsize=(8, 5))
monthly_sales.plot(kind='bar', title='Monthly Sales Analysis')
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("outputs/monthly_sales.png")
plt.close()

# Regional sales chart
plt.figure(figsize=(8, 5))
regional_sales.plot(kind='bar', title='Regional Sales Analysis')
plt.xlabel("Region")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("outputs/regional_sales.png")
plt.close()

# Product sales chart
plt.figure(figsize=(8, 5))
product_sales.plot(kind='bar', title='Product Sales Analysis')
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("outputs/product_sales.png")
plt.close()

# Profit analysis chart
plt.figure(figsize=(8, 5))
sns.barplot(data=df, x='Product', y='Profit',
            estimator=sum, errorbar=None)
plt.title("Product-wise Profit Analysis")
plt.xlabel("Product")
plt.ylabel("Total Profit")
plt.tight_layout()
plt.savefig("outputs/profit_analysis.png")
plt.close()

print("\nAll charts generated successfully!")
plt.show()
