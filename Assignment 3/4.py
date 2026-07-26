import pandas as pd

df1 = pd.read_csv("Auto(1).csv")
df2 = pd.read_csv("auto-mpg(1).csv")

df2.rename(columns={
    "model year": "year",
    "car name": "name"
}, inplace=True)

merged_df = pd.merge(df1, df2, on="mpg")

print("Merged DataFrame")
print(merged_df)

print("\nShape of Merged DataFrame:")
print(merged_df.shape)
