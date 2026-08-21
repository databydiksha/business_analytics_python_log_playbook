"""
Day 17 - Pandas Data Cleaning
Business Analytics Python Log Playbook

Data cleaning is the process of identifying and fixing
missing values, duplicates, incorrect data types, and
inconsistent data before analysis.
"""

import pandas as pd
import numpy as np


# --------------------------------------------------
# 1. Create a Messy Dataset
# --------------------------------------------------

data = {
    "Customer_ID": [
        "C101",
        "C102",
        "C103",
        "C104",
        "C105",
        "C105"
    ],

    "Name": [
        "Aarav",
        "Meera",
        "Rohan",
        "Ananya",
        "Kabir",
        "Kabir"
    ],

    "Age": [
        25,
        28,
        np.nan,
        32,
        27,
        27
    ],

    "City": [
        "Mumbai",
        "Delhi",
        "Mumbai",
        "Bengaluru",
        None,
        "Bengaluru"
    ],

    "Purchase": [
        25000,
        42000,
        18000,
        np.nan,
        35000,
        35000
    ]
}

df = pd.DataFrame(data)

print("--- Original Dataset ---")
print(df)


# --------------------------------------------------
# 2. Inspect Dataset
# --------------------------------------------------

print("\n--- Dataset Information ---")

print("Shape:", df.shape)

