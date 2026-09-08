# Day 27: Decision Trees with Python

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    precision_score,
    recall_score,
    f1_score
)
from sklearn.tree import plot_tree


# --------------------------------------------------
# 1. CREATE BUSINESS DATA
# --------------------------------------------------

np.random.seed(42)

data = pd.DataFrame({
    "Age": np.random.randint(20, 60, 250),
    "Monthly_Spend": np.random.randint(500, 10000, 250),
    "Website_Visits": np.random.randint(1, 30, 250),
    "Support_Calls": np.random.randint(0, 10, 250),
    "Tenure_Months": np.random.randint(1, 60, 250)
})

purchase_score = (
    data["Monthly_Spend"] / 3000
    + data["Website_Visits"] / 10
    + data["Tenure_Months"] / 20
    - data["Support_Calls"] / 3
)

data["Purchased"] = (
    purchase_score > purchase_score.median()
).astype(int)

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
    "Support_Calls",
    "Tenure_Months"
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
# 4. CREATE DECISION TREE MODEL
# --------------------------------------------------

model = DecisionTreeClassifier(
    max_depth=4,
    random_state=42
)

model.fit(
    X_train,
    y_train
)

print("\nDecision Tree Model Trained Successfully")


# --------------------------------------------------
# 5. MAKE PREDICTIONS
# --------------------------------------------------

y_pred = model.predict(X_test)

print("\nPredictions:")
print(y_pred[:10])


# --------------------------------------------------
# 6. MODEL ACCURACY
# --------------------------------------------------

accuracy = accuracy_score(
    y_test,
    y_pred
)

print("\nMODEL ACCURACY")
print("Accuracy:", round(accuracy, 3))


# --------------------------------------------------
# 7. CONFUSION MATRIX
# --------------------------------------------------

cm = confusion_matrix(
    y_test,
    y_pred
)

print("\nCONFUSION MATRIX")
print(cm)


# --------------------------------------------------
# 8. CLASSIFICATION METRICS
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
# 9. CLASSIFICATION REPORT
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
# 10. FEATURE IMPORTANCE
# --------------------------------------------------

feature_importance = pd.DataFrame({
    "Feature": features,
    "Importance": model.feature_importances_
})

feature_importance = feature_importance.sort_values(
    by="Importance",
    ascending=False
)

print("\nFEATURE IMPORTANCE")
print(feature_importance)


# --------------------------------------------------
# 11. PREDICT A NEW CUSTOMER
# --------------------------------------------------

new_customer = pd.DataFrame({
    "Age": [30],
    "Monthly_Spend": [7000],
    "Website_Visits": [18],
    "Support_Calls": [2],
    "Tenure_Months": [24]
})

prediction = model.predict(
    new_customer
)[0]

probability = model.predict_proba(
    new_customer
)[0]

print("\nNEW CUSTOMER PREDICTION")

print(
    "Probability of Not Purchasing:",
    round(probability[0] * 100, 2),
    "%"
)

print(
    "Probability of Purchasing:",
    round(probability[1] * 100, 2),
    "%"
)

if prediction == 1:
    print("Prediction: Customer is likely to purchase")
else:
    print("Prediction: Customer is unlikely to purchase")


# --------------------------------------------------
# 12. VISUALIZE DECISION TREE
# --------------------------------------------------

plt.figure(figsize=(18, 10))

plot_tree(
    model,
    feature_names=features,
    class_names=["No Purchase", "Purchase"],
    filled=True,
    rounded=True
)

plt.title("Decision Tree for Customer Purchase Prediction")

plt.show()


# --------------------------------------------------
# 13. FEATURE IMPORTANCE VISUALIZATION
# --------------------------------------------------

plt.figure(figsize=(8, 5))

plt.bar(
    feature_importance["Feature"],
    feature_importance["Importance"]
)

plt.xlabel("Features")
plt.ylabel("Importance")
plt.title("Decision Tree Feature Importance")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()


# --------------------------------------------------
# 14. DIFFERENT TREE DEPTHS
# --------------------------------------------------

depth_results = []

for depth in range(1, 9):

    tree = DecisionTreeClassifier(
        max_depth=depth,
        random_state=42
    )

    tree.fit(
        X_train,
        y_train
    )

    train_accuracy = tree.score(
        X_train,
        y_train
    )

    test_accuracy = tree.score(
        X_test,
        y_test
    )

    depth_results.append({
        "Max_Depth": depth,
        "Training_Accuracy": train_accuracy,
        "Testing_Accuracy": test_accuracy
    })

depth_results = pd.DataFrame(
    depth_results
)

print("\nTREE DEPTH ANALYSIS")
print(depth_results)


# --------------------------------------------------
# 15. BUSINESS INSIGHTS
# --------------------------------------------------

print("\nBUSINESS INSIGHTS")

print(
    "Decision Trees can be used for business classification problems."
)

print(
    "The model makes decisions using a series of conditions."
)

print(
    "Feature importance helps identify variables that contribute "
    "most to the prediction."
)

print(
    "Decision Trees are easy to interpret compared with many "
    "complex machine learning models."
)

print(
    "Very deep trees can overfit the training data."
)

print(
    "Controlling tree depth can help improve generalization."
)


# --------------------------------------------------
# 16. SAVE RESULTS
# --------------------------------------------------

prediction_results = X_test.copy()

prediction_results["Actual"] = y_test.values
prediction_results["Predicted"] = y_pred

prediction_results.to_csv(
    "Day-27-Decision-Tree-Predictions.csv",
    index=False
)

feature_importance.to_csv(
    "Day-27-Decision-Tree-Feature-Importance.csv",
    index=False
)

depth_results.to_csv(
    "Day-27-Decision-Tree-Depth-Analysis.csv",
    index=False
)

print("\nResults saved successfully.")
