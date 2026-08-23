"""
Day 18 - Pandas Data Analysis & GroupBy
Business Analytics Python Log Playbook

Pandas GroupBy and aggregation functions help transform
raw business data into meaningful insights and KPIs.

Today's focus:
- GroupBy
- Aggregation
- Sorting
- Ranking
- KPIs
- Regional analysis
- Product analysis
"""

import pandas as pd


# --------------------------------------------------
# 1. Create Business Dataset
# --------------------------------------------------

data = {
    "Customer_ID": [
        "C101", "C102", "C103", "C104", "C105",
        "C106", "C107", "C108", "C109", "C110"
    ],

    "Region": [
        "North", "South", "West", "North", "South",
        "West", "East", "North", "South", "West"
    ],

    "Product": [
        "Laptop", "Phone", "Laptop", "Tablet", "Phone",
        "Laptop", "Tablet", "Phone", "Laptop", "Tablet"
    ],

    "Salesperson": [
        "Aarav", "Meera", "Rohan", "Ananya", "Aarav",
        "Meera", "Rohan", "Ananya", "Aarav", "Meera"
    ],

    "Units_Sold": [
        12, 25, 8, 18, 30,
        10, 22, 28, 15, 20
    ],

    "Revenue": [
        900000, 1125000, 600000, 540000, 1350000,
        750000, 660000, 1260000, 1125000, 600000
    ],

    "Expenses": [
        720000, 900000, 480000, 400000, 1050000,
        600000, 500000, 980000, 850000, 450000
    ]
}

df = pd.DataFrame(data)

print("--- Business Dataset ---")
print(df)


# --------------------------------------------------
# 2. Basic Dataset Information
# --------------------------------------------------

print("\n--- Dataset Information ---")

print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\nColumn Names:")
print(df.columns.tolist())


# --------------------------------------------------
# 3. Create Profit Column
# --------------------------------------------------

df["Profit"] = df["Revenue"] - df["Expenses"]

print("\n--- Profit Added ---")
print(df)


# --------------------------------------------------
# 4. Create Profit Margin
# --------------------------------------------------

df["Profit_Margin"] = (
    df["Profit"] / df["Revenue"]
) * 100

print("\n--- Profit Margin ---")
print(df)


# --------------------------------------------------
# 5. Total Revenue
# --------------------------------------------------

total_revenue = df["Revenue"].sum()

print("\nTotal Revenue:", total_revenue)


# --------------------------------------------------
# 6. Total Expenses
# --------------------------------------------------

total_expenses = df["Expenses"].sum()

print("Total Expenses:", total_expenses)


# --------------------------------------------------
# 7. Total Profit
# --------------------------------------------------

total_profit = df["Profit"].sum()

print("Total Profit:", total_profit)


# --------------------------------------------------
# 8. Average Revenue
# --------------------------------------------------

average_revenue = df["Revenue"].mean()

print("Average Revenue:", average_revenue)


# --------------------------------------------------
# 9. Total Units Sold
# --------------------------------------------------

total_units = df["Units_Sold"].sum()

print("Total Units Sold:", total_units)


# --------------------------------------------------
# 10. Revenue by Region
# --------------------------------------------------

region_revenue = df.groupby(
    "Region"
)["Revenue"].sum()

print("\n--- Revenue by Region ---")
print(region_revenue)


# --------------------------------------------------
# 11. Profit by Region
# --------------------------------------------------

region_profit = df.groupby(
    "Region"
)["Profit"].sum()

print("\n--- Profit by Region ---")
print(region_profit)


# --------------------------------------------------
# 12. Units Sold by Region
# --------------------------------------------------

region_units = df.groupby(
    "Region"
)["Units_Sold"].sum()

print("\n--- Units Sold by Region ---")
print(region_units)


# --------------------------------------------------
# 13. Multiple Aggregations by Region
# --------------------------------------------------

region_summary = df.groupby(
    "Region"
).agg(
    Revenue=("Revenue", "sum"),
    Expenses=("Expenses", "sum"),
    Profit=("Profit", "sum"),
    Units_Sold=("Units_Sold", "sum")
)

print("\n--- Regional Business Summary ---")
print(region_summary)


# --------------------------------------------------
# 14. Product Revenue Analysis
# --------------------------------------------------

product_revenue = df.groupby(
    "Product"
)["Revenue"].sum()

print("\n--- Revenue by Product ---")
print(product_revenue)


# --------------------------------------------------
# 15. Product Profit Analysis
# --------------------------------------------------

product_profit = df.groupby(
    "Product"
)["Profit"].sum()

print("\n--- Profit by Product ---")
print(product_profit)


# --------------------------------------------------
# 16. Product Performance Summary
# --------------------------------------------------

product_summary = df.groupby(
    "Product"
).agg(
    Revenue=("Revenue", "sum"),
    Units_Sold=("Units_Sold", "sum"),
    Profit=("Profit", "sum")
)

print("\n--- Product Performance ---")
print(product_summary)


# --------------------------------------------------
# 17. Salesperson Performance
# --------------------------------------------------

