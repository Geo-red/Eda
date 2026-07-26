import pandas as pd

df1 = pd.read_csv("Auto(1).csv")
df2 = pd.read_csv("auto-mpg(1).csv")

df2.rename(columns={
    "model year": "year",
    "car name": "name"
}, inplace=True)

vertical_concat = pd.concat([df1, df2], ignore_index=True)

print("Vertical Concatenation")
print(vertical_concat)

print("\nShape of the New DataFrame:")
print(vertical_concat.shape)
