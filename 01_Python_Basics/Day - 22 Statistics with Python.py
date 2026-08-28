"""
Day 22 - Statistics with Python
Business Analytics Python Log Playbook

Statistics helps analysts understand patterns,
variation, and relationships within business data.

Topics:
- Mean
- Median
- Mode
- Range
- Variance
- Standard Deviation
- Percentiles
- Quartiles
- Correlation
"""

import pandas as pd
import numpy as np
import statistics


# --------------------------------------------------
# 1. Create Business Dataset
# --------------------------------------------------

sales = [
    12000,
    15000,
    18000,
    14000,
    21000,
    25000,
    19000,
    22000,
    17000,
    30000
]

df = pd.DataFrame({
    "Sales": sales
})

print("--- Sales Dataset ---")
print(df)


# --------------------------------------------------
# 2. Mean
# --------------------------------------------------

mean_sales = np.mean(sales)

print("\nMean Sales:", mean_sales)


# --------------------------------------------------
# 3. Median
# --------------------------------------------------

median_sales = np.median(sales)

print("Median Sales:", median_sales)


# --------------------------------------------------
# 4. Mode
# --------------------------------------------------

customer_orders = [
    2, 3, 2, 5, 4,
    2, 6, 3, 2, 5
]

mode_orders = statistics.mode(
    customer_orders
)

print("Most Common Number of Orders:", mode_orders)


# --------------------------------------------------
# 5. Minimum and Maximum
# --------------------------------------------------

minimum_sales = min(sales)

maximum_sales = max(sales)

print("\nMinimum Sales:", minimum_sales)

print("Maximum Sales:", maximum_sales)


# --------------------------------------------------
# 6. Range
# --------------------------------------------------

sales_range = maximum_sales - minimum_sales

print("Sales Range:", sales_range)


# --------------------------------------------------
# 7. Variance
# --------------------------------------------------

sales_variance = np.var(
    sales,
    ddof=1
)

print("\nSales Variance:", sales_variance)


# --------------------------------------------------
# 8. Standard Deviation
# --------------------------------------------------

sales_std = np.std(
    sales,
    ddof=1
)

print("Sales Standard Deviation:", sales_std)


# --------------------------------------------------
# 9. Percentiles
# --------------------------------------------------

percentile_25 = np.percentile(
    sales,
    25
)

percentile_50 = np.percentile(
    sales,
    50
)

percentile_75 = np.percentile(
    sales,
    75
)

print("\n25th Percentile:", percentile_25)

print("50th Percentile:", percentile_50)

print("75th Percentile:", percentile_75)


# --------------------------------------------------
# 10. Quartiles
# --------------------------------------------------

Q1 = np.percentile(sales, 25)

Q2 = np.percentile(sales, 50)

Q3 = np.percentile(sales, 75)

print("\n--- Quartiles ---")

print("Q1:", Q1)

print("Q2:", Q2)

print("Q3:", Q3)


# --------------------------------------------------
# 11. Interquartile Range
# --------------------------------------------------

IQR = Q3 - Q1

print("Interquartile Range:", IQR)


# --------------------------------------------------
# 12. Detect Outliers
# --------------------------------------------------

lower_limit = Q1 - 1.5 * IQR

upper_limit = Q3 + 1.5 * IQR

outliers = [
    value
    for value in sales
    if value < lower_limit or value > upper_limit
]

print("\n--- Outliers ---")

print(outliers)


# --------------------------------------------------
# 13. Coefficient of Variation
# --------------------------------------------------

coefficient_variation = (
    sales_std / mean_sales
) * 100

print(
    "\nCoefficient of Variation:",
    round(coefficient_variation, 2),
    "%"
)


# --------------------------------------------------
# 14. Create Business Dataset
# --------------------------------------------------

data = {
    "Marketing_Spend": [
        5000, 7000, 6000, 9000, 10000,
        12000, 8000, 11000, 13000, 15000
    ],

    "Revenue": [
        18000, 24000, 21000, 30000, 35000,
        40000, 28000, 37000, 42000, 48000
    ],

    "Orders": [
        45, 55, 50, 68, 75,
        82, 62, 78, 90, 105
    ]
}

business_df = pd.DataFrame(data)

print("\n--- Business Dataset ---")

print(business_df)


# --------------------------------------------------
# 15. Descriptive Statistics
# --------------------------------------------------

