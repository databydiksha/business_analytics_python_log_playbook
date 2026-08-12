"""
Day 08 - Python Dictionaries
Business Analytics Python Log Playbook

Dictionaries store data in key-value pairs.
They are useful for representing structured information
such as customer records, products, employees, and KPIs.
"""


# --------------------------------------------------
# 1. Creating a Dictionary
# --------------------------------------------------

student = {
    "name": "Diksha",
    "course": "MBA Business Analytics",
    "age": 22,
    "location": "Bhopal"
}

print("Student Information:")
print(student)


# --------------------------------------------------
# 2. Accessing Values
# --------------------------------------------------

print("\nName:", student["name"])
print("Course:", student["course"])


# --------------------------------------------------
# 3. Using get()
# --------------------------------------------------

print("\nAge:", student.get("age"))
print("Email:", student.get("email", "Not Available"))


# --------------------------------------------------
# 4. Adding a New Key-Value Pair
# --------------------------------------------------

student["skills"] = "Python, SQL, Power BI"

print("\nAfter Adding Skills:")
print(student)


# --------------------------------------------------
# 5. Updating a Value
# --------------------------------------------------

student["age"] = 23

print("\nUpdated Age:", student["age"])


# --------------------------------------------------
# 6. Updating Multiple Values
# --------------------------------------------------

student.update({
    "location": "Bengaluru",
    "status": "Student"
})

print("\nUpdated Student Information:")
print(student)


# --------------------------------------------------
# 7. Removing an Item
# --------------------------------------------------

student.pop("status")

print("\nAfter Removing Status:")
print(student)


# --------------------------------------------------
# 8. Dictionary Keys
# --------------------------------------------------

print("\nKeys:")

for key in student.keys():
    print(key)


# --------------------------------------------------
# 9. Dictionary Values
# --------------------------------------------------

print("\nValues:")

for value in student.values():
    print(value)


# --------------------------------------------------
# 10. Dictionary Items
# --------------------------------------------------

print("\nKey-Value Pairs:")

for key, value in student.items():
    print(key, ":", value)


# --------------------------------------------------
# 11. Business Example - Customer Record
# --------------------------------------------------

customer = {
    "customer_id": 101,
    "name": "Rahul",
    "age": 28,
    "city": "Mumbai",
    "purchase_amount": 12500,
    "payment_method": "Credit Card"
}

print("\n--- Customer Profile ---")

for key, value in customer.items():
    print(key, ":", value)


# --------------------------------------------------
# 12. Business Example - Sales Data
# --------------------------------------------------

sales = {
    "January": 45000,
    "February": 52000,
    "March": 61000,
    "April": 58000,
    "May": 67000
}

print("\n--- Monthly Sales ---")

for month, revenue in sales.items():
    print(month, ":", revenue)


# --------------------------------------------------
# 13. Calculate Total Sales
# --------------------------------------------------

total_sales = sum(sales.values())
average_sales = total_sales / len(sales)

print("\nTotal Sales:", total_sales)
print("Average Monthly Sales:", average_sales)


# --------------------------------------------------
# 14. Find Highest Sales Month
# --------------------------------------------------

best_month = max(sales, key=sales.get)

print("Best Performing Month:", best_month)
print("Revenue:", sales[best_month])


# --------------------------------------------------
# 15. Nested Dictionary
# --------------------------------------------------

employees = {
    "E001": {
        "name": "Aarav",
        "department": "Finance",
        "salary": 55000
    },
    "E002": {
        "name": "Meera",
        "department": "Analytics",
        "salary": 65000
    },
    "E003": {
        "name": "Rohan",
        "department": "Marketing",
        "salary": 58000
    }
}

print("\n--- Employee Records ---")

for employee_id, details in employees.items():

    print("\nEmployee ID:", employee_id)

    for key, value in details.items():
        print(key, ":", value)


# --------------------------------------------------
# 16. Dictionary Comprehension
# --------------------------------------------------

numbers = [1, 2, 3, 4, 5]

squares = {
    number: number ** 2
    for number in numbers
}

print("\n--- Number and Square ---")
print(squares)


# --------------------------------------------------
# 17. Practical Business Example
# --------------------------------------------------

products = {
    "Laptop": 75000,
    "Smartphone": 45000,
    "Tablet": 30000,
    "Headphones": 8000
}

print("\n--- Product Prices ---")

for product, price in products.items():

    if price > 40000:
        category = "Premium"
    else:
        category = "Standard"

    print(product, ":", price, "| Category:", category)


# --------------------------------------------------
# 18. Mini Challenge
# --------------------------------------------------

expenses = {
    "Rent": 25000,
    "Electricity": 5000,
    "Marketing": 12000,
    "Software": 8000,
    "Travel": 7000
}

total_expenses = sum(expenses.values())

highest_expense = max(expenses, key=expenses.get)

print("\n--- Expense Analysis ---")
print("Total Expenses:", total_expenses)
print("Highest Expense:", highest_expense)
print("Amount:", expenses[highest_expense])


# --------------------------------------------------
# Key Takeaway
# --------------------------------------------------

print("\nDay 08 Complete: Python Dictionaries")