print("\nColumns:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)


# --------------------------------------------------
# 3. Check Missing Values
# --------------------------------------------------

print("\n--- Missing Values ---")

print(df.isnull().sum())


# --------------------------------------------------
# 4. Find Rows with Missing Values
# --------------------------------------------------

missing_rows = df[df.isnull().any(axis=1)]

print("\n--- Rows with Missing Values ---")
print(missing_rows)


# --------------------------------------------------
# 5. Fill Missing Age
# --------------------------------------------------

df["Age"] = df["Age"].fillna(
    df["Age"].median()
)

print("\n--- Age After Cleaning ---")
print(df["Age"])


# --------------------------------------------------
# 6. Fill Missing City
# --------------------------------------------------

df["City"] = df["City"].fillna("Unknown")

print("\n--- City After Cleaning ---")
print(df["City"])


# --------------------------------------------------
# 7. Fill Missing Purchase
# --------------------------------------------------

df["Purchase"] = df["Purchase"].fillna(0)

print("\n--- Purchase After Cleaning ---")
print(df["Purchase"])


# --------------------------------------------------
# 8. Check Missing Values Again
# --------------------------------------------------

print("\n--- Missing Values After Cleaning ---")

print(df.isnull().sum())


# --------------------------------------------------
# 9. Detect Duplicate Records
# --------------------------------------------------

duplicates = df.duplicated()

print("\n--- Duplicate Records ---")
print(df[duplicates])


# --------------------------------------------------
# 10. Remove Duplicate Records
# --------------------------------------------------

df = df.drop_duplicates()

print("\n--- After Removing Duplicates ---")
print(df)


# --------------------------------------------------
# 11. Check Duplicate Customer IDs
# --------------------------------------------------

duplicate_ids = df[
    df["Customer_ID"].duplicated()
]

print("\n--- Duplicate Customer IDs ---")
print(duplicate_ids)


# --------------------------------------------------
# 12. Standardize Text
# --------------------------------------------------

df["Name"] = df["Name"].str.strip()

df["City"] = df["City"].str.strip().str.title()

print("\n--- Standardized Text ---")
print(df)


# --------------------------------------------------
# 13. Convert Data Type
# --------------------------------------------------

df["Age"] = df["Age"].astype(int)

df["Purchase"] = df["Purchase"].astype(float)

print("\n--- Updated Data Types ---")
print(df.dtypes)


# --------------------------------------------------
# 14. Detect Invalid Values
# --------------------------------------------------

invalid_age = df[
    (df["Age"] < 0) |
    (df["Age"] > 100)
]

print("\n--- Invalid Age Records ---")
print(invalid_age)


# --------------------------------------------------
# 15. Filter Valid Records
# --------------------------------------------------

df = df[
    (df["Age"] >= 18) &
    (df["Age"] <= 100)
]

print("\n--- Valid Customer Records ---")
print(df)


# --------------------------------------------------
# 16. Create Customer Segment
# --------------------------------------------------

def customer_segment(purchase):

    if purchase >= 40000:
        return "High Value"

    elif purchase >= 20000:
        return "Medium Value"

    else:
        return "Low Value"


df["Customer_Segment"] = df["Purchase"].apply(
    customer_segment
)

print("\n--- Customer Segments ---")
print(df)


# --------------------------------------------------
# 17. Remove Unnecessary Spaces
# --------------------------------------------------

df["Name"] = df["Name"].str.strip()

print("\nNames After Cleaning:")
print(df["Name"])


# --------------------------------------------------
# 18. Replace Inconsistent Values
# --------------------------------------------------

df["City"] = df["City"].replace(
    {
        "Bangalore": "Bengaluru",
        "Bombay": "Mumbai"
    }
)

print("\n--- Standardized Cities ---")
print(df["City"])


# --------------------------------------------------
# 19. Detect Outliers Using IQR
# --------------------------------------------------

Q1 = df["Purchase"].quantile(0.25)

Q3 = df["Purchase"].quantile(0.75)

IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR

upper_limit = Q3 + 1.5 * IQR

outliers = df[
    (df["Purchase"] < lower_limit) |
    (df["Purchase"] > upper_limit)
]

print("\n--- Purchase Outliers ---")
print(outliers)


# --------------------------------------------------
# 20. Cleaning Column Names
# --------------------------------------------------

df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

print("\n--- Clean Column Names ---")
print(df.columns)


# --------------------------------------------------
# 21. Sorting Cleaned Data
# --------------------------------------------------

df = df.sort_values(
    by="purchase",
    ascending=False
)

print("\n--- Sorted Customer Data ---")
print(df)


# --------------------------------------------------
# 22. Business Summary
# --------------------------------------------------

total_customers = df["customer_id"].nunique()

total_purchase = df["purchase"].sum()

average_purchase = df["purchase"].mean()

print("\n--- Business Summary ---")

print("Unique Customers:", total_customers)

print("Total Purchase:", total_purchase)

print("Average Purchase:", average_purchase)


# --------------------------------------------------
# 23. Segment Analysis
# --------------------------------------------------

segment_summary = df.groupby(
    "customer_segment"
)["purchase"].agg(
    ["count", "sum", "mean"]
)

print("\n--- Customer Segment Analysis ---")
print(segment_summary)


# --------------------------------------------------
# 24. City Analysis
# --------------------------------------------------

city_summary = df.groupby(
    "city"
)["purchase"].sum()

print("\n--- Purchase by City ---")
print(city_summary)


# --------------------------------------------------
# 25. Save Cleaned Dataset
# --------------------------------------------------

df.to_csv(
    "cleaned_customer_data.csv",
    index=False
)

print("\nCleaned dataset saved successfully.")


# --------------------------------------------------
# 26. Mini Challenge
# --------------------------------------------------

product_data = pd.DataFrame({

    "Product": [
        "Laptop",
        "Phone",
        "Tablet",
        "Phone",
        "Laptop",
        None
    ],

    "Price": [
        75000,
        45000,
        None,
        45000,
        75000,
        30000
    ],

    "Units_Sold": [
        12,
        25,
        18,
        25,
        12,
        10
    ]
})

print("\n--- Product Dataset ---")
print(product_data)


# Handle missing product names
product_data["Product"] = product_data[
    "Product"
].fillna("Unknown")


# Handle missing prices
product_data["Price"] = product_data[
    "Price"
].fillna(
    product_data["Price"].median()
)


# Remove duplicate products
product_data = product_data.drop_duplicates()


# Create revenue column
product_data["Revenue"] = (
    product_data["Price"] *
    product_data["Units_Sold"]
)


print("\n--- Cleaned Product Dataset ---")
print(product_data)


# --------------------------------------------------
# Key Takeaway
# --------------------------------------------------

print("\nDay 17 Complete: Pandas Data Cleaning")
