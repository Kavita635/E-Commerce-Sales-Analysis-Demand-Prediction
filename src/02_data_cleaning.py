import pandas as pd

#loading the dataset
df = pd.read_csv("data/DataCoSupplyChainDataset.csv", encoding = "latin1")
print ("Dataset Loaded Successfully")
print(df.shape)

#creating a copy of the original dataset
clean_df = df.copy()
print("working copy created")

#removing unnecessary columns
columns_to_drop = [
    "Customer Email",
    "Customer Password",
    "Customer Fname",
    "Customer Lname",
    "Customer Street",
    "Product Image",
    "Product Description",
    "Customer Zipcode",
    "Order Zipcode"
]
clean_df.drop(columns = columns_to_drop, inplace = True)
print("Columns removed successfully!")
print(clean_df.shape)

#checking date columns
date_columns = [
    "order date (DateOrders)",
    "shipping date (DateOrders)"
]
for column in date_columns:
    clean_df[column] = pd.to_datetime(clean_df[column])
print("\nDate columns converted successfully!")
print(clean_df[date_columns].dtypes)
print(clean_df[date_columns].head())

#data validation
print("\nDataset shape:")
print(clean_df.shape)
print("\nTotal missing values:")
print(clean_df.isnull().sum())
print("\nData Type:")
print(clean_df.dtypes.value_counts())
print("\nDataset Information:")
clean_df.info()

#saving the clean dataset
clean_df.to_csv("data/cleaned_dataset.csv", index=False)
print("\nCleaned dataset saved successfully!")