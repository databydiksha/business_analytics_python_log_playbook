"""
Day 12 - Python Modules & Packages
Business Analytics Python Log Playbook

Modules allow us to organize reusable Python code into separate files.
Python also provides many built-in modules that are useful for
data analysis, calculations, dates, and automation.
"""


# --------------------------------------------------
# 1. Importing a Built-in Module
# --------------------------------------------------

import math

number = 25

print("Square Root:", math.sqrt(number))


# --------------------------------------------------
# 2. Using Constants from a Module
# --------------------------------------------------

print("\nValue of Pi:", math.pi)


# --------------------------------------------------
# 3. Using Specific Functions from a Module
# --------------------------------------------------

from math import sqrt

print("Square Root of 144:", sqrt(144))


# --------------------------------------------------
# 4. Importing Multiple Functions
# --------------------------------------------------

from math import sqrt, ceil, floor

value = 12.7

print("\n--- Math Functions ---")
print("Square Root:", sqrt(144))
print("Ceiling:", ceil(value))
print("Floor:", floor(value))


# --------------------------------------------------
# 5. Using an Alias
# --------------------------------------------------

import math as m

print("\nSquare Root using Alias:", m.sqrt(81))


# --------------------------------------------------
# 6. Random Module
# --------------------------------------------------

import random

random_number = random.randint(1, 100)

print("\nRandom Number:", random_number)


# --------------------------------------------------
# 7. Random Business Example
# --------------------------------------------------

customer_ids = ["C101", "C102", "C103", "C104", "C105"]

selected_customer = random.choice(customer_ids)

print("Selected Customer:", selected_customer)


# --------------------------------------------------
# 8. Datetime Module
# --------------------------------------------------

from datetime import datetime

current_date = datetime.now()

print("\nCurrent Date and Time:", current_date)


# --------------------------------------------------
# 9. Formatting a Date
# --------------------------------------------------

formatted_date = current_date.strftime("%d-%m-%Y")

print("Formatted Date:", formatted_date)


# --------------------------------------------------
# 10. Business Date Example
# --------------------------------------------------

order_date = datetime(2026, 8, 16)

print("\nOrder Date:", order_date.strftime("%d %B %Y"))


# --------------------------------------------------
# 11. Statistics Module
# --------------------------------------------------

import statistics

sales = [45000, 52000, 61000, 58000, 67000]

average_sales = statistics.mean(sales)
median_sales = statistics.median(sales)

print("\n--- Sales Statistics ---")
print("Average Sales:", average_sales)
print("Median Sales:", median_sales)


# --------------------------------------------------
# 12. Finding Standard Deviation
# --------------------------------------------------

standard_deviation = statistics.stdev(sales)

print("Standard Deviation:", standard_deviation)


# --------------------------------------------------
# 13. Creating a Simple Custom Module
# --------------------------------------------------

# A separate Python file can contain reusable functions.
# Example:
#
# business_calculations.py
#
# def calculate_profit(revenue, expenses):
#     return revenue - expenses
#
# It can then be imported using:
#
# from business_calculations import calculate_profit


# --------------------------------------------------
# 14. Simulating a Reusable Function
# --------------------------------------------------

def calculate_profit(revenue, expenses):

    return revenue - expenses


revenue = 150000
expenses = 95000

profit = calculate_profit(revenue, expenses)

print("\n--- Business Calculation ---")
print("Revenue:", revenue)
print("Expenses:", expenses)
print("Profit:", profit)


# --------------------------------------------------
# 15. Using the os Module
# --------------------------------------------------

import os

current_directory = os.getcwd()

print("\nCurrent Working Directory:")
print(current_directory)


# --------------------------------------------------
# 16. Checking Whether a File Exists
# --------------------------------------------------

file_name = "sales_data.txt"

if os.path.exists(file_name):
    print("\nFile exists:", file_name)
else:
    print("\nFile does not exist:", file_name)


# --------------------------------------------------
# 17. Combining Multiple Modules
# --------------------------------------------------

import math
import statistics
import random

sales = [42000, 48000, 55000, 62000, 70000]

average = statistics.mean(sales)
highest = max(sales)
growth_factor = math.sqrt(highest)

print("\n--- Combined Module Example ---")
print("Average Sales:", average)
print("Highest Sales:", highest)
print("Growth Factor:", growth_factor)


# --------------------------------------------------
# 18. Mini Challenge
# --------------------------------------------------

monthly_revenue = [45000, 52000, 61000, 58000, 67000]

average_revenue = statistics.mean(monthly_revenue)
median_revenue = statistics.median(monthly_revenue)
standard_deviation = statistics.stdev(monthly_revenue)

print("\n--- Revenue Analysis ---")
print("Average Revenue:", average_revenue)
print("Median Revenue:", median_revenue)
print("Standard Deviation:", standard_deviation)


# --------------------------------------------------
# Key Takeaway
# --------------------------------------------------

print("\nDay 12 Complete: Python Modules & Packages")
