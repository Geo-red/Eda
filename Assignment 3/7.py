import pandas as pd

df1 = pd.read_csv("Auto(1).csv")
df2 = pd.read_csv("auto-mpg(1).csv")

df2.rename(columns={
    "model year": "year",
    "car name": "name"
}, inplace=True)

outer_join = pd.merge(df1, df2, on="mpg", how="outer")

print("Outer Join")
print(outer_join)

print("\nShape:")
print(outer_join.shape)
