import pandas as pd
df1 = pd.read_csv("Auto(1).csv")
df2 = pd.read_csv("auto-mpg(1).csv")
df2.rename(columns={
    "model year": "year",
    "car name": "name"
}, inplace=True)
print("First DataFrame")
print(df1)
print("\nSecond DataFrame")
print(df2)
