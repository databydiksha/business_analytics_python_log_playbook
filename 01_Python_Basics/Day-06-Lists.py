"""
Day 06 - Python Lists
Business Analytics Python Log Playbook

Lists are one of the most commonly used data structures in Python.
They allow us to store multiple values in a single variable.
"""

# --------------------------------------------------
# 1. Creating a List
# --------------------------------------------------

sales = [12000, 18500, 14300, 21000, 17500]

print("Sales Data:")
print(sales)


# --------------------------------------------------
# 2. Accessing List Elements
# --------------------------------------------------

print("\nFirst Sale:", sales[0])
print("Last Sale:", sales[-1])


# --------------------------------------------------
# 3. Adding Elements
# --------------------------------------------------

sales.append(23000)

print("\nAfter Adding New Sale:")
print(sales)


# --------------------------------------------------
# 4. Inserting Elements
# --------------------------------------------------

sales.insert(2, 16000)

print("\nAfter Inserting Sale:")
print(sales)


# --------------------------------------------------
# 5. Removing Elements
# --------------------------------------------------

sales.remove(12000)

print("\nAfter Removing Sale:")
print(sales)


# --------------------------------------------------
# 6. Finding Length
# --------------------------------------------------

print("\nNumber of Sales Records:", len(sales))


# --------------------------------------------------
# 7. Sorting a List
# --------------------------------------------------

sales.sort()

print("\nSorted Sales:")
print(sales)


# --------------------------------------------------
# 8. Finding Maximum and Minimum
# --------------------------------------------------

print("\nHighest Sale:", max(sales))
print("Lowest Sale:", min(sales))


# --------------------------------------------------
# 9. Calculating Total and Average
# --------------------------------------------------

total_sales = sum(sales)
average_sales = total_sales / len(sales)

print("\nTotal Sales:", total_sales)
print("Average Sales:", average_sales)


# --------------------------------------------------
# 10. Looping Through a List
# --------------------------------------------------

print("\nSales Records:")

for sale in sales:
    print(sale)


# --------------------------------------------------
# 11. List Comprehension
# --------------------------------------------------

high_value_sales = [sale for sale in sales if sale > 18000]

print("\nHigh-Value Sales:")
print(high_value_sales)


# --------------------------------------------------
# 12. Practical Business Example
# --------------------------------------------------

monthly_sales = [45000, 52000, 48000, 61000, 57000, 68000]

best_month = max(monthly_sales)
worst_month = min(monthly_sales)
average_monthly_sales = sum(monthly_sales) / len(monthly_sales)

print("\n--- Monthly Sales Analysis ---")
print("Best Monthly Sales:", best_month)
print("Lowest Monthly Sales:", worst_month)
print("Average Monthly Sales:", average_monthly_sales)


# --------------------------------------------------
# 13. Mini Challenge
# --------------------------------------------------

expenses = [12000, 8500, 15000, 9200, 11000]

total_expenses = sum(expenses)
average_expense = total_expenses / len(expenses)

print("\n--- Expense Analysis ---")
print("Total Expenses:", total_expenses)
print("Average Expense:", average_expense)
print("Highest Expense:", max(expenses))
print("Lowest Expense:", min(expenses))


# --------------------------------------------------
# Key Takeaway
# --------------------------------------------------

print("\nDay 06 Complete: Python Lists")
