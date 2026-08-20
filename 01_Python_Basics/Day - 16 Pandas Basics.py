"""
Day 16 - Pandas Basics
Business Analytics Python Log Playbook

Pandas is a Python library used for data manipulation and analysis.

It provides powerful data structures such as Series and DataFrames
for working with structured and tabular data.
"""

import pandas as pd


# --------------------------------------------------
# 1. Creating a Pandas Series
# --------------------------------------------------

sales = pd.Series([
    45000,
    52000,
    61000,
    58000,
    67000
])

print("Sales Series:")
print(sales)


# --------------------------------------------------
# 2. Creating a DataFrame
# --------------------------------------------------

data = {
    "Month": [
        "January",
        "February",
        "March",
        "April",
        "May"
    ],
    "Revenue": [
        45000,
        52000,
        61000,
        58000,
        67000
    ],
    "Expenses": [
        28000,
        31000,
        35000,
        33000,
        39000
    ]
}

df = pd.DataFrame(data)

print("\n--- Sales DataFrame ---")
print(df)


# --------------------------------------------------
# 3. Viewing the First Rows
# --------------------------------------------------

print("\n--- First 3 Rows ---")
print(df.head(3))


# --------------------------------------------------
# 4. Viewing the Last Rows
# --------------------------------------------------

print("\n--- Last 2 Rows ---")
print(df.tail(2))


# --------------------------------------------------
# 5. Checking DataFrame Shape
# --------------------------------------------------

print("\nDataFrame Shape:")
print(df.shape)


# --------------------------------------------------
# 6. Checking Column Names
# --------------------------------------------------

print("\nColumn Names:")
print(df.columns)


# --------------------------------------------------
# 7. Checking Data Types
# --------------------------------------------------

print("\nData Types:")
print(df.dtypes)


# --------------------------------------------------
# 8. Selecting a Column
# --------------------------------------------------

print("\nRevenue Column:")
print(df["Revenue"])


# --------------------------------------------------
# 9. Selecting Multiple Columns
# --------------------------------------------------

print("\nRevenue and Expenses:")
print(df[["Revenue", "Expenses"]])


# --------------------------------------------------
# 10. Creating a New Column
# --------------------------------------------------

df["Profit"] = df["Revenue"] - df["Expenses"]

print("\n--- DataFrame with Profit ---")
print(df)


# --------------------------------------------------
# 11. Creating Profit Margin
# --------------------------------------------------

df["Profit_Margin"] = (
    df["Profit"] / df["Revenue"]
) * 100

print("\n--- Profit Margin ---")
print(df)


# --------------------------------------------------
# 12. Basic Statistics
# --------------------------------------------------

print("\n--- Statistical Summary ---")
print(df.describe())


# --------------------------------------------------
# 13. Calculating Total Revenue
# --------------------------------------------------

total_revenue = df["Revenue"].sum()

print("\nTotal Revenue:", total_revenue)


# --------------------------------------------------
# 14. Calculating Average Revenue
# --------------------------------------------------

average_revenue = df["Revenue"].mean()

print("Average Revenue:", average_revenue)


# --------------------------------------------------
# 15. Finding Maximum Revenue
# --------------------------------------------------

maximum_revenue = df["Revenue"].max()

print("Maximum Revenue:", maximum_revenue)


# --------------------------------------------------
# 16. Finding Minimum Revenue
# --------------------------------------------------

minimum_revenue = df["Revenue"].min()

print("Minimum Revenue:", minimum_revenue)


# --------------------------------------------------
# 17. Filtering Data
# --------------------------------------------------

high_revenue = df[df["Revenue"] > 55000]

print("\n--- High Revenue Months ---")
print(high_revenue)


# --------------------------------------------------
# 18. Multiple Conditions
# --------------------------------------------------

high_profit = df[
    (df["Revenue"] > 50000) &
    (df["Profit"] > 20000)
]

print("\n--- High Revenue and High Profit ---")
print(high_profit)


# --------------------------------------------------
# 19. Sorting Data
# --------------------------------------------------

sorted_df = df.sort_values(
    by="Revenue",
    ascending=False
)

print("\n--- Revenue Sorted Descending ---")
print(sorted_df)


# --------------------------------------------------
# 20. Adding a Category
# --------------------------------------------------