salesperson_summary = df.groupby(
    "Salesperson"
).agg(
    Revenue=("Revenue", "sum"),
    Units_Sold=("Units_Sold", "sum"),
    Profit=("Profit", "sum")
)

print("\n--- Salesperson Performance ---")
print(salesperson_summary)


# --------------------------------------------------
# 18. Sort by Revenue
# --------------------------------------------------

revenue_ranking = salesperson_summary.sort_values(
    by="Revenue",
    ascending=False
)

print("\n--- Salesperson Revenue Ranking ---")
print(revenue_ranking)


# --------------------------------------------------
# 19. Top Salesperson
# --------------------------------------------------

top_salesperson = revenue_ranking.index[0]

top_salesperson_revenue = revenue_ranking.iloc[0]["Revenue"]

print("\n--- Top Salesperson ---")
print("Name:", top_salesperson)
print("Revenue:", top_salesperson_revenue)


# --------------------------------------------------
# 20. Top Product
# --------------------------------------------------

top_product = product_summary["Revenue"].idxmax()

top_product_revenue = product_summary[
    "Revenue"
].max()

print("\n--- Top Product ---")
print("Product:", top_product)
print("Revenue:", top_product_revenue)


# --------------------------------------------------
# 21. Top Region
# --------------------------------------------------

top_region = region_summary["Revenue"].idxmax()

top_region_revenue = region_summary[
    "Revenue"
].max()

print("\n--- Top Region ---")
print("Region:", top_region)
print("Revenue:", top_region_revenue)


# --------------------------------------------------
# 22. Revenue Ranking
# --------------------------------------------------

region_ranking = region_summary.sort_values(
    by="Revenue",
    ascending=False
)

print("\n--- Regional Revenue Ranking ---")
print(region_ranking)


# --------------------------------------------------
# 23. Profit Margin by Region
# --------------------------------------------------

region_summary["Profit_Margin"] = (
    region_summary["Profit"] /
    region_summary["Revenue"]
) * 100

print("\n--- Regional Profit Margin ---")
print(region_summary)


# --------------------------------------------------
# 24. Filter High-Revenue Transactions
# --------------------------------------------------

high_revenue = df[
    df["Revenue"] > 1000000
]

print("\n--- High-Revenue Transactions ---")
print(high_revenue)


# --------------------------------------------------
# 25. Filter High-Profit Transactions
# --------------------------------------------------

high_profit = df[
    df["Profit"] > 200000
]

print("\n--- High-Profit Transactions ---")
print(high_profit)


# --------------------------------------------------
# 26. Cross-Tab Analysis
# --------------------------------------------------

product_region = pd.pivot_table(
    df,
    values="Revenue",
    index="Region",
    columns="Product",
    aggfunc="sum",
    fill_value=0
)

print("\n--- Revenue by Region and Product ---")
print(product_region)


# --------------------------------------------------
# 27. Product Contribution
# --------------------------------------------------

product_summary["Revenue_Share"] = (
    product_summary["Revenue"] /
    product_summary["Revenue"].sum()
) * 100

print("\n--- Product Revenue Contribution ---")
print(product_summary)


# --------------------------------------------------
# 28. Business KPI Dashboard Values
# --------------------------------------------------

total_revenue = df["Revenue"].sum()

total_profit = df["Profit"].sum()

total_units = df["Units_Sold"].sum()

overall_margin = (
    total_profit / total_revenue
) * 100

average_order_value = (
    total_revenue / len(df)
)

print("\n--- Business KPI Summary ---")

print("Total Revenue:", total_revenue)
print("Total Profit:", total_profit)
print("Total Units Sold:", total_units)
print("Overall Profit Margin:", overall_margin)
print("Average Order Value:", average_order_value)


# --------------------------------------------------
# 29. Region with Highest Profit
# --------------------------------------------------

highest_profit_region = region_summary[
    "Profit"
].idxmax()

print("\nHighest Profit Region:", highest_profit_region)


# --------------------------------------------------
# 30. Product with Highest Units Sold
# --------------------------------------------------

highest_volume_product = product_summary[
    "Units_Sold"
].idxmax()

print(
    "Highest Volume Product:",
    highest_volume_product
)


# --------------------------------------------------
# 31. Mini Business Insight
# --------------------------------------------------

print("\n--- Key Business Insights ---")

print(
    f"Top revenue region: {top_region}"
)

print(
    f"Top revenue product: {top_product}"
)

print(
    f"Top salesperson: {top_salesperson}"
)

print(
    f"Overall profit margin: {overall_margin:.2f}%"
)


# --------------------------------------------------
# 32. Export Analysis
# --------------------------------------------------

region_summary.to_csv(
    "regional_business_summary.csv"
)

product_summary.to_csv(
    "product_business_summary.csv"
)

print("\nAnalysis files exported successfully.")


# --------------------------------------------------
# Key Takeaway
# --------------------------------------------------

print("\nDay 18 Complete: Pandas Data Analysis & GroupBy")
