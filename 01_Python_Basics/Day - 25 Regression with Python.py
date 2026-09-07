# Day 25: Regression with Python

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split


# --------------------------------------------------
# 1. CREATE BUSINESS DATA
# --------------------------------------------------

np.random.seed(42)

data = pd.DataFrame({
    "Advertising_Spend": np.random.randint(10000, 100000, 100),
    "Website_Visits": np.random.randint(1000, 10000, 100),
    "Discount_Percentage": np.random.randint(5, 31, 100)
})

data["Sales"] = (
    15000
    + data["Advertising_Spend"] * 0.65
    + data["Website_Visits"] * 8
    - data["Discount_Percentage"] * 300
    + np.random.normal(0, 5000, 100)
)

print("Business Dataset:")
print(data.head())

print("\nDataset Shape:")
print(data.shape)

print("\nDescriptive Statistics:")
print(data.describe())


# --------------------------------------------------
# 2. SIMPLE LINEAR REGRESSION
# --------------------------------------------------

X = data[["Advertising_Spend"]]
y = data["Sales"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = LinearRegression()

model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("\nSIMPLE LINEAR REGRESSION")

print("Intercept:", round(model.intercept_, 2))
print("Coefficient:", round(model.coef_[0], 2))
print("R-Squared:", round(r2_score(y_test, predictions), 3))


# --------------------------------------------------
# 3. MODEL EVALUATION
# --------------------------------------------------

mae = mean_absolute_error(y_test, predictions)
mse = mean_squared_error(y_test, predictions)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, predictions)

print("\nMODEL EVALUATION")

print("MAE:", round(mae, 2))
print("MSE:", round(mse, 2))
print("RMSE:", round(rmse, 2))
print("R-Squared:", round(r2, 3))


# --------------------------------------------------
# 4. ACTUAL VS PREDICTED SALES
# --------------------------------------------------

comparison = pd.DataFrame({
    "Actual_Sales": y_test.values,
    "Predicted_Sales": predictions
})

print("\nActual vs Predicted Sales:")
print(comparison.head(10))


# --------------------------------------------------
# 5. MULTIPLE LINEAR REGRESSION
# --------------------------------------------------

features = [
    "Advertising_Spend",
    "Website_Visits",
    "Discount_Percentage"
]

X = data[features]
y = data["Sales"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

multiple_model = LinearRegression()

multiple_model.fit(X_train, y_train)

predictions = multiple_model.predict(X_test)

print("\nMULTIPLE LINEAR REGRESSION")

print("Intercept:", round(multiple_model.intercept_, 2))

coefficients = pd.DataFrame({
    "Feature": features,
    "Coefficient": multiple_model.coef_
})

print("\nFeature Coefficients:")
print(coefficients)

print(
    "\nR-Squared:",
    round(r2_score(y_test, predictions), 3)
)


# --------------------------------------------------
# 6. MODEL PERFORMANCE
# --------------------------------------------------

mae = mean_absolute_error(y_test, predictions)
mse = mean_squared_error(y_test, predictions)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, predictions)

print("\nMULTIPLE REGRESSION PERFORMANCE")

print("MAE:", round(mae, 2))
print("MSE:", round(mse, 2))
print("RMSE:", round(rmse, 2))
print("R-Squared:", round(r2, 3))


# --------------------------------------------------
# 7. PREDICT SALES FOR A NEW SCENARIO
# --------------------------------------------------

new_business_data = pd.DataFrame({
    "Advertising_Spend": [75000],
    "Website_Visits": [6500],
    "Discount_Percentage": [15]
})

predicted_sales = multiple_model.predict(new_business_data)

print("\nNEW BUSINESS SCENARIO")

print(
    "Advertising Spend:",
    new_business_data["Advertising_Spend"].iloc[0]
)

print(
    "Website Visits:",
    new_business_data["Website_Visits"].iloc[0]
)

print(
    "Discount Percentage:",
    new_business_data["Discount_Percentage"].iloc[0]
)

print(
    "Predicted Sales:",
    round(predicted_sales[0], 2)
)


# --------------------------------------------------
# 8. REGRESSION VISUALIZATION
# --------------------------------------------------

plt.figure(figsize=(8, 5))

plt.scatter(
    data["Advertising_Spend"],
    data["Sales"]
)

plt.xlabel("Advertising Spend")
plt.ylabel("Sales")
plt.title("Advertising Spend vs Sales")

plt.show()


# --------------------------------------------------
# 9. ACTUAL VS PREDICTED VISUALIZATION
# --------------------------------------------------

plt.figure(figsize=(8, 5))

plt.scatter(
    y_test,
    predictions
)

plt.xlabel("Actual Sales")
plt.ylabel("Predicted Sales")
plt.title("Actual vs Predicted Sales")

plt.show()


# --------------------------------------------------
# 10. RESIDUAL ANALYSIS
# --------------------------------------------------

residuals = y_test - predictions

plt.figure(figsize=(8, 5))

plt.scatter(
    predictions,
    residuals
)

plt.axhline(
    y=0,
    linestyle="--"
)

plt.xlabel("Predicted Sales")
plt.ylabel("Residuals")
plt.title("Residual Analysis")

plt.show()


# --------------------------------------------------
# 11. BUSINESS INSIGHTS
# --------------------------------------------------

print("\nBUSINESS INSIGHTS")

print(
    "Advertising spend can be used as a predictor of sales."
)

print(
    "Multiple regression allows several business factors "
    "to be considered simultaneously."
)

print(
    "R-Squared shows how much variation in sales is explained "
    "by the model."
)

print(
    "MAE and RMSE help measure prediction error."
)

print(
    "The regression model can be used to estimate sales "
    "under new business scenarios."
)


# --------------------------------------------------
# 12. SAVE RESULTS
# --------------------------------------------------

comparison["Residual"] = (
    comparison["Actual_Sales"]
    - comparison["Predicted_Sales"]
)

comparison.to_csv(
    "Day-25-Regression-Predictions.csv",
    index=False
)

coefficients.to_csv(
    "Day-25-Regression-Coefficients.csv",
    index=False
)

print("\nRegression results saved successfully.")
