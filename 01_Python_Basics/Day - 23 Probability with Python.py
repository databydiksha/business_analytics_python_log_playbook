"""
Day 23 - Probability with Python
Business Analytics Python Log Playbook

Probability helps analysts measure the likelihood of
events and make decisions under uncertainty.

Topics:
- Basic Probability
- Complement Probability
- Conditional Probability
- Independent Events
- Joint Probability
- Business Applications
"""

import pandas as pd
import numpy as np


# --------------------------------------------------
# 1. Basic Probability
# --------------------------------------------------

total_customers = 1000

customers_purchased = 250

probability_purchase = (
    customers_purchased / total_customers
)

print("--- Basic Probability ---")

print(
    "Probability of Purchase:",
    probability_purchase
)

print(
    "Probability Percentage:",
    probability_purchase * 100,
    "%"
)


# --------------------------------------------------
# 2. Complement Probability
# --------------------------------------------------

probability_no_purchase = (
    1 - probability_purchase
)

print("\n--- Complement Probability ---")

print(
    "Probability of No Purchase:",
    probability_no_purchase
)

print(
    "Percentage:",
    probability_no_purchase * 100,
    "%"
)


# --------------------------------------------------
# 3. Dice Probability
# --------------------------------------------------

total_outcomes = 6

favorable_outcomes = 1

probability_six = (
    favorable_outcomes / total_outcomes
)

print("\n--- Dice Example ---")

print(
    "Probability of rolling a 6:",
    probability_six
)


# --------------------------------------------------
# 4. Probability of an Even Number
# --------------------------------------------------

even_outcomes = 3

probability_even = (
    even_outcomes / total_outcomes
)

print(
    "Probability of rolling an even number:",
    probability_even
)


# --------------------------------------------------
# 5. Conditional Probability
# --------------------------------------------------

total_customers = 1000

premium_customers = 300

premium_and_purchased = 180

conditional_probability = (
    premium_and_purchased /
    premium_customers
)

print("\n--- Conditional Probability ---")

print(
    "P(Purchase | Premium Customer):",
    conditional_probability
)

print(
    "Percentage:",
    conditional_probability * 100,
    "%"
)


# --------------------------------------------------
# 6. Joint Probability
# --------------------------------------------------

probability_email_open = 0.40

probability_purchase_given_open = 0.20

probability_open_and_purchase = (
    probability_email_open *
    probability_purchase_given_open
)

print("\n--- Joint Probability ---")

print(
    "Probability of Email Open and Purchase:",
    probability_open_and_purchase
)


# --------------------------------------------------
# 7. Independent Events
# --------------------------------------------------

probability_a = 0.50

probability_b = 0.30

probability_a_and_b = (
    probability_a * probability_b
)

print("\n--- Independent Events ---")

print(
    "P(A and B):",
    probability_a_and_b
)


# --------------------------------------------------
# 8. Probability of Either Event
# --------------------------------------------------

probability_a = 0.50

probability_b = 0.30

probability_a_and_b = 0.10

probability_a_or_b = (
    probability_a
    + probability_b
    - probability_a_and_b
)

print("\n--- Probability of A or B ---")

print(
    "P(A or B):",
    probability_a_or_b
)


# --------------------------------------------------
# 9. Business Dataset
# --------------------------------------------------

data = {
    "Customer_ID": [
        "C101", "C102", "C103", "C104", "C105",
        "C106", "C107", "C108", "C109", "C110",
        "C111", "C112", "C113", "C114", "C115"
    ],

    "Region": [
        "North", "South", "West", "North", "East",
        "South", "West", "North", "East", "South",
        "North", "West", "East", "South", "North"
    ],

    "Premium": [
        "Yes", "No", "Yes", "Yes", "No",
        "No", "Yes", "No", "Yes", "No",
        "Yes", "Yes", "No", "No", "Yes"
    ],

    "Purchased": [
        "Yes", "No", "Yes", "No", "Yes",
        "No", "Yes", "Yes", "No", "No",
        "Yes", "Yes", "No", "Yes", "Yes"
    ]
}

df = pd.DataFrame(data)

print("\n--- Customer Dataset ---")

print(df)


# --------------------------------------------------
# 10. Probability of Purchase
# --------------------------------------------------

total = len(df)

purchased = (
    df["Purchased"] == "Yes"
).sum()

purchase_probability = (
    purchased / total
)

print("\n--- Purchase Probability ---")

print(
    "Total Customers:",
    total
)

print(
    "Customers Who Purchased:",
    purchased
)

print(
    "Probability of Purchase:",
    round(purchase_probability, 2)
)


# --------------------------------------------------
# 11. Probability of Premium Customer
# --------------------------------------------------

