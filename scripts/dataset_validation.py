import pandas as pd

# Load dataset
df = pd.read_csv("data/FPGA_Reddit_Dataset_1_222.csv")

# Standardize column names
df.columns = (
    df.columns
      .str.strip()
      .str.lower()
)

print("=" * 60)
print("DATASET SUMMARY")
print("=" * 60)

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nUnique Labels:")
print(df["label"].unique())

print("\nLabel Counts:")
print(df["label"].value_counts())

print("\nLabel Percentages:")
print(
    (df["label"]
       .value_counts(normalize=True)
       * 100)
       .round(2)
)

print("\nFirst Five Rows:")
print(df.head())

print("\nLast Five Rows:")
print(df.tail())