"""
Day 15 - NumPy Basics
Business Analytics Python Log Playbook

NumPy is a Python library used for numerical computing.
It provides powerful arrays and mathematical operations
that are useful for data analysis and machine learning.
"""

import numpy as np


# --------------------------------------------------
# 1. Creating a NumPy Array
# --------------------------------------------------

sales = np.array([45000, 52000, 61000, 58000, 67000])

print("Sales Array:")
print(sales)


# --------------------------------------------------
# 2. Checking Array Type
# --------------------------------------------------

print("\nArray Type:")
print(type(sales))


# --------------------------------------------------
# 3. Array Shape
# --------------------------------------------------

print("\nArray Shape:")
print(sales.shape)


# --------------------------------------------------
# 4. Number of Elements
# --------------------------------------------------

print("\nNumber of Elements:")
print(sales.size)


# --------------------------------------------------
# 5. Data Type
# --------------------------------------------------

print("\nData Type:")
print(sales.dtype)


# --------------------------------------------------
# 6. Accessing Array Elements
# --------------------------------------------------

print("\nFirst Sale:", sales[0])
print("Last Sale:", sales[-1])


# --------------------------------------------------
# 7. Array Slicing
# --------------------------------------------------

print("\nFirst Three Sales:")
print(sales[:3])


# --------------------------------------------------
# 8. Mathematical Operations
# --------------------------------------------------

print("\n--- Mathematical Operations ---")

print("Sales + 1000:")
print(sales + 1000)

print("\nSales - 1000:")
print(sales - 1000)

print("\nSales * 2:")
print(sales * 2)

print("\nSales / 2:")
print(sales / 2)


# --------------------------------------------------
# 9. NumPy Statistical Functions
# --------------------------------------------------

print("\n--- Sales Statistics ---")

print("Total:", np.sum(sales))
print("Average:", np.mean(sales))
print("Median:", np.median(sales))
print("Maximum:", np.max(sales))
print("Minimum:", np.min(sales))


# --------------------------------------------------
# 10. Standard Deviation
# --------------------------------------------------

standard_deviation = np.std(sales)

print("\nStandard Deviation:", standard_deviation)


# --------------------------------------------------
# 11. Reshaping an Array
# --------------------------------------------------

monthly_sales = np.array([
    45000, 52000, 61000,
    58000, 67000, 72000
])

sales_matrix = monthly_sales.reshape(2, 3)

print("\n--- Reshaped Sales Array ---")
print(sales_matrix)


# --------------------------------------------------
# 12. Two-Dimensional Array
# --------------------------------------------------

business_data = np.array([
    [45000, 28000],
    [52000, 31000],
    [61000, 35000],
    [58000, 33000]
])

print("\n--- Business Data ---")
print(business_data)


# --------------------------------------------------
# 13. Accessing Rows and Columns
# --------------------------------------------------

print("\nFirst Row:")
print(business_data[0])

print("\nFirst Column:")
print(business_data[:, 0])


# --------------------------------------------------
# 14. Row and Column Statistics
# --------------------------------------------------

print("\nColumn Totals:")
print(np.sum(business_data, axis=0))

print("\nRow Totals:")
print(np.sum(business_data, axis=1))


# --------------------------------------------------
# 15. Creating Arrays with zeros()
# --------------------------------------------------

zero_array = np.zeros(5)

print("\nArray of Zeros:")
print(zero_array)


# --------------------------------------------------
# 16. Creating Arrays with ones()
# --------------------------------------------------

one_array = np.ones(5)

print("\nArray of Ones:")
print(one_array)


# --------------------------------------------------
# 17. Creating a Range of Numbers
# --------------------------------------------------

numbers = np.arange(1, 11)

print("\nNumbers from 1 to 10:")
print(numbers)


# --------------------------------------------------
# 18. Creating Even Numbers
# --------------------------------------------------

even_numbers = np.arange(2, 21, 2)

print("\nEven Numbers:")
print(even_numbers)


# --------------------------------------------------
# 19. Filtering Data
# --------------------------------------------------

high_sales = sales[sales > 55000]

print("\n--- High Sales ---")
print(high_sales)


# --------------------------------------------------
# 20. Business Example - Profit Calculation
# --------------------------------------------------

revenue = np.array([
    45000,
    52000,
    61000,
    58000,
    67000
])

expenses = np.array([
    28000,
    31000,
    35000,
    33000,
    39000
])

profit = revenue - expenses

print("\n--- Profit Analysis ---")
print("Revenue:", revenue)
print("Expenses:", expenses)
print("Profit:", profit)


# --------------------------------------------------
# 21. Profit Margin
# --------------------------------------------------

profit_margin = (profit / revenue) * 100

print("\nProfit Margin:")
print(profit_margin)


# --------------------------------------------------
# 22. Finding Highest Profit
# --------------------------------------------------

highest_profit = np.max(profit)
highest_profit_index = np.argmax(profit)

print("\nHighest Profit:", highest_profit)
print("Month Index:", highest_profit_index)


# --------------------------------------------------
# 23. Random Data
# --------------------------------------------------

random_sales = np.random.randint(
    10000,
    50000,
    size=5
)

print("\nRandom Sales Data:")
print(random_sales)


# --------------------------------------------------
# 24. Mini Challenge
# --------------------------------------------------

customer_spending = np.array([
    12000,
    25000,
    18000,
    45000,
    32000,
    55000
])

high_value_customers = customer_spending[
    customer_spending >= 30000
]

average_spending = np.mean(customer_spending)

print("\n--- Customer Spending Analysis ---")
print("Customer Spending:", customer_spending)
print("High-Value Spending:", high_value_customers)
print("Average Spending:", average_spending)


# --------------------------------------------------
# Key Takeaway
# --------------------------------------------------

print("\nDay 15 Complete: NumPy Basics")