premium_count = (
    df["Premium"] == "Yes"
).sum()

premium_probability = (
    premium_count / total
)

print("\n--- Premium Customer Probability ---")

print(
    "Probability of Premium Customer:",
    round(premium_probability, 2)
)


# --------------------------------------------------
# 12. Conditional Probability
# --------------------------------------------------

premium_df = df[
    df["Premium"] == "Yes"
]

premium_total = len(premium_df)

premium_purchased = (
    premium_df["Purchased"] == "Yes"
).sum()

premium_purchase_probability = (
    premium_purchased /
    premium_total
)

print(
    "\nProbability of Purchase given Premium:",
    round(
        premium_purchase_probability,
        2
    )
)


# --------------------------------------------------
# 13. Non-Premium Purchase Probability
# --------------------------------------------------

non_premium_df = df[
    df["Premium"] == "No"
]

non_premium_total = len(
    non_premium_df
)

non_premium_purchased = (
    non_premium_df["Purchased"] == "Yes"
).sum()

non_premium_purchase_probability = (
    non_premium_purchased /
    non_premium_total
)

print(
    "Probability of Purchase given Non-Premium:",
    round(
        non_premium_purchase_probability,
        2
    )
)


# --------------------------------------------------
# 14. Compare Customer Groups
# --------------------------------------------------

print("\n--- Customer Group Comparison ---")

print(
    "Premium Purchase Probability:",
    round(
        premium_purchase_probability,
        2
    )
)

print(
    "Non-Premium Purchase Probability:",
    round(
        non_premium_purchase_probability,
        2
    )
)


# --------------------------------------------------
# 15. Region Probability
# --------------------------------------------------

region_counts = df[
    "Region"
].value_counts()

region_probability = (
    region_counts / total
)

print("\n--- Region Probability ---")

print(region_probability)


# --------------------------------------------------
# 16. Probability of Purchase by Region
# --------------------------------------------------

region_purchase = pd.crosstab(
    df["Region"],
    df["Purchased"],
    normalize="index"
)

print(
    "\n--- Purchase Probability by Region ---"
)

print(region_purchase)


# --------------------------------------------------
# 17. Probability Table
# --------------------------------------------------

joint_probability = pd.crosstab(
    df["Premium"],
    df["Purchased"],
    normalize=True
)

print(
    "\n--- Joint Probability Table ---"
)

print(joint_probability)


# --------------------------------------------------
# 18. Business Risk Example
# --------------------------------------------------

total_transactions = 5000

failed_transactions = 125

failure_probability = (
    failed_transactions /
    total_transactions
)

print("\n--- Transaction Failure Probability ---")

print(
    "Failure Probability:",
    failure_probability
)

print(
    "Failure Rate:",
    failure_probability * 100,
    "%"
)


# --------------------------------------------------
# 19. Customer Churn Probability
# --------------------------------------------------

customers = 2000

churned_customers = 160

churn_probability = (
    churned_customers /
    customers
)

print("\n--- Customer Churn Probability ---")

print(
    "Churn Probability:",
    round(churn_probability, 3)
)

print(
    "Churn Rate:",
    churn_probability * 100,
    "%"
)


# --------------------------------------------------
# 20. Expected Number of Events
# --------------------------------------------------

customers = 10000

purchase_probability = 0.25

expected_purchases = (
    customers *
    purchase_probability
)

print("\n--- Expected Purchases ---")

print(
    "Expected Purchases:",
    expected_purchases
)


# --------------------------------------------------
# 21. Random Probability Simulation
# --------------------------------------------------

np.random.seed(42)

simulated_results = np.random.choice(
    ["Purchase", "No Purchase"],
    size=1000,
    p=[0.30, 0.70]
)

simulation_df = pd.Series(
    simulated_results
)

simulated_probability = (
    simulation_df.value_counts(
        normalize=True
    )
)

print("\n--- Probability Simulation ---")

print(simulated_probability)


# --------------------------------------------------
# 22. Business Interpretation
# --------------------------------------------------

print("\n--- Business Insights ---")

if premium_purchase_probability > non_premium_purchase_probability:

    print(
        "Premium customers have a higher "
        "probability of purchasing."
    )

else:

    print(
        "Non-premium customers have a higher "
        "probability of purchasing."
    )


print(
    f"Overall purchase probability: "
    f"{purchase_probability:.2f}"
)

print(
    f"Transaction failure rate: "
    f"{failure_probability * 100:.2f}%"
)

print(
    f"Customer churn rate: "
    f"{churn_probability * 100:.2f}%"
)


# --------------------------------------------------
# Key Takeaway
# --------------------------------------------------

print("\nDay 23 Complete: Probability with Python")
