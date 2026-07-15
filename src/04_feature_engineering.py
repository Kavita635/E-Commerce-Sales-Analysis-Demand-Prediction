import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import joblib

#loading the cleaned dataset
df = pd.read_csv("data/cleaned_dataset.csv")
print("Dataset loaded successfully!")
print(df.shape)

#converting date columns
df["order date (DateOrders)"] = pd.to_datetime(df["order date (DateOrders)"])
df["shipping date (DateOrders)"] = pd.to_datetime(df["shipping date (DateOrders)"])
print("Date columns converted successfully")

#feature engineering from order date
df["Order Year"]  = df["order date (DateOrders)"].dt.year
df["Order Month"] = df["order date (DateOrders)"].dt.month
df["Order Day"] = df["order date (DateOrders)"].dt.day
df["Order Weekday"] = df["order date (DateOrders)"].dt.day_name()
df["Order Quarter"] = df["order date (DateOrders)"].dt.quarter
print("\nNew date features created")
print(df[[
    "order date (DateOrders)",
    "Order Year",
    "Order Month",
    "Order Day",
    "Order Weekday",
    "Order Quarter"
]].head())

#Label Encoding
label_encoders = {}
categorical_columns = df.select_dtypes(include="object").columns
print("\nCategorical Columns")
print(categorical_columns)
for column in categorical_columns:

    encoder = LabelEncoder()

    df[column] = encoder.fit_transform(df[column])

    label_encoders[column] = encoder

print("\nCategorical columns encoded successfully!")

joblib.dump(
    label_encoders["Product Name"],
    "models/product_name_encoder.pkl"
)

print("\nProduct Name Encoder Saved!")
print(df.head())

#droping the unnecessary columns
columns_to_drop = [
    "order date (DateOrders)",
    "shipping date (DateOrders)",
    "Customer Id",
    "Order Customer Id",
    "Order Id",
    "Order Item Id",
    "Product Card Id",
    "Category Id",
    "Department Id"
]
df.drop(columns=columns_to_drop, inplace=True)
print("\nUnnecessary columns removed!")
print(df.shape)

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
X = df.drop(columns=leakage_columns + ["Order Item Quantity"])
y = df["Order Item Quantity"]

#defining features and target
print("\nTarget Variable: Order Item Quantity")
print("\nFeature Matrix Shape:", X.shape)
print("Target Shape:", y.shape)
print("\nFeatures Used:")
print(X.columns.tolist())

#Spliting the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("\nTrain-Test Split Completed")
print("X_train:", X_train.shape)
print("X_test:", X_test.shape)
print("y_train:", y_train.shape)
print("y_test:",y_test.shape)

#saving the prpcessed dataset
df.to_csv("data/processed_dataset.csv", index=False)
print("\nProcessed dataset saved successfully!")
