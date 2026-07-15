import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

#loading the dataset
df = pd.read_csv("data/processed_dataset.csv")

print("Processed dataset loaded successfully!")
print(df.shape)

# Remove leakage columns (same as Day 4)
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

# Define features and target
X = df.drop(columns=leakage_columns + ["Order Item Quantity"])
y = df["Order Item Quantity"]

print("\nTarget Variable: Order Item Quantity")
print("Feature Matrix:", X.shape)
print("Target:", y.shape)

#splitting the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=42)
print("\nTrain-Test split completed")
print("X_train:", X_train.shape)
print("X_test:", X_test.shape)
print("y_train:", y_train.shape)
print("y_test:",y_test.shape)

#Training linear regression
linear_model = LinearRegression()
linear_model.fit(X_train, y_train)
print("\nLinear Regression model trained successfully")

#training the random forest
rf_model = RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1)
rf_model.fit(X_train, y_train)
print("Random Forest model trained successfully")

#saving the trained models
joblib.dump(linear_model, "models/linear_regression.pkl")
joblib.dump(rf_model, "models/random_forest.pkl")
print("\nModels saved successfully")

#making predictions
linear_predictions = linear_model.predict(X_test)
rf_predictions = rf_model.predict(X_test)
print("\nPredictions generated successfully!")
prediction_df = pd.DataFrame({
    "Actual Quantity": y_test.values,
    "Linear Prediction": linear_predictions,
    "Random Forest Prediction": rf_predictions
})
print("\nSample Predictions")
print(prediction_df.head(10))

prediction_df.to_csv("results/model_predictions.csv", index=False)
print("\nPredictions saved successfully")