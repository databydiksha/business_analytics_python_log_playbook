"""
Day 19 - Pandas Data Visualization
Business Analytics Python Log Playbook

Visualization helps convert business data into charts
that make trends, comparisons, and patterns easier to understand.

Libraries used:
- Pandas
- Matplotlib
"""

import pandas as pd
import matplotlib.pyplot as plt


# --------------------------------------------------
# 1. Create Business Dataset
# --------------------------------------------------

data = {
    "Month": [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June"
    ],

    "Revenue": [
        45000,
        52000,
        61000,
        58000,
        67000,
        74000
    ],

    "Expenses": [
        28000,
        31000,
        35000,
        33000,
        39000,
        42000
    ],

    "Orders": [
        120,
        145,
        160,
        150,
        175,
        190
    ]
}

df = pd.DataFrame(data)


# --------------------------------------------------
# 2. Create Profit Column
# --------------------------------------------------

df["Profit"] = df["Revenue"] - df["Expenses"]

print("--- Business Dataset ---")
print(df)


# --------------------------------------------------
# 3. Revenue Trend
# --------------------------------------------------

plt.figure(figsize=(10, 5))

df.plot(
    x="Month",
    y="Revenue",
    kind="line",
    marker="o",
    title="Monthly Revenue Trend"
)

plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# --------------------------------------------------
# 4. Expense Trend
# --------------------------------------------------

df.plot(
    x="Month",
    y="Expenses",
    kind="line",
    marker="o",
    title="Monthly Expense Trend",
    figsize=(10, 5)
)

plt.xlabel("Month")
plt.ylabel("Expenses")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# --------------------------------------------------
# 5. Profit Trend
# --------------------------------------------------

df.plot(
    x="Month",
    y="Profit",
    kind="line",
    marker="o",
    title="Monthly Profit Trend",
    figsize=(10, 5)
)

plt.xlabel("Month")
plt.ylabel("Profit")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# --------------------------------------------------
# 6. Revenue vs Expenses
# --------------------------------------------------

df.plot(
    x="Month",
    y=["Revenue", "Expenses"],
    kind="bar",
    figsize=(10, 5),
    title="Revenue vs Expenses"
)

plt.xlabel("Month")
plt.ylabel("Amount")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# --------------------------------------------------
# 7. Monthly Profit Bar Chart
# --------------------------------------------------

df.plot(
    x="Month",
    y="Profit",
    kind="bar",
    figsize=(10, 5),
    title="Monthly Profit"
)

plt.xlabel("Month")
plt.ylabel("Profit")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# --------------------------------------------------
# 8. Orders Trend
# --------------------------------------------------

df.plot(
    x="Month",
    y="Orders",
    kind="line",
    marker="o",
    figsize=(10, 5),
    title="Monthly Orders Trend"
)

plt.xlabel("Month")
plt.ylabel("Number of Orders")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# --------------------------------------------------
# 9. Revenue Distribution
# --------------------------------------------------

df["Revenue"].plot(
    kind="hist",
    bins=5,
    figsize=(8, 5),
    title="Revenue Distribution"
)

plt.xlabel("Revenue")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()


# --------------------------------------------------
# 10. Profit Distribution
# --------------------------------------------------

df["Profit"].plot(
    kind="hist",
    bins=5,
    figsize=(8, 5),
    title="Profit Distribution"
)

plt.xlabel("Profit")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()


# --------------------------------------------------
# 11. Box Plot for Revenue
# --------------------------------------------------

df["Revenue"].plot(
    kind="box",
    figsize=(6, 5),
    title="Revenue Distribution and Outliers"
)

plt.ylabel("Revenue")
plt.tight_layout()
plt.show()


# --------------------------------------------------
# 12. Box Plot for Profit
# --------------------------------------------------

df["Profit"].plot(
    kind="box",
    figsize=(6, 5),
    title="Profit Distribution and Outliers"
)

plt.ylabel("Profit")
plt.tight_layout()
plt.show()


# --------------------------------------------------
# 13. Revenue and Profit Comparison
# --------------------------------------------------

df.plot(
    x="Month",
    y=["Revenue", "Profit"],
    kind="line",
    marker="o",
    figsize=(10, 5),
    title="Revenue vs Profit Trend"
)

plt.xlabel("Month")
plt.ylabel("Amount")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# --------------------------------------------------
# 14. Orders vs Revenue
# --------------------------------------------------

df.plot(
    x="Orders",
    y="Revenue",
    kind="scatter",
    figsize=(8, 5),
    title="Orders vs Revenue"
)

plt.xlabel("Number of Orders")
plt.ylabel("Revenue")
plt.tight_layout()
plt.show()


# --------------------------------------------------
# 15. Revenue Share
# --------------------------------------------------

revenue_share = df.set_index("Month")["Revenue"]

revenue_share.plot(
    kind="pie",
    figsize=(8, 8),
    autopct="%1.1f%%",
    title="Monthly Revenue Share"
)

plt.ylabel("")
plt.tight_layout()
plt.show()


# --------------------------------------------------
# 16. Business KPI Summary
# --------------------------------------------------

total_revenue = df["Revenue"].sum()

total_expenses = df["Expenses"].sum()

total_profit = df["Profit"].sum()

total_orders = df["Orders"].sum()

average_revenue = df["Revenue"].mean()

overall_profit_margin = (
    total_profit / total_revenue
) * 100


print("\n--- Business KPI Summary ---")

print("Total Revenue:", total_revenue)

print("Total Expenses:", total_expenses)

print("Total Profit:", total_profit)

print("Total Orders:", total_orders)

print("Average Monthly Revenue:", average_revenue)

print(
    "Overall Profit Margin:",
    round(overall_profit_margin, 2),
    "%"
)


# --------------------------------------------------
# 17. Best Performing Month
# --------------------------------------------------

best_month = df.loc[
    df["Revenue"].idxmax(),
    "Month"
]

highest_revenue = df["Revenue"].max()

print("\n--- Best Performing Month ---")

print("Month:", best_month)

print("Revenue:", highest_revenue)


# --------------------------------------------------
# 18. Most Profitable Month
# --------------------------------------------------

profit_month = df.loc[
    df["Profit"].idxmax(),
    "Month"
]

highest_profit = df["Profit"].max()

print("\n--- Most Profitable Month ---")

print("Month:", profit_month)

print("Profit:", highest_profit)


# --------------------------------------------------
# 19. Business Insights
# --------------------------------------------------

revenue_growth = (
    (
        df["Revenue"].iloc[-1]
        - df["Revenue"].iloc[0]
    )
    / df["Revenue"].iloc[0]
) * 100

print("\n--- Business Insights ---")

print(
    f"Revenue increased by {revenue_growth:.2f}% "
    "from January to June."
)

print(
    f"{best_month} generated the highest revenue."
)

print(
    f"{profit_month} generated the highest profit."
)


# --------------------------------------------------
# 20. Save Dataset
# --------------------------------------------------

df.to_csv(
    "visualization_business_data.csv",
    index=False
)

print("\nDataset saved successfully.")


# --------------------------------------------------
# Key Takeaway
# --------------------------------------------------

print("\nDay 19 Complete: Pandas Data Visualization")
