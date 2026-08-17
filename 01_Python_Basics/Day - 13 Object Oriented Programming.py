"""
Day 13 - Object-Oriented Programming (OOP)
Business Analytics Python Log Playbook

Object-Oriented Programming allows us to organize code using
classes and objects.

OOP is useful for building structured, reusable, and scalable
Python applications.
"""


# --------------------------------------------------
# 1. Creating a Class
# --------------------------------------------------

class Student:

    def display(self):
        print("MBA Business Analytics Student")


student = Student()

student.display()


# --------------------------------------------------
# 2. Class with Attributes
# --------------------------------------------------

class Customer:

    def __init__(self, name, city, age):
        self.name = name
        self.city = city
        self.age = age

    def display_details(self):
        print("Name:", self.name)
        print("City:", self.city)
        print("Age:", self.age)


customer = Customer("Diksha", "Bhopal", 22)

print("\n--- Customer Details ---")
customer.display_details()


# --------------------------------------------------
# 3. Multiple Objects
# --------------------------------------------------

customer1 = Customer("Aarav", "Mumbai", 28)
customer2 = Customer("Meera", "Delhi", 25)
customer3 = Customer("Rohan", "Pune", 30)

print("\n--- Customers ---")

customer1.display_details()

print()

customer2.display_details()

print()

customer3.display_details()


# --------------------------------------------------
# 4. Product Class
# --------------------------------------------------

class Product:

    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def display_product(self):
        print("Product:", self.name)
        print("Price:", self.price)
        print("Category:", self.category)


product1 = Product("Laptop", 75000, "Electronics")

print("\n--- Product Information ---")

product1.display_product()


# --------------------------------------------------
# 5. Methods with Calculations
# --------------------------------------------------

class Sales:

    def __init__(self, revenue, expenses):
        self.revenue = revenue
        self.expenses = expenses

    def calculate_profit(self):
        return self.revenue - self.expenses

    def calculate_margin(self):

        profit = self.calculate_profit()

        return (profit / self.revenue) * 100


sales = Sales(150000, 95000)

print("\n--- Sales Analysis ---")

print("Revenue:", sales.revenue)
print("Expenses:", sales.expenses)
print("Profit:", sales.calculate_profit())
print("Profit Margin:", sales.calculate_margin(), "%")


# --------------------------------------------------
# 6. Updating Object Attributes
# --------------------------------------------------

customer1.age = 29

print("\nUpdated Customer Age:", customer1.age)


# --------------------------------------------------
# 7. Encapsulation
# --------------------------------------------------

class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):

        if amount > 0:
            self.__balance += amount

        return self.__balance


account = BankAccount(50000)

print("\n--- Bank Account ---")
print("Initial Balance:", account.get_balance())

account.deposit(10000)

print("Updated Balance:", account.get_balance())


# --------------------------------------------------
# 8. Inheritance
# --------------------------------------------------

class Employee:

    def __init__(self, name, department):
        self.name = name
        self.department = department

    def display_employee(self):
        print("Name:", self.name)
        print("Department:", self.department)


class DataAnalyst(Employee):

    def show_role(self):
        print("Role: Data Analyst")


analyst = DataAnalyst("Diksha", "Analytics")

print("\n--- Employee Profile ---")

analyst.display_employee()
analyst.show_role()


# --------------------------------------------------
# 9. Method Overriding
# --------------------------------------------------

class Manager:

    def work(self):
        print("Manager is managing the team.")


class AnalyticsManager(Manager):

    def work(self):
        print("Analytics Manager is managing data-driven decisions.")


manager = AnalyticsManager()

print("\n--- Method Overriding ---")

manager.work()


# --------------------------------------------------
# 10. Practical Customer Analysis
# --------------------------------------------------

class CustomerPurchase:

    def __init__(self, customer_id, purchase_amount):
        self.customer_id = customer_id
        self.purchase_amount = purchase_amount

    def customer_category(self):

        if self.purchase_amount >= 50000:
            return "High Value"

        elif self.purchase_amount >= 20000:
            return "Medium Value"

        else:
            return "Low Value"


customers = [
    CustomerPurchase("C101", 75000),
    CustomerPurchase("C102", 35000),
    CustomerPurchase("C103", 12000),
    CustomerPurchase("C104", 62000)
]

print("\n--- Customer Segmentation ---")

for customer in customers:

    print(
        customer.customer_id,
        "| Purchase:",
        customer.purchase_amount,
        "| Segment:",
        customer.customer_category()
    )


# --------------------------------------------------
# 11. Total Customer Revenue
# --------------------------------------------------

total_revenue = sum(
    customer.purchase_amount
    for customer in customers
)

average_revenue = total_revenue / len(customers)

print("\n--- Revenue Summary ---")
print("Total Revenue:", total_revenue)
print("Average Customer Revenue:", average_revenue)


# --------------------------------------------------
# 12. Mini Challenge
# --------------------------------------------------

class EmployeeSalary:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def annual_salary(self):
        return self.salary * 12

    def salary_category(self):

        if self.salary >= 80000:
            return "High"

        elif self.salary >= 50000:
            return "Medium"

        else:
            return "Entry Level"


employees = [
    EmployeeSalary("Aarav", 65000),
    EmployeeSalary("Meera", 85000),
    EmployeeSalary("Rohan", 45000)
]

print("\n--- Employee Salary Analysis ---")

for employee in employees:

    print(
        employee.name,
        "| Monthly Salary:",
        employee.salary,
        "| Annual Salary:",
        employee.annual_salary(),
        "| Category:",
        employee.salary_category()
    )


# --------------------------------------------------
# Key Takeaway
# --------------------------------------------------

print("\nDay 13 Complete: Object-Oriented Programming")
