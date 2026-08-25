"""
Day 20 - Exploratory Data Analysis
Business Analytics Python Log Playbook

Exploratory Data Analysis (EDA) is used to understand a dataset
before applying statistical analysis or machine learning.

Today's workflow:
- Data inspection
- Data quality checks
- Descriptive statistics
- Univariate analysis
- Bivariate analysis
- Correlation analysis
- Business insights
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# --------------------------------------------------
# 1. Create Business Dataset
# --------------------------------------------------

data = {
    "Customer_ID": [
        "C101", "C102", "C103", "C104", "C105",
        "C106", "C107", "C108", "C109", "C110",
        "C111", "C112"
    ],

    "Age": [
        23, 31, 28, 42, 35,
        26, 39, 30, 45, 33,
        27, 41
    ],

    "Region": [
        "North", "South", "West", "North", "South",
        "West", "East", "North", "South", "West",
        "East", "North"
    ],

    "Product": [
        "Laptop", "Phone", "Tablet", "Laptop", "Phone",
        "Laptop", "Tablet", "Phone", "Laptop", "Tablet",
        "Phone", "Laptop"
    ],

    "Marketing_Spend": [
        12000, 15000, 9000, 18000, 14000,
        11000, 8000, 16000, 19000, 10000,
        13000, 17000
    ],

    "Orders": [
        8, 15, 6, 18, 14,
        9, 5, 16, 20, 7,
        12, 17
    ],

    "Revenue": [
        48000, 75000, 36000, 92000, 70000,
        45000, 30000, 80000, 98000, 40000,
        62000, 85000
    ]
}

df = pd.DataFrame(data)

print("--- Dataset ---")
print(df)


# --------------------------------------------------
# 2. Understand Dataset Shape
# --------------------------------------------------

print("\n--- Dataset Shape ---")

print("Rows:", df.shape[0])
print("Columns:", df.shape[1])


# --------------------------------------------------
# 3. Inspect Column Names
# --------------------------------------------------

print("\n--- Columns ---")

print(df.columns.tolist())


# --------------------------------------------------
# 4. Check Data Types
# --------------------------------------------------

print("\n--- Data Types ---")

print(df.dtypes)


# --------------------------------------------------
# 5. Dataset Information
# --------------------------------------------------

print("\n--- Dataset Information ---")

df.info()


# --------------------------------------------------
# 6. Check Missing Values
# --------------------------------------------------

print("\n--- Missing Values ---")

print(df.isnull().sum())


# --------------------------------------------------
# 7. Check Duplicate Records
# --------------------------------------------------

print("\n--- Duplicate Records ---")

print(df.duplicated().sum())


# --------------------------------------------------
# 8. Descriptive Statistics
# --------------------------------------------------

print("\n--- Descriptive Statistics ---")

print(df.describe())


# --------------------------------------------------
# 9. Unique Values
# --------------------------------------------------

print("\n--- Unique Regions ---")

print(df["Region"].unique())


print("\n--- Unique Products ---")

print(df["Product"].unique())


# --------------------------------------------------
# 10. Number of Unique Customers
# --------------------------------------------------

unique_customers = df["Customer_ID"].nunique()

print("\nUnique Customers:", unique_customers)


# --------------------------------------------------
# 11. Revenue Statistics
# --------------------------------------------------

print("\n--- Revenue Statistics ---")

print("Total Revenue:", df["Revenue"].sum())

print("Average Revenue:", df["Revenue"].mean())

print("Median Revenue:", df["Revenue"].median())

print("Maximum Revenue:", df["Revenue"].max())

print("Minimum Revenue:", df["Revenue"].min())


# --------------------------------------------------
# 12. Order Statistics
# --------------------------------------------------

print("\n--- Order Statistics ---")

print("Total Orders:", df["Orders"].sum())

print("Average Orders:", df["Orders"].mean())

print("Maximum Orders:", df["Orders"].max())

print("Minimum Orders:", df["Orders"].min())


# --------------------------------------------------
# 13. Create Revenue per Order
# --------------------------------------------------

df["Revenue_Per_Order"] = (
    df["Revenue"] / df["Orders"]
)

print("\n--- Revenue Per Order ---")

print(df[
    [
        "Customer_ID",
        "Revenue",
        "Orders",
        "Revenue_Per_Order"
    ]
])


# --------------------------------------------------
# 14. Create Customer Value Segment
# --------------------------------------------------

def customer_segment(revenue):

    if revenue >= 80000:
        return "High Value"

    elif revenue >= 50000:
        return "Medium Value"

    else:
        return "Low Value"


df["Customer_Segment"] = df["Revenue"].apply(
    customer_segment
)

print("\n--- Customer Segments ---")

print(
    df[
        [
            "Customer_ID",
            "Revenue",
            "Customer_Segment"
        ]
    ]
)


# --------------------------------------------------
# 15. Customer Segment Distribution
# --------------------------------------------------

segment_count = df[
    "Customer_Segment"
].value_counts()

print("\n--- Customer Segment Distribution ---")

print(segment_count)


# --------------------------------------------------
# 16. Revenue by Region
# --------------------------------------------------

region_revenue = df.groupby(
    "Region"
)["Revenue"].sum().sort_values(
    ascending=False
)

print("\n--- Revenue by Region ---")

print(region_revenue)


# --------------------------------------------------
# 17. Average Revenue by Region
# --------------------------------------------------

region_average = df.groupby(
    "Region"
)["Revenue"].mean().sort_values(
    ascending=False
)

print("\n--- Average Revenue by Region ---")

print(region_average)


# --------------------------------------------------
# 18. Revenue by Product
# --------------------------------------------------

product_revenue = df.groupby(
    "Product"
)["Revenue"].sum().sort_values(
    ascending=False
)

print("\n--- Revenue by Product ---")

print(product_revenue)


# --------------------------------------------------
# 19. Orders by Product
# --------------------------------------------------

product_orders = df.groupby(
    "Product"
)["Orders"].sum().sort_values(
    ascending=False
)

print("\n--- Orders by Product ---")

print(product_orders)


# --------------------------------------------------
# 20. Marketing Spend vs Revenue
# --------------------------------------------------

marketing_correlation = df[
    [
        "Marketing_Spend",
        "Revenue"
    ]
].corr()

print("\n--- Marketing Spend and Revenue Correlation ---")

print(marketing_correlation)


# --------------------------------------------------
# 21. Orders vs Revenue Correlation
# --------------------------------------------------

orders_correlation = df[
    [
        "Orders",
        "Revenue"
    ]
].corr()

print("\n--- Orders and Revenue Correlation ---")

print(orders_correlation)


# --------------------------------------------------
# 22. Full Correlation Matrix
# --------------------------------------------------

numeric_columns = [
    "Age",
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
# 23. Revenue Distribution
# --------------------------------------------------

plt.figure(figsize=(8, 5))

df["Revenue"].plot(
    kind="hist",
    bins=6
)

plt.title("Revenue Distribution")
plt.xlabel("Revenue")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()


# --------------------------------------------------
# 24. Orders Distribution
# --------------------------------------------------

plt.figure(figsize=(8, 5))

df["Orders"].plot(
    kind="hist",
    bins=6
)

plt.title("Orders Distribution")
plt.xlabel("Orders")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()


# --------------------------------------------------
# 25. Revenue by Region
# --------------------------------------------------

plt.figure(figsize=(8, 5))

region_revenue.plot(
    kind="bar"
)

plt.title("Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Revenue")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# --------------------------------------------------
# 26. Revenue by Product
# --------------------------------------------------

plt.figure(figsize=(8, 5))

product_revenue.plot(
    kind="bar"
)

plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# --------------------------------------------------
# 27. Marketing Spend vs Revenue
# --------------------------------------------------

plt.figure(figsize=(8, 5))

plt.scatter(
    df["Marketing_Spend"],
    df["Revenue"]
)

plt.title("Marketing Spend vs Revenue")
plt.xlabel("Marketing Spend")
plt.ylabel("Revenue")
plt.tight_layout()
plt.show()


# --------------------------------------------------
# 28. Orders vs Revenue
# --------------------------------------------------

plt.figure(figsize=(8, 5))

plt.scatter(
    df["Orders"],
    df["Revenue"]
)

plt.title("Orders vs Revenue")
plt.xlabel("Orders")
plt.ylabel("Revenue")
plt.tight_layout()
plt.show()


# --------------------------------------------------
# 29. Revenue by Customer Segment
# --------------------------------------------------

segment_revenue = df.groupby(
    "Customer_Segment"
)["Revenue"].sum().sort_values(
    ascending=False
)

print("\n--- Revenue by Customer Segment ---")

print(segment_revenue)


# --------------------------------------------------
# 30. Top Customers
# --------------------------------------------------

top_customers = df.sort_values(
    by="Revenue",
    ascending=False
).head(5)

print("\n--- Top 5 Customers ---")

print(
    top_customers[
        [
            "Customer_ID",
            "Region",
            "Product",
            "Revenue"
        ]
    ]
)


# --------------------------------------------------
# 31. Highest Revenue Customer
# --------------------------------------------------

highest_customer = df.loc[
    df["Revenue"].idxmax()
]

print("\n--- Highest Revenue Customer ---")

print("Customer:", highest_customer["Customer_ID"])

print("Revenue:", highest_customer["Revenue"])

print("Region:", highest_customer["Region"])

print("Product:", highest_customer["Product"])


# --------------------------------------------------
# 32. Detect Revenue Outliers
# --------------------------------------------------

Q1 = df["Revenue"].quantile(0.25)

Q3 = df["Revenue"].quantile(0.75)

IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR

upper_limit = Q3 + 1.5 * IQR

outliers = df[
    (df["Revenue"] < lower_limit) |
    (df["Revenue"] > upper_limit)
]

print("\n--- Revenue Outliers ---")

print(outliers)


# --------------------------------------------------
# 33. Business KPIs
# --------------------------------------------------

total_revenue = df["Revenue"].sum()

total_orders = df["Orders"].sum()

average_order_value = (
    total_revenue / total_orders
)

average_customer_revenue = (
    df["Revenue"].mean()
)

print("\n--- Business KPIs ---")

print("Total Revenue:", total_revenue)

print("Total Orders:", total_orders)

print(
    "Average Order Value:",
    round(average_order_value, 2)
)

print(
    "Average Customer Revenue:",
    round(average_customer_revenue, 2)
)


# --------------------------------------------------
# 34. Key Business Insights
# --------------------------------------------------

top_region = region_revenue.index[0]

top_product = product_revenue.index[0]

top_customer = df.loc[
    df["Revenue"].idxmax(),
    "Customer_ID"
]

print("\n--- Key Business Insights ---")

print(
    "Highest Revenue Region:",
    top_region
)

print(
    "Highest Revenue Product:",
    top_product
)

print(
    "Highest Value Customer:",
    top_customer
)

print(
    "Marketing-Revenue Correlation:",
    round(
        marketing_correlation.loc[
            "Marketing_Spend",
            "Revenue"
        ],
        2
    )
)


# --------------------------------------------------
# 35. Export EDA Summary
# --------------------------------------------------

region_revenue.to_csv(
    "eda_region_revenue.csv"
)

product_revenue.to_csv(
    "eda_product_revenue.csv"
)

print("\nEDA summary files saved successfully.")


# --------------------------------------------------
# Key Takeaway
# --------------------------------------------------

print("\nDay 20 Complete: Exploratory Data Analysis")
