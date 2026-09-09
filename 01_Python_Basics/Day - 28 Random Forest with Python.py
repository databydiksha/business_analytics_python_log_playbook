# Day 28: Random Forest with Python

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score
)


# --------------------------------------------------
# 1. CREATE BUSINESS DATA
# --------------------------------------------------

np.random.seed(42)

data = pd.DataFrame({
    "Age": np.random.randint(20, 60, 300),
    "Monthly_Spend": np.random.randint(500, 10000, 300),
    "Website_Visits": np.random.randint(1, 30, 300),
    "Support_Calls": np.random.randint(0, 10, 300),
    "Tenure_Months": np.random.randint(1, 60, 300)
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
# 4. CREATE RANDOM FOREST MODEL
# --------------------------------------------------

random_forest = RandomForestClassifier(
    n_estimators=100,
    max_depth=5,
    random_state=42
)

random_forest.fit(
    X_train,
    y_train
)

print("\nRandom Forest Model Trained Successfully")


# --------------------------------------------------
# 5. MAKE PREDICTIONS
# --------------------------------------------------

y_pred = random_forest.predict(
    X_test
)

y_probability = random_forest.predict_proba(
    X_test
)[:, 1]

print("\nPredictions:")
print(y_pred[:10])

print("\nPurchase Probabilities:")
print(y_probability[:10])


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

roc_auc = roc_auc_score(
    y_test,
    y_probability
)

print("\nCLASSIFICATION METRICS")

print("Precision:", round(precision, 3))
print("Recall:", round(recall, 3))
print("F1 Score:", round(f1, 3))
print("ROC-AUC:", round(roc_auc, 3))


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
    "Importance": random_forest.feature_importances_
})

feature_importance = feature_importance.sort_values(
    by="Importance",
    ascending=False
)

print("\nFEATURE IMPORTANCE")
print(feature_importance)


# --------------------------------------------------
# 11. FEATURE IMPORTANCE VISUALIZATION
# --------------------------------------------------

plt.figure(figsize=(8, 5))

plt.bar(
    feature_importance["Feature"],
    feature_importance["Importance"]
)

plt.xlabel("Features")
plt.ylabel("Importance")
plt.title("Random Forest Feature Importance")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()


# --------------------------------------------------
# 12. PREDICT A NEW CUSTOMER
# --------------------------------------------------

new_customer = pd.DataFrame({
    "Age": [32],
    "Monthly_Spend": [7500],
    "Website_Visits": [20],
    "Support_Calls": [2],
    "Tenure_Months": [30]
})

new_prediction = random_forest.predict(
    new_customer
)[0]

new_probability = random_forest.predict_proba(
    new_customer
)[0]

print("\nNEW CUSTOMER PREDICTION")

print(
    "Probability of Not Purchasing:",
    round(new_probability[0] * 100, 2),
    "%"
)

print(
    "Probability of Purchasing:",
    round(new_probability[1] * 100, 2),
    "%"
)

if new_prediction == 1:
    print("Prediction: Customer is likely to purchase")
else:
    print("Prediction: Customer is unlikely to purchase")


# --------------------------------------------------
# 13. COMPARE DECISION TREE AND RANDOM FOREST
# --------------------------------------------------

decision_tree = DecisionTreeClassifier(
    max_depth=5,
    random_state=42
)

decision_tree.fit(
    X_train,
    y_train
)

tree_predictions = decision_tree.predict(
    X_test
)

tree_accuracy = accuracy_score(
    y_test,
    tree_predictions
)

forest_accuracy = accuracy_score(
    y_test,
    y_pred
)

comparison = pd.DataFrame({
    "Model": [
        "Decision Tree",
        "Random Forest"
    ],
    "Accuracy": [
        tree_accuracy,
        forest_accuracy
    ]
})

print("\nMODEL COMPARISON")
print(comparison)


# --------------------------------------------------
# 14. MODEL COMPARISON VISUALIZATION
# --------------------------------------------------

plt.figure(figsize=(7, 5))

plt.bar(
    comparison["Model"],
    comparison["Accuracy"]
)

plt.xlabel("Model")
plt.ylabel("Accuracy")
plt.title("Decision Tree vs Random Forest")

plt.ylim(0, 1)

plt.show()


# --------------------------------------------------
# 15. TEST DIFFERENT NUMBERS OF TREES
# --------------------------------------------------

tree_results = []

for number_of_trees in [10, 25, 50, 100, 150, 200]:

    model = RandomForestClassifier(
        n_estimators=number_of_trees,
        max_depth=5,
        random_state=42
    )

    model.fit(
        X_train,
        y_train
    )

    predictions = model.predict(
        X_test
    )

    accuracy_value = accuracy_score(
        y_test,
        predictions
    )

    tree_results.append({
        "Number_of_Trees": number_of_trees,
        "Accuracy": accuracy_value
    })

tree_results = pd.DataFrame(
    tree_results
)

print("\nNUMBER OF TREES ANALYSIS")
print(tree_results)


# --------------------------------------------------
# 16. BUSINESS INSIGHTS
# --------------------------------------------------

print("\nBUSINESS INSIGHTS")

print(
    "Random Forest combines multiple decision trees "
    "to improve prediction stability."
)

print(
    "It can be used for customer purchase prediction "
    "and other classification problems."
)

print(
    "Feature importance helps identify the variables "
    "that contribute most to the prediction."
)

print(
    "Increasing the number of trees can improve model "
    "stability, although it also increases computation."
)

print(
    "Random Forest is generally more robust than a "
    "single Decision Tree."
)

print(
    "Model performance should be evaluated using multiple "
    "metrics rather than accuracy alone."
)


# --------------------------------------------------
# 17. SAVE RESULTS
# --------------------------------------------------

prediction_results = X_test.copy()

prediction_results["Actual"] = y_test.values
prediction_results["Predicted"] = y_pred
prediction_results["Purchase_Probability"] = y_probability

prediction_results.to_csv(
    "Day-28-Random-Forest-Predictions.csv",
    index=False
)

feature_importance.to_csv(
    "Day-28-Random-Forest-Feature-Importance.csv",
    index=False
)

comparison.to_csv(
    "Day-28-Model-Comparison.csv",
    index=False
)

tree_results.to_csv(
    "Day-28-Number-of-Trees-Analysis.csv",
    index=False
)

print("\nResults saved successfully.")
