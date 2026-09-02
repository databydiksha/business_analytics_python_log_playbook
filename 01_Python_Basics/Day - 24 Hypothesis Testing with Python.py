# Day 24: Hypothesis Testing with Python

import numpy as np
import pandas as pd
from scipy import stats


# --------------------------------------------------
# 1. BASIC HYPOTHESIS TESTING CONCEPT
# --------------------------------------------------

print("HYPOTHESIS TESTING")

print("\nNull Hypothesis (H0): No significant difference or effect")
print("Alternative Hypothesis (H1): Significant difference or effect")
print("Significance Level: 5%")
print("Decision Rule: If p-value < 0.05, reject H0")


# --------------------------------------------------
# 2. CREATE BUSINESS DATA
# --------------------------------------------------

np.random.seed(42)

sales_data = pd.DataFrame({
    "Customer_ID": range(1, 101),
    "Group": ["Before"] * 50 + ["After"] * 50,
    "Sales": np.concatenate([
        np.random.normal(5000, 700, 50),
        np.random.normal(5500, 700, 50)
    ])
})

print("\nBusiness Data:")
print(sales_data.head())

print("\nGroup Summary:")
print(sales_data.groupby("Group")["Sales"].agg(
    ["count", "mean", "median", "std", "min", "max"]
))


# --------------------------------------------------
# 3. ONE-SAMPLE T-TEST
# --------------------------------------------------

sample_sales = sales_data["Sales"]

test_value = 5000

t_statistic, p_value = stats.ttest_1samp(
    sample_sales,
    test_value
)

print("\nONE-SAMPLE T-TEST")
print("T-Statistic:", round(t_statistic, 3))
print("P-Value:", round(p_value, 5))

if p_value < 0.05:
    print("Decision: Reject H0")
    print("There is a significant difference from the target value.")
else:
    print("Decision: Fail to reject H0")
    print("There is no significant difference from the target value.")


# --------------------------------------------------
# 4. INDEPENDENT TWO-SAMPLE T-TEST
# --------------------------------------------------

before_sales = sales_data[
    sales_data["Group"] == "Before"
]["Sales"]

after_sales = sales_data[
    sales_data["Group"] == "After"
]["Sales"]

t_statistic, p_value = stats.ttest_ind(
    before_sales,
    after_sales
)

print("\nINDEPENDENT TWO-SAMPLE T-TEST")
print("Before Average Sales:", round(before_sales.mean(), 2))
print("After Average Sales:", round(after_sales.mean(), 2))
print("T-Statistic:", round(t_statistic, 3))
print("P-Value:", round(p_value, 5))

if p_value < 0.05:
    print("Decision: Reject H0")
    print("The difference between the two groups is statistically significant.")
else:
    print("Decision: Fail to reject H0")
    print("The difference between the two groups is not statistically significant.")


# --------------------------------------------------
# 5. PAIRED T-TEST
# --------------------------------------------------

before = np.array([
    4500, 4700, 4800, 5000, 4900,
    5100, 5200, 5300, 5000, 4800
])

after = np.array([
    4800, 5000, 5100, 5300, 5200,
    5400, 5500, 5600, 5300, 5100
])

t_statistic, p_value = stats.ttest_rel(
    before,
    after
)

print("\nPAIRED T-TEST")
print("Before Average:", round(before.mean(), 2))
print("After Average:", round(after.mean(), 2))
print("T-Statistic:", round(t_statistic, 3))
print("P-Value:", round(p_value, 5))

if p_value < 0.05:
    print("Decision: Reject H0")
    print("The change is statistically significant.")
else:
    print("Decision: Fail to reject H0")
    print("The change is not statistically significant.")


# --------------------------------------------------
# 6. CHI-SQUARE TEST OF INDEPENDENCE
# --------------------------------------------------

