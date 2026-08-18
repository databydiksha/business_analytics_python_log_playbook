"""
Day 14 - Working with CSV Files
Business Analytics Python Log Playbook

CSV (Comma-Separated Values) files are commonly used to store
tabular data such as sales, customers, transactions, and expenses.

Python's csv module allows us to create, read, and process CSV data.
"""

import csv


# --------------------------------------------------
# 1. Creating a CSV File
# --------------------------------------------------

sales_data = [
    ["Month", "Revenue", "Expenses"],
    ["January", 45000, 28000],
    ["February", 52000, 31000],
    ["March", 61000, 35000],
    ["April", 58000, 33000],
    ["May", 67000, 39000]
]

with open("sales_data.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerows(sales_data)

print("CSV file created successfully.")


# --------------------------------------------------
# 2. Reading a CSV File
# --------------------------------------------------

with open("sales_data.csv", "r") as file:

    reader = csv.reader(file)

    print("\n--- Sales Data ---")

    for row in reader:
        print(row)


# --------------------------------------------------
# 3. Reading CSV Using DictReader
# --------------------------------------------------

with open("sales_data.csv", "r") as file:

    reader = csv.DictReader(file)

    print("\n--- Dictionary Format ---")

    for row in reader:
        print(row)


# --------------------------------------------------
# 4. Accessing Specific Columns
# --------------------------------------------------

with open("sales_data.csv", "r") as file:

    reader = csv.DictReader(file)

    print("\n--- Monthly Revenue ---")

    for row in reader:
        print(row["Month"], ":", row["Revenue"])


# --------------------------------------------------
# 5. Calculating Total Revenue
# --------------------------------------------------

total_revenue = 0

with open("sales_data.csv", "r") as file:

    reader = csv.DictReader(file)

    for row in reader:

        revenue = int(row["Revenue"])

        total_revenue += revenue


print("\nTotal Revenue:", total_revenue)


# --------------------------------------------------
# 6. Calculating Total Expenses
# --------------------------------------------------

total_expenses = 0

with open("sales_data.csv", "r") as file:

    reader = csv.DictReader(file)

    for row in reader:

        expenses = int(row["Expenses"])

        total_expenses += expenses


print("Total Expenses:", total_expenses)


# --------------------------------------------------
# 7. Calculating Profit
# --------------------------------------------------

profit = total_revenue - total_expenses

print("Total Profit:", profit)


# --------------------------------------------------
# 8. Calculating Average Revenue
# --------------------------------------------------

with open("sales_data.csv", "r") as file:

    reader = csv.DictReader(file)

    revenues = []

    for row in reader:

        revenues.append(int(row["Revenue"]))


average_revenue = sum(revenues) / len(revenues)

print("Average Revenue:", average_revenue)


# --------------------------------------------------
# 9. Finding the Best Performing Month
# --------------------------------------------------

with open("sales_data.csv", "r") as file:

    reader = csv.DictReader(file)

    best_month = None
    highest_revenue = 0

    for row in reader:

        revenue = int(row["Revenue"])

        if revenue > highest_revenue:

            highest_revenue = revenue
            best_month = row["Month"]


print("\n--- Best Performing Month ---")
print("Month:", best_month)
print("Revenue:", highest_revenue)


# --------------------------------------------------
# 10. Creating a Customer CSV
# --------------------------------------------------

customers = [
    ["Customer_ID", "Name", "City", "Purchase"],
    ["C101", "Aarav", "Mumbai", 25000],
    ["C102", "Meera", "Delhi", 42000],
    ["C103", "Rohan", "Pune", 18000],
    ["C104", "Ananya", "Bengaluru", 55000]
]

with open("customers.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerows(customers)


print("\nCustomer CSV created successfully.")


# --------------------------------------------------
# 11. Customer Purchase Analysis
# --------------------------------------------------

with open("customers.csv", "r") as file:

    reader = csv.DictReader(file)

    print("\n--- Customer Purchases ---")

    for row in reader:

        print(
            row["Customer_ID"],
            "|",
            row["Name"],
            "|",
            row["City"],
            "| Purchase:",
            row["Purchase"]
        )


# --------------------------------------------------
# 12. Finding High-Value Customers
# --------------------------------------------------

with open("customers.csv", "r") as file:

    reader = csv.DictReader(file)

    high_value_customers = []

    for row in reader:

        purchase = int(row["Purchase"])

        if purchase >= 40000:

            high_value_customers.append(row["Name"])


print("\n--- High-Value Customers ---")

for customer in high_value_customers:
    print(customer)


# --------------------------------------------------
# 13. Counting Customers
# --------------------------------------------------

with open("customers.csv", "r") as file:

    reader = csv.DictReader(file)

    customer_count = sum(1 for row in reader)


print("\nTotal Customers:", customer_count)


# --------------------------------------------------
# 14. Calculating Customer Revenue
# --------------------------------------------------

with open("customers.csv", "r") as file:

    reader = csv.DictReader(file)

    customer_revenue = 0

    for row in reader:

        customer_revenue += int(row["Purchase"])


print("Total Customer Revenue:", customer_revenue)


# --------------------------------------------------
# 15. Creating a Filtered CSV
# --------------------------------------------------

with open("customers.csv", "r") as input_file:

    reader = csv.DictReader(input_file)

    with open(
        "high_value_customers.csv",
        "w",
        newline=""
    ) as output_file:

        fieldnames = [
            "Customer_ID",
            "Name",
            "City",
            "Purchase"
        ]

        writer = csv.DictWriter(
            output_file,
            fieldnames=fieldnames
        )

        writer.writeheader()

        for row in reader:

            if int(row["Purchase"]) >= 40000:
                writer.writerow(row)


print("\nHigh-value customer CSV created.")


# --------------------------------------------------
# 16. Handling Missing or Invalid Data
# --------------------------------------------------

customer_data = [
    ["Customer_ID", "Name", "Purchase"],
    ["C105", "Kabir", "35000"],
    ["C106", "Isha", ""],
    ["C107", "Arjun", "Invalid"]
]

with open("customer_quality.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerows(customer_data)


print("\nCustomer quality dataset created.")


# --------------------------------------------------
# 17. Data Validation
# --------------------------------------------------

with open("customer_quality.csv", "r") as file:

    reader = csv.DictReader(file)

    valid_records = []

    for row in reader:

        try:

            purchase = float(row["Purchase"])

            if purchase >= 0:
                valid_records.append(row)

        except ValueError:

            print(
                "Invalid purchase value:",
                row["Purchase"]
            )


print("\nValid Records:", len(valid_records))


# --------------------------------------------------
# 18. Mini Challenge
# --------------------------------------------------

expenses = [
    ["Category", "Amount"],
    ["Rent", 25000],
    ["Electricity", 5000],
    ["Marketing", 12000],
    ["Travel", 7000],
    ["Software", 8000]
]

with open("expenses.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerows(expenses)


total_expenses = 0

with open("expenses.csv", "r") as file:

    reader = csv.DictReader(file)

    for row in reader:

        total_expenses += int(row["Amount"])


print("\n--- Expense Analysis ---")
print("Total Expenses:", total_expenses)


# --------------------------------------------------
# Key Takeaway
# --------------------------------------------------

print("\nDay 14 Complete: Working with CSV Files")
