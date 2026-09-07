# Day 26: Logistic Regression with Python

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    roc_curve
)


# --------------------------------------------------
# 1. CREATE BUSINESS DATA
# --------------------------------------------------

np.random.seed(42)

data = pd.DataFrame({
    "Age": np.random.randint(20, 60, 200),
    "Monthly_Spend": np.random.randint(500, 10000, 200),
    "Website_Visits": np.random.randint(1, 30, 200),
    "Support_Calls": np.random.randint(0, 10, 200)
})

probability = (
    0.25
    + data["Monthly_Spend"] / 30000
    + data["Website_Visits"] / 100
    - data["Support_Calls"] / 20
)

probability = np.clip(probability, 0.05, 0.95)

data["Purchased"] = np.random.binomial(
    1,
    probability
)

print("Business Dataset:")
print(data.head())

print("\nDataset Shape:")
print(data.shape)

print("\nTarget Distribution:")
print(data["Purchased"].value_counts())


# --------------------------------------------------
# 2. DEFINE FEATURES AND TARGET
# --------------------------------------------------

features = [
    "Age",
    "Monthly_Spend",
    "Website_Visits",
    "Support_Calls"
]

X = data[features]
y = data["Purchased"]


# --------------------------------------------------
# 3. TRAIN-TEST SPLIT
# --------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\nTraining Data:", X_train.shape)
print("Testing Data:", X_test.shape)


# --------------------------------------------------
# 4. FEATURE SCALING
# --------------------------------------------------

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


# --------------------------------------------------
# 5. TRAIN LOGISTIC REGRESSION
# --------------------------------------------------

model = LogisticRegression(
    random_state=42
)

model.fit(
    X_train_scaled,
    y_train
)

print("\nLogistic Regression Model Trained Successfully")


# --------------------------------------------------
# 6. MAKE PREDICTIONS
# --------------------------------------------------

y_pred = model.predict(X_test_scaled)

y_probability = model.predict_proba(
    X_test_scaled
)[:, 1]

print("\nPredictions:")
print(y_pred[:10])

print("\nPurchase Probabilities:")
print(y_probability[:10])


# --------------------------------------------------
# 7. MODEL ACCURACY
# --------------------------------------------------

accuracy = accuracy_score(
    y_test,
    y_pred
)

print("\nMODEL ACCURACY")
print("Accuracy:", round(accuracy, 3))


# --------------------------------------------------
# 8. CONFUSION MATRIX
# --------------------------------------------------

cm = confusion_matrix(
    y_test,
    y_pred
)

print("\nCONFUSION MATRIX")
print(cm)


# --------------------------------------------------
# 9. CLASSIFICATION METRICS
# --------------------------------------------------

precision = precision_score(
    y_test,
    y_pred,
    zero_division=0
)

recall = recall_score(
    y_test,
    y_pred,
    zero_division=0
)

f1 = f1_score(
    y_test,
    y_pred,
    zero_division=0
)

print("\nCLASSIFICATION METRICS")

print("Precision:", round(precision, 3))
print("Recall:", round(recall, 3))
print("F1 Score:", round(f1, 3))


# --------------------------------------------------
# 10. CLASSIFICATION REPORT
# --------------------------------------------------

print("\nCLASSIFICATION REPORT")

print(
    classification_report(
        y_test,
        y_pred,
        zero_division=0
    )
)


# --------------------------------------------------
# 11. ROC-AUC SCORE
# --------------------------------------------------

roc_auc = roc_auc_score(
    y_test,
    y_probability
)

print("\nROC-AUC SCORE")
print("ROC-AUC:", round(roc_auc, 3))


# --------------------------------------------------
# 12. MODEL COEFFICIENTS
# --------------------------------------------------

coefficients = pd.DataFrame({
    "Feature": features,
    "Coefficient": model.coef_[0]
})

coefficients["Impact"] = np.where(
    coefficients["Coefficient"] > 0,
    "Positive",
    "Negative"
)

print("\nMODEL COEFFICIENTS")
print(coefficients)


# --------------------------------------------------
# 13. PREDICTION FOR A NEW CUSTOMER
# --------------------------------------------------

new_customer = pd.DataFrame({
    "Age": [30],
    "Monthly_Spend": [6500],
    "Website_Visits": [15],
    "Support_Calls": [2]
})

new_customer_scaled = scaler.transform(
    new_customer
)

new_prediction = model.predict(
    new_customer_scaled
)[0]

new_probability = model.predict_proba(
    new_customer_scaled
)[0][1]

print("\nNEW CUSTOMER PREDICTION")

print(
    "Purchase Probability:",
    round(new_probability * 100, 2),
    "%"
)

if new_prediction == 1:
    print("Prediction: Customer is likely to purchase")
else:
    print("Prediction: Customer is unlikely to purchase")


# --------------------------------------------------
# 14. ROC CURVE
# --------------------------------------------------

fpr, tpr, thresholds = roc_curve(
    y_test,
    y_probability
)

plt.figure(figsize=(8, 5))

plt.plot(
    fpr,
    tpr,
    label=f"ROC-AUC = {roc_auc:.3f}"
)

plt.plot(
    [0, 1],
    [0, 1],
    linestyle="--"
)

plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")

plt.legend()

plt.show()


# --------------------------------------------------
# 15. PREDICTION RESULTS
# --------------------------------------------------

results = X_test.copy()

results["Actual"] = y_test.values
results["Predicted"] = y_pred
results["Purchase_Probability"] = y_probability

print("\nPREDICTION RESULTS")
print(results.head(10))


# --------------------------------------------------
# 16. BUSINESS INSIGHTS
# --------------------------------------------------

print("\nBUSINESS INSIGHTS")

print(
    "Logistic Regression is useful for binary classification problems."
)

print(
    "The model estimates the probability of a customer purchasing."
)

print(
    "Precision measures how many predicted positive cases were correct."
)

print(
    "Recall measures how many actual positive cases were identified."
)

print(
    "F1 Score balances precision and recall."
)

print(
    "ROC-AUC evaluates the model's ability to distinguish between classes."
)

print(
    "Model coefficients help understand the direction of feature impact."
)


# --------------------------------------------------
# 17. SAVE RESULTS
# --------------------------------------------------

results.to_csv(
    "Day-26-Logistic-Regression-Predictions.csv",
    index=False
)

coefficients.to_csv(
    "Day-26-Logistic-Regression-Coefficients.csv",
    index=False
)

print("\nResults saved successfully.")
