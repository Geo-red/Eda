import pandas as pd

df1 = pd.read_csv("Auto(1).csv")
df2 = pd.read_csv("auto-mpg(1).csv")

df2.rename(columns={
    "model year": "year",
    "car name": "name"
}, inplace=True)

horizontal_concat = pd.concat([df1, df2], axis=1)

print("Horizontal Concatenation")
print(horizontal_concat)

print("\nShape of the New DataFrame:")
print(horizontal_concat.shape)
