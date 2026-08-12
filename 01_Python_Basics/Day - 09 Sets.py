"""
Day 09 - Python Sets
Business Analytics Python Log Playbook

Sets are unordered collections of unique elements.
They are especially useful for removing duplicates
and performing comparisons between groups of data.
"""


# --------------------------------------------------
# 1. Creating a Set
# --------------------------------------------------

customers = {"C101", "C102", "C103", "C104"}

print("Customer IDs:")
print(customers)


# --------------------------------------------------
# 2. Duplicate Values
# --------------------------------------------------

customer_ids = {
    "C101",
    "C102",
    "C103",
    "C101",
    "C102"
}

print("\nUnique Customer IDs:")
print(customer_ids)


# --------------------------------------------------
# 3. Adding an Element
# --------------------------------------------------

customer_ids.add("C105")

print("\nAfter Adding C105:")
print(customer_ids)


# --------------------------------------------------
# 4. Adding Multiple Elements
# --------------------------------------------------

customer_ids.update(["C106", "C107"])

print("\nAfter Adding Multiple Customers:")
print(customer_ids)


# --------------------------------------------------
# 5. Removing an Element
# --------------------------------------------------

customer_ids.remove("C107")

print("\nAfter Removing C107:")
print(customer_ids)


# --------------------------------------------------
# 6. Discarding an Element
# --------------------------------------------------

customer_ids.discard("C999")

print("\nAfter Using discard():")
print(customer_ids)


# --------------------------------------------------
# 7. Checking Membership
# --------------------------------------------------

if "C103" in customer_ids:
    print("\nC103 is an existing customer.")


# --------------------------------------------------
# 8. Set Union
# --------------------------------------------------

online_customers = {"C101", "C102", "C103", "C104"}
store_customers = {"C103", "C104", "C105", "C106"}

all_customers = online_customers.union(store_customers)

print("\nAll Customers:")
print(all_customers)


# --------------------------------------------------
# 9. Set Intersection
# --------------------------------------------------

common_customers = online_customers.intersection(store_customers)

print("\nCustomers Using Both Channels:")
print(common_customers)


# --------------------------------------------------
# 10. Set Difference
# --------------------------------------------------

online_only = online_customers.difference(store_customers)

print("\nOnline-Only Customers:")
print(online_only)


# --------------------------------------------------
# 11. Symmetric Difference
# --------------------------------------------------

exclusive_customers = online_customers.symmetric_difference(
    store_customers
)

print("\nCustomers Present in Only One Channel:")
print(exclusive_customers)


# --------------------------------------------------
# 12. Number of Unique Customers
# --------------------------------------------------

print("\nTotal Unique Customers:", len(all_customers))


# --------------------------------------------------
# 13. Converting a List into a Set
# --------------------------------------------------

sales_regions = [
    "North",
    "South",
    "North",
    "West",
    "South",
    "East"
]

unique_regions = set(sales_regions)

print("\nUnique Sales Regions:")
print(unique_regions)


# --------------------------------------------------
# 14. Practical Business Example
# --------------------------------------------------

january_customers = {
    "A101",
    "A102",
    "A103",
    "A104",
    "A105"
}

february_customers = {
    "A103",
    "A104",
    "A105",
    "A106",
    "A107"
}

returning_customers = january_customers.intersection(
    february_customers
)

new_customers = february_customers.difference(
    january_customers
)

print("\n--- Customer Analysis ---")
print("Returning Customers:", returning_customers)
print("New Customers:", new_customers)


# --------------------------------------------------
# 15. Set Comparisons
# --------------------------------------------------

required_skills = {
    "Python",
    "SQL",
    "Power BI",
    "Excel"
}

my_skills = {
    "Python",
    "SQL",
    "Power BI",
    "Excel",
    "Tableau"
}

missing_skills = required_skills.difference(my_skills)

additional_skills = my_skills.difference(required_skills)

print("\n--- Skill Analysis ---")
print("Missing Skills:", missing_skills)
print("Additional Skills:", additional_skills)


# --------------------------------------------------
# 16. Mini Challenge
# --------------------------------------------------

website_visitors = {
    "U101",
    "U102",
    "U103",
    "U104",
    "U105"
}

purchase_users = {
    "U102",
    "U103",
    "U105"
}

non_purchasing_users = website_visitors.difference(
    purchase_users
)

print("\n--- Website Conversion Analysis ---")
print("Total Visitors:", len(website_visitors))
print("Purchasers:", len(purchase_users))
print("Non-Purchasers:", len(non_purchasing_users))
print("Non-Purchasing Users:", non_purchasing_users)


# --------------------------------------------------
# Key Takeaway
# --------------------------------------------------

print("\nDay 09 Complete: Python Sets")
