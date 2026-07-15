import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import (mean_absolute_error, mean_squared_error, r2_score)

#loading the processed dataset
df = pd.read_csv("data/processed_dataset.csv")
print("Processed dataset loaded successfully!")
print(df.shape)

# Target variable
y = df["Order Item Quantity"]

# Remove leakage columns
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
print("Target:", y.shape)
print("\nFeatures Used:")
print(X.columns.tolist())

#splitting the dataset into training and testing data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("\nTrain-Test split completed ")
print("X_train:", X_train.shape)
print("X_test :", X_test.shape)
print("y_train:", y_train.shape)
print("y_test :", y_test.shape)

#linear regression
linear_model = LinearRegression()
linear_model.fit(X_train, y_train)
#random forest
rf_model = RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1)
rf_model.fit(X_train, y_train)
print("\nModels trained successfully!")

#prediction
linear_predictions = linear_model.predict(X_test)
rf_predictions = rf_model.predict(X_test)
print("\nPredictions generated successfully")

#calculating model evalution metrics
print("\nFor Linear Regression:-")
linear_mae = mean_absolute_error(y_test, linear_predictions)
linear_rmse = mean_squared_error(y_test, linear_predictions) ** 0.5
linear_r2 = r2_score(y_test, linear_predictions)
print("MAE:", linear_mae)
print("RMSE:", linear_rmse)
print("R² Score:", linear_r2)

print("\nFor Random Forest:-")
rf_mae = mean_absolute_error(y_test, rf_predictions)
rf_rmse = mean_squared_error(y_test, rf_predictions) ** 0.5
rf_r2 = r2_score(y_test, rf_predictions)
print("MAE :", rf_mae)
print("RMSE:", rf_rmse)
print("R² Score:", rf_r2)

#model comparision
comparison = pd.DataFrame({
    "Model": ["Linear Regression", "Random Forest"],
    "MAE": [linear_mae, rf_mae],
    "RMSE": [linear_rmse, rf_rmse],
    "R2 Score": [linear_r2, rf_r2]
})
print("\nModel Comparison")
print(comparison)
comparison.to_csv("results/model_comparison.csv", index=False)
print("\nModel comparison saved successfully!")
#Actual vs Predicted visualization
plt.figure(figsize=(8,6))
plt.scatter(y_test, rf_predictions, alpha=0.5)
plt.xlabel("Actual Quantity")
plt.ylabel("Predicted Quantity")
plt.title("Actual vs Predicted (Random Forest)")
plt.tight_layout()
plt.savefig("images/actual_vs_predicted.png")
plt.show()
plt.close()

#Feature Importance visualization
importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": rf_model.feature_importances_
})
importance = importance.sort_values(by="Importance", ascending=False)
print("\nTop 10 Important Features")
print(importance.head(10))
plt.figure(figsize=(10,6))
plt.barh(importance["Feature"].head(10), importance["Importance"].head(10))
plt.title("Top 10 Important Features")
plt.xlabel("Importance")
plt.tight_layout()
plt.savefig("images/feature_importance.png")
plt.show()
plt.close()

