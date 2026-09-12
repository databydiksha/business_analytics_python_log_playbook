# Day 30: K-Means Clustering with Python

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score


# --------------------------------------------------
# 1. CREATE CUSTOMER DATA
# --------------------------------------------------

np.random.seed(42)

data = pd.DataFrame({
    "Annual_Income": np.random.randint(20000, 120000, 300),
    "Annual_Spend": np.random.randint(5000, 90000, 300),
    "Website_Visits": np.random.randint(5, 100, 300),
    "Purchase_Frequency": np.random.randint(1, 30, 300)
})

print("Customer Dataset:")
print(data.head())

print("\nDataset Shape:")
print(data.shape)

print("\nDescriptive Statistics:")
print(data.describe())


# --------------------------------------------------
# 2. SELECT FEATURES
# --------------------------------------------------

features = [
    "Annual_Income",
    "Annual_Spend",
    "Website_Visits",
    "Purchase_Frequency"
]

X = data[features]


# --------------------------------------------------
# 3. FEATURE SCALING
# --------------------------------------------------

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

print("\nFeatures scaled successfully.")


# --------------------------------------------------
# 4. ELBOW METHOD
# --------------------------------------------------

inertia_values = []

for k in range(2, 11):

    model = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )

    model.fit(X_scaled)

    inertia_values.append(
        model.inertia_
    )

elbow_data = pd.DataFrame({
    "Number_of_Clusters": range(2, 11),
    "Inertia": inertia_values
})

print("\nELBOW METHOD RESULTS")
print(elbow_data)


# --------------------------------------------------
# 5. ELBOW METHOD VISUALIZATION
# --------------------------------------------------

plt.figure(figsize=(8, 5))

plt.plot(
    elbow_data["Number_of_Clusters"],
    elbow_data["Inertia"],
    marker="o"
)

plt.xlabel("Number of Clusters")
plt.ylabel("Inertia")
plt.title("Elbow Method for Optimal Number of Clusters")

plt.show()


# --------------------------------------------------
# 6. CREATE K-MEANS MODEL
# --------------------------------------------------

kmeans = KMeans(
    n_clusters=4,
    random_state=42,
    n_init=10
)

data["Cluster"] = kmeans.fit_predict(
    X_scaled
)

print("\nK-Means Clustering Completed")


# --------------------------------------------------
# 7. CLUSTER DISTRIBUTION
# --------------------------------------------------

cluster_counts = data["Cluster"].value_counts().sort_index()

print("\nCUSTOMERS IN EACH CLUSTER")
print(cluster_counts)


# --------------------------------------------------
# 8. CLUSTER SUMMARY
# --------------------------------------------------

cluster_summary = data.groupby(
    "Cluster"
)[features].mean().round(2)

print("\nCLUSTER SUMMARY")
print(cluster_summary)


# --------------------------------------------------
# 9. SILHOUETTE SCORE
# --------------------------------------------------

silhouette = silhouette_score(
    X_scaled,
    data["Cluster"]
)

print("\nSILHOUETTE SCORE")
print("Score:", round(silhouette, 3))


# --------------------------------------------------
# 10. CLUSTER VISUALIZATION
# --------------------------------------------------

plt.figure(figsize=(8, 5))

for cluster in sorted(data["Cluster"].unique()):

    cluster_data = data[
        data["Cluster"] == cluster
    ]

    plt.scatter(
        cluster_data["Annual_Income"],
        cluster_data["Annual_Spend"],
        label=f"Cluster {cluster}"
    )

plt.xlabel("Annual Income")
plt.ylabel("Annual Spend")
plt.title("Customer Segmentation Using K-Means")

plt.legend()

plt.show()


# --------------------------------------------------
# 11. CLUSTER CENTERS
# --------------------------------------------------

cluster_centers_scaled = kmeans.cluster_centers_

cluster_centers = scaler.inverse_transform(
    cluster_centers_scaled
)

centers = pd.DataFrame(
    cluster_centers,
    columns=features
)

centers.index.name = "Cluster"

print("\nCLUSTER CENTERS")
print(centers.round(2))


# --------------------------------------------------
# 12. ASSIGN CUSTOMER SEGMENTS
# --------------------------------------------------

segment_names = {
    0: "Segment A",
    1: "Segment B",
    2: "Segment C",
    3: "Segment D"
}

data["Customer_Segment"] = data["Cluster"].map(
    segment_names
)

print("\nCUSTOMER SEGMENTS")
print(
    data[
        [
            "Annual_Income",
            "Annual_Spend",
            "Website_Visits",
            "Purchase_Frequency",
            "Customer_Segment"
        ]
    ].head(10)
)


# --------------------------------------------------
# 13. SEGMENT BUSINESS PROFILE
# --------------------------------------------------

segment_profile = data.groupby(
    "Customer_Segment"
)[features].agg(
    ["mean", "min", "max"]
).round(2)

print("\nCUSTOMER SEGMENT PROFILE")
print(segment_profile)


# --------------------------------------------------
# 14. CUSTOMER COUNT BY SEGMENT
# --------------------------------------------------

segment_counts = (
    data["Customer_Segment"]
    .value_counts()
    .reset_index()
)

segment_counts.columns = [
    "Customer_Segment",
    "Customer_Count"
]

print("\nCUSTOMER COUNT BY SEGMENT")
print(segment_counts)


# --------------------------------------------------
# 15. SPENDING RATE
# --------------------------------------------------

data["Spend_Rate"] = (
    data["Annual_Spend"]
    / data["Annual_Income"]
)

spending_summary = data.groupby(
    "Customer_Segment"
)["Spend_Rate"].mean().sort_values(
    ascending=False
)

print("\nAVERAGE SPENDING RATE")
print(spending_summary.round(3))


# --------------------------------------------------
# 16. IDENTIFY HIGH-VALUE CUSTOMERS
# --------------------------------------------------

high_value_threshold = data[
    "Annual_Spend"
].quantile(0.75)

data["High_Value_Customer"] = np.where(
    data["Annual_Spend"] >= high_value_threshold,
    "Yes",
    "No"
)

print("\nHIGH-VALUE CUSTOMER DISTRIBUTION")
print(
    data["High_Value_Customer"].value_counts()
)


# --------------------------------------------------
# 17. BUSINESS INSIGHTS
# --------------------------------------------------

print("\nBUSINESS INSIGHTS")

print(
    "K-Means clustering groups customers based on "
    "similar characteristics."
)

print(
    "Customer segmentation can support targeted "
    "marketing strategies."
)

print(
    "The Elbow Method helps identify a suitable "
    "number of clusters."
)

print(
    "The Silhouette Score helps evaluate how well "
    "customers are separated into clusters."
)

print(
    "High-spending segments can be targeted with "
    "premium offers and loyalty programs."
)

print(
    "Low-engagement segments can be targeted with "
    "personalized campaigns."
)


# --------------------------------------------------
# 18. SAVE RESULTS
# --------------------------------------------------

data.to_csv(
    "Day-30-KMeans-Customer-Segmentation.csv",
    index=False
)

cluster_summary.to_csv(
    "Day-30-Cluster-Summary.csv"
)

centers.to_csv(
    "Day-30-Cluster-Centers.csv"
)

elbow_data.to_csv(
    "Day-30-Elbow-Analysis.csv",
    index=False
)

segment_counts.to_csv(
    "Day-30-Segment-Counts.csv",
    index=False
)

print("\nResults saved successfully.")