print("\n--- Descriptive Statistics ---")

print(
    business_df.describe()
)


# --------------------------------------------------
# 16. Mean of Business Metrics
# --------------------------------------------------

print("\n--- Mean ---")

print(
    business_df.mean(numeric_only=True)
)


# --------------------------------------------------
# 17. Median of Business Metrics
# --------------------------------------------------

print("\n--- Median ---")

print(
    business_df.median(numeric_only=True)
)


# --------------------------------------------------
# 18. Standard Deviation
# --------------------------------------------------

print("\n--- Standard Deviation ---")

print(
    business_df.std(numeric_only=True)
)


# --------------------------------------------------
# 19. Variance
# --------------------------------------------------

print("\n--- Variance ---")

print(
    business_df.var(numeric_only=True)
)


# --------------------------------------------------
# 20. Correlation
# --------------------------------------------------

correlation = business_df.corr()

print("\n--- Correlation Matrix ---")

print(correlation)


# --------------------------------------------------
# 21. Marketing Spend vs Revenue
# --------------------------------------------------

marketing_revenue_corr = correlation.loc[
    "Marketing_Spend",
    "Revenue"
]

print(
    "\nMarketing Spend vs Revenue Correlation:",
    round(marketing_revenue_corr, 2)
)


# --------------------------------------------------
# 22. Orders vs Revenue
# --------------------------------------------------

orders_revenue_corr = correlation.loc[
    "Orders",
    "Revenue"
]

print(
    "Orders vs Revenue Correlation:",
    round(orders_revenue_corr, 2)
)


# --------------------------------------------------
# 23. Z-Score
# --------------------------------------------------

business_df["Revenue_Z_Score"] = (
    business_df["Revenue"]
    - business_df["Revenue"].mean()
) / business_df["Revenue"].std()

print("\n--- Revenue Z-Scores ---")

print(
    business_df[
        [
            "Revenue",
            "Revenue_Z_Score"
        ]
    ]
)


# --------------------------------------------------
# 24. Identify Above-Average Revenue
# --------------------------------------------------

average_revenue = business_df[
    "Revenue"
].mean()

above_average = business_df[
    business_df["Revenue"] > average_revenue
]

print("\n--- Above Average Revenue ---")

print(above_average)


# --------------------------------------------------
# 25. Identify High Revenue Records
# --------------------------------------------------

high_revenue = business_df[
    business_df["Revenue"] >= 40000
]

print("\n--- High Revenue Records ---")

print(high_revenue)


# --------------------------------------------------
# 26. Revenue Distribution
# --------------------------------------------------

business_df["Revenue"].plot(
    kind="hist",
    bins=5,
    figsize=(8, 5),
    title="Revenue Distribution"
)

print("\nRevenue distribution chart created.")


# --------------------------------------------------
# 27. Revenue Box Plot
# --------------------------------------------------

business_df["Revenue"].plot(
    kind="box",
    figsize=(6, 5),
    title="Revenue Box Plot"
)

print("Revenue box plot created.")


# --------------------------------------------------
# 28. Business Summary
# --------------------------------------------------

total_revenue = business_df[
    "Revenue"
].sum()

average_revenue = business_df[
    "Revenue"
].mean()

median_revenue = business_df[
    "Revenue"
].median()

revenue_std = business_df[
    "Revenue"
].std()

print("\n--- Business Statistics Summary ---")

print("Total Revenue:", total_revenue)

print(
    "Average Revenue:",
    round(average_revenue, 2)
)

print(
    "Median Revenue:",
    round(median_revenue, 2)
)

print(
    "Revenue Standard Deviation:",
    round(revenue_std, 2)
)


# --------------------------------------------------
# 29. Statistical Insights
# --------------------------------------------------

print("\n--- Statistical Insights ---")

if mean_sales > median_sales:
    print(
        "Mean sales are higher than median sales, "
        "indicating possible influence from higher values."
    )
else:
    print(
        "Mean sales are not higher than median sales."
    )

print(
    f"Marketing and revenue correlation: "
    f"{marketing_revenue_corr:.2f}"
)

print(
    f"Orders and revenue correlation: "
    f"{orders_revenue_corr:.2f}"
)


# --------------------------------------------------
# Key Takeaway
# --------------------------------------------------

print("\nDay 22 Complete: Statistics with Python")