df["Performance"] = df["Profit"].apply(
    lambda profit:
    "High" if profit >= 25000
    else "Moderate"
)

print("\n--- Performance Category ---")
print(df)


# --------------------------------------------------
# 21. Checking Missing Values
# --------------------------------------------------

print("\n--- Missing Values ---")
print(df.isnull().sum())


# --------------------------------------------------
# 22. Creating Data with Missing Values
# --------------------------------------------------

customer_data = {
    "Customer": [
        "Aarav",
        "Meera",
        "Rohan",
        "Ananya",
        "Kabir"
    ],
    "Age": [
        25,
        28,
        None,
        32,
        27
    ],
    "Purchase": [
        25000,
        42000,
        18000,
        None,
        35000
    ]
}

customer_df = pd.DataFrame(customer_data)

print("\n--- Customer Data ---")
print(customer_df)


# --------------------------------------------------
# 23. Handling Missing Values
# --------------------------------------------------

print("\nMissing Values:")
print(customer_df.isnull().sum())


# --------------------------------------------------
# 24. Filling Missing Values
# --------------------------------------------------

customer_df["Age"] = customer_df["Age"].fillna(
    customer_df["Age"].mean()
)

customer_df["Purchase"] = customer_df["Purchase"].fillna(0)

print("\n--- Cleaned Customer Data ---")
print(customer_df)


# --------------------------------------------------
# 25. Renaming Columns
# --------------------------------------------------

customer_df = customer_df.rename(
    columns={
        "Customer": "Customer_Name",
        "Purchase": "Purchase_Amount"
    }
)

print("\n--- Renamed Columns ---")
print(customer_df)


# --------------------------------------------------
# 26. Reading a CSV File
# --------------------------------------------------

try:

    sales_df = pd.read_csv("sales_data.csv")

    print("\n--- CSV Data ---")
    print(sales_df.head())

except FileNotFoundError:

    print(
        "\nNo sales_data.csv file found."
        " Create or upload the file before reading it."
    )


# --------------------------------------------------
# 27. Creating a Business Dataset
# --------------------------------------------------

business_data = pd.DataFrame({

    "Customer_ID": [
        "C101",
        "C102",
        "C103",
        "C104",
        "C105"
    ],

    "Region": [
        "North",
        "South",
        "West",
        "North",
        "South"
    ],

    "Revenue": [
        35000,
        52000,
        28000,
        67000,
        45000
    ],

    "Orders": [
        3,
        5,
        2,
        7,
        4
    ]
})

print("\n--- Business Dataset ---")
print(business_data)


# --------------------------------------------------
# 28. Business KPI Analysis
# --------------------------------------------------

total_revenue = business_data["Revenue"].sum()

total_orders = business_data["Orders"].sum()

average_order_value = (
    total_revenue / total_orders
)

print("\n--- Business KPIs ---")
print("Total Revenue:", total_revenue)
print("Total Orders:", total_orders)
print("Average Order Value:", average_order_value)


# --------------------------------------------------
# 29. Region-Based Analysis
# --------------------------------------------------

region_summary = business_data.groupby(
    "Region"
)["Revenue"].sum()

print("\n--- Revenue by Region ---")
print(region_summary)


# --------------------------------------------------
# 30. Mini Challenge
# --------------------------------------------------

products = pd.DataFrame({

    "Product": [
        "Laptop",
        "Phone",
        "Tablet",
        "Headphones",
        "Monitor"
    ],

    "Price": [
        75000,
        45000,
        30000,
        8000,
        18000
    ],

    "Units_Sold": [
        12,
        25,
        18,
        40,
        22
    ]
})

products["Revenue"] = (
    products["Price"] *
    products["Units_Sold"]
)

print("\n--- Product Analysis ---")
print(products)

print(
    "\nTotal Product Revenue:",
    products["Revenue"].sum()
)

print(
    "Best Selling Product:",
    products.loc[
        products["Units_Sold"].idxmax(),
        "Product"
    ]
)

print(
    "Highest Revenue Product:",
    products.loc[
        products["Revenue"].idxmax(),
        "Product"
    ]
)


# --------------------------------------------------
# Key Takeaway
# --------------------------------------------------

print("\nDay 16 Complete: Pandas Basics")
