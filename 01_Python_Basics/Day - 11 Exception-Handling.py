"""
Day 10 - Python File Handling
Business Analytics Python Log Playbook

File handling allows Python programs to create, read, write,
and modify files. It is an important skill for working with
datasets and automating data-processing tasks.
"""


# --------------------------------------------------
# 1. Creating and Writing to a File
# --------------------------------------------------

file = open("sales_data.txt", "w")

file.write("January,45000\n")
file.write("February,52000\n")
file.write("March,61000\n")

file.close()

print("File created and data written successfully.")


# --------------------------------------------------
# 2. Reading a File
# --------------------------------------------------

file = open("sales_data.txt", "r")

content = file.read()

file.close()

print("\n--- File Content ---")
print(content)


# --------------------------------------------------
# 3. Reading Line by Line
# --------------------------------------------------

file = open("sales_data.txt", "r")

print("--- Reading Line by Line ---")

for line in file:
    print(line.strip())

file.close()


# --------------------------------------------------
# 4. Using with Statement
# --------------------------------------------------

with open("sales_data.txt", "r") as file:

    content = file.read()

print("\n--- Using with Statement ---")
print(content)


# --------------------------------------------------
# 5. Reading Individual Lines
# --------------------------------------------------

with open("sales_data.txt", "r") as file:

    lines = file.readlines()

print("\n--- Individual Lines ---")

for line in lines:
    print(line.strip())


# --------------------------------------------------
# 6. Appending Data
# --------------------------------------------------

with open("sales_data.txt", "a") as file:

    file.write("April,58000\n")

print("\nNew sales record added successfully.")


# --------------------------------------------------
# 7. Checking Whether a File Exists
# --------------------------------------------------

import os

if os.path.exists("sales_data.txt"):
    print("\nThe sales data file exists.")
else:
    print("\nThe file does not exist.")


# --------------------------------------------------
# 8. File Information
# --------------------------------------------------

file_size = os.path.getsize("sales_data.txt")

print("File Size:", file_size, "bytes")


# --------------------------------------------------
# 9. Processing File Data
# --------------------------------------------------

with open("sales_data.txt", "r") as file:

    total_sales = 0

    for line in file:

        month, sales = line.strip().split(",")

        total_sales += int(sales)

print("\n--- Sales Analysis ---")
print("Total Sales:", total_sales)


# --------------------------------------------------
# 10. Calculating Average Sales
# --------------------------------------------------

with open("sales_data.txt", "r") as file:

    sales_values = []

    for line in file:

        month, sales = line.strip().split(",")

        sales_values.append(int(sales))

average_sales = sum(sales_values) / len(sales_values)

print("Average Monthly Sales:", average_sales)


# --------------------------------------------------
# 11. Finding the Highest Sales
# --------------------------------------------------

with open("sales_data.txt", "r") as file:

    sales_data = {}

    for line in file:

        month, sales = line.strip().split(",")

        sales_data[month] = int(sales)

best_month = max(sales_data, key=sales_data.get)

print("Best Performing Month:", best_month)
print("Sales:", sales_data[best_month])


# --------------------------------------------------
# 12. Creating a Customer File
# --------------------------------------------------

with open("customers.txt", "w") as file:

    file.write("C101,Diksha,Bhopal\n")
    file.write("C102,Aarav,Mumbai\n")
    file.write("C103,Meera,Delhi\n")

print("\nCustomer file created successfully.")


# --------------------------------------------------
# 13. Reading Customer Records
# --------------------------------------------------

with open("customers.txt", "r") as file:

    print("\n--- Customer Records ---")

    for line in file:

        customer_id, name, city = line.strip().split(",")

        print(
            "ID:", customer_id,
            "| Name:", name,
            "| City:", city
        )


# --------------------------------------------------
# 14. Mini Challenge
# --------------------------------------------------

with open("expenses.txt", "w") as file:

    file.write("Rent,25000\n")
    file.write("Electricity,5000\n")
    file.write("Marketing,12000\n")
    file.write("Travel,7000\n")


total_expenses = 0

with open("expenses.txt", "r") as file:

    for line in file:

        category, amount = line.strip().split(",")

        total_expenses += int(amount)


print("\n--- Expense Analysis ---")
print("Total Expenses:", total_expenses)


# --------------------------------------------------
# Key Takeaway
# --------------------------------------------------

print("\nDay 10 Complete: Python File Handling")
