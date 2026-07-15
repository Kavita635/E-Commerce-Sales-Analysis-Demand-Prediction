import pandas as pd

#loading the dataset
df = pd.read_csv("data/DataCoSupplyChainDataset.csv", encoding="latin1")

print("=" * 50)
print("First 5 rows")
print("=" * 50)
print(df.head())

print("\n")

print("=" * 50)
print("Dataset Shape")
print("=" * 50)
print(df.shape)

print("\n")

print("=" * 50)
print("Column Names")
print("=" * 50)
print(df.columns.tolist())

print("\n")

print("=" * 50)
print("Dataset Information")
print("=" * 50)
df.info()

print("\n")

print("=" * 50)
print("Missing Values")
print("=" * 50)
print(df.isnull().sum())

print("\n")

print("=" * 50)
print("Duplicate Rows")
print("=" * 50)
print(df.duplicated().sum())

print("Dataset loaded successfully")