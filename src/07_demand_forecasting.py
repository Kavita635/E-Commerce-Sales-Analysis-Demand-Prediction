import pandas as pd
import joblib
import matplotlib.pyplot as plt

#loadig the processed dataset
df = pd.read_csv("data/processed_dataset.csv")
original_df = pd.read_csv(
    "data/DataCoSupplyChainDataset.csv",
    encoding="latin1"
)
print("Datasets loaded successfully!")
print("Processed Dataset:", df.shape)
print("Original Dataset :", original_df.shape)

#loading the trained random forest model
rf_model = joblib.load("models/random_forest.pkl")
print("Random forest model loaded successfully!")

# Target variable
y = df["Order Item Quantity"]

# Remove leakage columns (same as training)
leakage_columns = [
    "Sales",
    "Sales per customer",
    "Order Item Total",
    "Benefit per order",
    "Order Profit Per Order",
    "Order Item Profit Ratio",
    "Days for shipping (real)",
    "Late_delivery_risk"
]

# Feature matrix
X = df.drop(columns=leakage_columns + ["Order Item Quantity"])

print("\nTarget Variable: Order Item Quantity")
print("Feature Matrix:", X.shape)
print("\nFeatures Used:")
print(X.columns.tolist())

#generating the demand predictions
future_predictions = rf_model.predict(X)
print("\nDemand forecast generated successfully")

# Create forecast dataframe using original dataset
forecast_df = original_df.copy()

# Add model predictions
forecast_df["Predicted Demand"] = future_predictions

print("\nChecking Product Names:")
print(forecast_df["Product Name"].head(10))

print("\nSample Demand Forecast")
print(
    forecast_df[
        [
            "Product Name",
            "Predicted Demand"
        ]
    ].head(10)
)

#demand level classification
def classify_demand(x):
    if x >= 4:
        return "High"
    elif x >= 2:
        return "Medium"
    else:
        return "Low"
forecast_df["Demand Level"] = forecast_df["Predicted Demand"].apply(classify_demand)
print("\nDemand level distribution")
print(forecast_df["Demand Level"].value_counts())

# Inventory Recommendation
def inventory_action(level):
    if level == "High":
        return "Increase Stock"
    elif level == "Medium":
        return "Maintain Stock"
    else:
        return "Reduce Stock"
forecast_df["Inventory Recommendation"] = forecast_df["Demand Level"].apply(inventory_action)
print("\nInventory Recommendations")
print(
    forecast_df[
        [
            "Predicted Demand",
            "Demand Level",
            "Inventory Recommendation"
        ]
    ].head(10)
)
forecast_df.to_csv(
    "results/demand_forecast.csv",
    index=False
)
print("\nDemand forecast saved successfully!")
print("File saved at: results/demand_forecast.csv")

#Demand level distribution chart
plt.figure(figsize=(8,5))
forecast_df["Demand Level"].value_counts().plot(kind="bar")
plt.title("Demand Level Distribution")
plt.xlabel("Demand Level")
plt.ylabel("Number of Products")
plt.tight_layout()
plt.savefig("images/demand_level_distribution.png")
plt.show()
plt.close()

#Inventory recommendation chart
plt.figure(figsize=(8,5))
forecast_df["Inventory Recommendation"].value_counts().plot(kind="bar")
plt.title("Inventory Recommendation Distribution")
plt.xlabel("Recommendation")
plt.ylabel("Number of Products")
plt.tight_layout()
plt.savefig("images/inventory_recommendation.png")
plt.show()
plt.close()

#top predicted demand products
top_products = forecast_df.sort_values(
    by="Predicted Demand",
    ascending=False
).head(10)
print("\nTop 10 Highest Predicted Demand Products")
print(top_products[["Product Name", "Predicted Demand"]])
plt.figure(figsize=(10,6))
plt.figure(figsize=(14,6))
plt.bar(
    top_products["Product Name"].str[:30],
    top_products["Predicted Demand"]
)
plt.xticks(rotation=60, ha="right")
plt.title("Top 10 Predicted Demand Products")
plt.xlabel("Product")
plt.ylabel("Predicted Demand")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("images/top_predicted_products.png")
plt.show()
plt.close()

#average predicted demand bye shipping mode
shipping_forecast = forecast_df.groupby(
    "Shipping Mode"
)["Predicted Demand"].mean()
print("\nAverage Demand by Shipping Mode")
print(shipping_forecast)
plt.figure(figsize=(8,5))
shipping_forecast.plot(kind="bar")
plt.title("Average Predicted Demand by Shipping Mode")
plt.xlabel("Shipping Mode")
plt.ylabel("Average Predicted Demand")
plt.tight_layout()
plt.savefig("images/shipping_mode_prediction.png")
plt.show()
plt.close()