customer_data = pd.DataFrame({
    "Purchased": [
        "Yes", "No", "Yes", "Yes", "No",
        "Yes", "No", "Yes", "No", "Yes",
        "Yes", "No", "Yes", "No", "Yes",
        "No", "Yes", "Yes", "No", "Yes"
    ],
    "Premium_Customer": [
        "Yes", "No", "Yes", "No", "No",
        "Yes", "No", "Yes", "No", "Yes",
        "Yes", "No", "Yes", "No", "Yes",
        "No", "Yes", "Yes", "No", "Yes"
    ]
})

contingency_table = pd.crosstab(
    customer_data["Premium_Customer"],
    customer_data["Purchased"]
)

print("\nCONTINGENCY TABLE")
print(contingency_table)

chi2, p_value, degrees_of_freedom, expected = stats.chi2_contingency(
    contingency_table
)

print("\nCHI-SQUARE TEST")
print("Chi-Square Statistic:", round(chi2, 3))
print("Degrees of Freedom:", degrees_of_freedom)
print("P-Value:", round(p_value, 5))

if p_value < 0.05:
    print("Decision: Reject H0")
    print("Customer type and purchase behavior are significantly associated.")
else:
    print("Decision: Fail to reject H0")
    print("No significant association was found.")


# --------------------------------------------------
# 7. CORRELATION SIGNIFICANCE TEST
# --------------------------------------------------

advertising_spend = np.array([
    100, 120, 130, 150, 170,
    180, 200, 220, 250, 280
])

sales = np.array([
    200, 230, 250, 280, 310,
    330, 360, 390, 430, 470
])

correlation, p_value = stats.pearsonr(
    advertising_spend,
    sales
)

print("\nPEARSON CORRELATION TEST")
print("Correlation:", round(correlation, 3))
print("P-Value:", round(p_value, 5))

if p_value < 0.05:
    print("The relationship is statistically significant.")
else:
    print("The relationship is not statistically significant.")


# --------------------------------------------------
# 8. CONFIDENCE INTERVAL
# --------------------------------------------------

sample = sales_data["Sales"]

mean = sample.mean()
standard_error = stats.sem(sample)

confidence_interval = stats.t.interval(
    confidence=0.95,
    df=len(sample) - 1,
    loc=mean,
    scale=standard_error
)

print("\n95% CONFIDENCE INTERVAL")
print("Sample Mean:", round(mean, 2))
print("Lower Limit:", round(confidence_interval[0], 2))
print("Upper Limit:", round(confidence_interval[1], 2))


# --------------------------------------------------
# 9. BUSINESS DECISION
# --------------------------------------------------

print("\nBUSINESS DECISION")

if p_value < 0.05:
    print("The statistical evidence supports a significant relationship.")
else:
    print("The statistical evidence is not strong enough to confirm a relationship.")


# --------------------------------------------------
# 10. KEY CONCEPTS
# --------------------------------------------------

print("\nKEY CONCEPTS")
print("H0 = Null Hypothesis")
print("H1 = Alternative Hypothesis")
print("Alpha = Significance Level")
print("p-value < 0.05 = Reject H0")
print("p-value >= 0.05 = Fail to Reject H0")
print("T-Test = Compare means")
print("Chi-Square = Test categorical association")
print("Pearson Correlation = Test linear relationship")
print("Confidence Interval = Range of plausible population values")


# --------------------------------------------------
# 11. SAVE RESULTS
# --------------------------------------------------

results = pd.DataFrame({
    "Metric": [
        "Overall Mean Sales",
        "Before Mean Sales",
        "After Mean Sales",
        "95% CI Lower",
        "95% CI Upper"
    ],
    "Value": [
        sample.mean(),
        before_sales.mean(),
        after_sales.mean(),
        confidence_interval[0],
        confidence_interval[1]
    ]
})

results.to_csv(
    "Day-24-Hypothesis-Testing-Results.csv",
    index=False
)

print("\nResults saved successfully.")
