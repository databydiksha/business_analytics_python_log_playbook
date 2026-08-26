"""
Day 21 - Seaborn Data Visualization
Business Analytics Python Log Playbook

Seaborn is a Python visualization library built on Matplotlib.
It is useful for statistical visualization and exploratory
data analysis.
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# --------------------------------------------------
# 1. Create Business Dataset
# --------------------------------------------------

data = {
    "Region": [
        "North", "South", "West", "East",
        "North", "South", "West", "East",
        "North", "South", "West", "East"
    ],

    "Product": [
        "Laptop", "Phone", "Tablet", "Laptop",
        "Phone", "Tablet", "Laptop", "Phone",
        "Tablet", "Laptop", "Phone", "Tablet"
    ],

    "Marketing_Spend": [
        12000, 15000, 9000, 11000,
        18000, 10000, 14000, 16000,
        8000, 19000, 13000, 10000
    ],

    "Orders": [
        8, 15, 6, 10,
        18, 9, 14, 16,
        5, 20, 12, 7
    ],

    "Revenue": [
        48000, 75000, 36000, 52000,
        92000, 45000, 70000, 80000,
        30000, 98000, 62000, 40000
    ]
}

df = pd.DataFrame(data)

print("--- Business Dataset ---")
print(df)


# --------------------------------------------------
# 2. Dataset Overview
# --------------------------------------------------

print("\n--- Dataset Shape ---")
print(df.shape)

print("\n--- Data Types ---")
print(df.dtypes)

print("\n--- Missing Values ---")
print(df.isnull().sum())


# --------------------------------------------------
# 3. Create Revenue per Order
# --------------------------------------------------

df["Revenue_Per_Order"] = (
    df["Revenue"] / df["Orders"]
)

print("\n--- Revenue Per Order ---")
print(df)


# --------------------------------------------------
# 4. Set Seaborn Theme
# --------------------------------------------------

sns.set_theme()


# --------------------------------------------------
# 5. Revenue Distribution
# --------------------------------------------------

plt.figure(figsize=(8, 5))

sns.histplot(
    data=df,
    x="Revenue",
    bins=6,
    kde=True
)

plt.title("Revenue Distribution")
plt.xlabel("Revenue")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()


# --------------------------------------------------
# 6. Orders Distribution
# --------------------------------------------------

plt.figure(figsize=(8, 5))

sns.histplot(
    data=df,
    x="Orders",
    bins=6,
    kde=True
)

plt.title("Orders Distribution")
plt.xlabel("Orders")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()


# --------------------------------------------------
# 7. Revenue by Region
# --------------------------------------------------

plt.figure(figsize=(8, 5))

sns.barplot(
    data=df,
    x="Region",
    y="Revenue",
    estimator="sum"
)

plt.title("Total Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Revenue")
plt.tight_layout()
plt.show()


# --------------------------------------------------
# 8. Revenue by Product
# --------------------------------------------------

plt.figure(figsize=(8, 5))

sns.barplot(
    data=df,
    x="Product",
    y="Revenue",
    estimator="sum"
)

plt.title("Total Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.tight_layout()
plt.show()


# --------------------------------------------------
# 9. Orders by Product
# --------------------------------------------------

plt.figure(figsize=(8, 5))

sns.barplot(
    data=df,
    x="Product",
    y="Orders",
    estimator="sum"
)

plt.title("Total Orders by Product")
plt.xlabel("Product")
plt.ylabel("Orders")
plt.tight_layout()
plt.show()


# --------------------------------------------------
# 10. Marketing Spend vs Revenue
# --------------------------------------------------

plt.figure(figsize=(8, 5))

sns.scatterplot(
    data=df,
    x="Marketing_Spend",
    y="Revenue",
    hue="Region",
    style="Product",
    s=100
)

plt.title("Marketing Spend vs Revenue")
plt.xlabel("Marketing Spend")
plt.ylabel("Revenue")
plt.tight_layout()
plt.show()


# --------------------------------------------------
# 11. Orders vs Revenue
# --------------------------------------------------

plt.figure(figsize=(8, 5))

sns.scatterplot(
    data=df,
    x="Orders",
    y="Revenue",
    hue="Product",
    s=100
)

plt.title("Orders vs Revenue")
plt.xlabel("Orders")
plt.ylabel("Revenue")
plt.tight_layout()
plt.show()


# --------------------------------------------------
# 12. Revenue by Region and Product
# --------------------------------------------------

plt.figure(figsize=(9, 5))

sns.barplot(
    data=df,
    x="Region",
    y="Revenue",
    hue="Product",
    estimator="sum"
)

plt.title("Revenue by Region and Product")
plt.xlabel("Region")
plt.ylabel("Revenue")
plt.tight_layout()
plt.show()


# --------------------------------------------------
# 13. Box Plot
# --------------------------------------------------

plt.figure(figsize=(8, 5))

sns.boxplot(
    data=df,
    x="Product",
    y="Revenue"
)

plt.title("Revenue Distribution by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.tight_layout()
plt.show()


# --------------------------------------------------
# 14. Violin Plot
# --------------------------------------------------

plt.figure(figsize=(8, 5))

sns.violinplot(
    data=df,
    x="Region",
    y="Revenue"
)

plt.title("Revenue Distribution by Region")
plt.xlabel("Region")
plt.ylabel("Revenue")
plt.tight_layout()
plt.show()


# --------------------------------------------------
# 15. Strip Plot
# --------------------------------------------------

plt.figure(figsize=(8, 5))

sns.stripplot(
    data=df,
    x="Product",
    y="Revenue",
    jitter=True
)

plt.title("Revenue Distribution Across Products")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.tight_layout()
plt.show()


# --------------------------------------------------
# 16. Correlation Matrix
# --------------------------------------------------

numeric_columns = [
    "Marketing_Spend",
    "Orders",
    "Revenue",
    "Revenue_Per_Order"
]

correlation_matrix = df[
    numeric_columns
].corr()

print("\n--- Correlation Matrix ---")
print(correlation_matrix)


# --------------------------------------------------
# 17. Correlation Heatmap
# --------------------------------------------------

plt.figure(figsize=(8, 6))

sns.heatmap(
    correlation_matrix,
    annot=True,
    fmt=".2f",
    linewidths=0.5
)

plt.title("Business Metrics Correlation Heatmap")
plt.tight_layout()
plt.show()


# --------------------------------------------------
# 18. Pair Plot
# --------------------------------------------------

sns.pairplot(
    df[
        [
            "Marketing_Spend",
            "Orders",
            "Revenue",
            "Revenue_Per_Order"
        ]
    ]
)

plt.show()


# --------------------------------------------------
# 19. Regional Summary
# --------------------------------------------------

region_summary = df.groupby(
    "Region"
).agg(
    Revenue=("Revenue", "sum"),
    Orders=("Orders", "sum"),
    Marketing_Spend=("Marketing_Spend", "sum")
)

print("\n--- Regional Summary ---")
print(region_summary)


# --------------------------------------------------
# 20. Product Summary
# --------------------------------------------------

product_summary = df.groupby(
    "Product"
).agg(
    Revenue=("Revenue", "sum"),
    Orders=("Orders", "sum"),
    Marketing_Spend=("Marketing_Spend", "sum")
)

print("\n--- Product Summary ---")
print(product_summary)


# --------------------------------------------------
# 21. Identify Top Region
# --------------------------------------------------

top_region = region_summary[
    "Revenue"
].idxmax()

top_region_revenue = region_summary[
    "Revenue"
].max()

print("\n--- Top Region ---")
print("Region:", top_region)
print("Revenue:", top_region_revenue)


# --------------------------------------------------
# 22. Identify Top Product
# --------------------------------------------------

top_product = product_summary[
    "Revenue"
].idxmax()

top_product_revenue = product_summary[
    "Revenue"
].max()

print("\n--- Top Product ---")
print("Product:", top_product)
print("Revenue:", top_product_revenue)


# --------------------------------------------------
# 23. Marketing Efficiency
# --------------------------------------------------

df["Marketing_ROI"] = (
    df["Revenue"] /
    df["Marketing_Spend"]
)

print("\n--- Marketing ROI ---")
print(
    df[
        [
            "Region",
            "Product",
            "Marketing_Spend",
            "Revenue",
            "Marketing_ROI"
        ]
    ]
)


# --------------------------------------------------
# 24. Highest Marketing ROI
# --------------------------------------------------

best_roi = df.loc[
    df["Marketing_ROI"].idxmax()
]

print("\n--- Highest Marketing ROI ---")

print("Region:", best_roi["Region"])
print("Product:", best_roi["Product"])
print("ROI:", round(best_roi["Marketing_ROI"], 2))


# --------------------------------------------------
# 25. Business Insights
# --------------------------------------------------

marketing_correlation = correlation_matrix.loc[
    "Marketing_Spend",
    "Revenue"
]

orders_correlation = correlation_matrix.loc[
    "Orders",
    "Revenue"
]

print("\n--- Business Insights ---")

print(
    f"Top revenue region: {top_region}"
)

print(
    f"Top revenue product: {top_product}"
)

print(
    f"Marketing spend vs revenue correlation: "
    f"{marketing_correlation:.2f}"
)

print(
    f"Orders vs revenue correlation: "
    f"{orders_correlation:.2f}"
)


# --------------------------------------------------
# 26. Export Analysis
# --------------------------------------------------

region_summary.to_csv(
    "seaborn_region_analysis.csv"
)

product_summary.to_csv(
    "seaborn_product_analysis.csv"
)

print("\nAnalysis files saved successfully.")


# --------------------------------------------------
# Key Takeaway
# --------------------------------------------------

print("\nDay 21 Complete: Seaborn Data Visualization")
