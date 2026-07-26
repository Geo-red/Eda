import pandas as pd

df = pd.read_csv("Auto(1).csv")

new_df = df[["mpg", "cylinders", "horsepower", "weight"]]

print("Original DataFrame")
print(new_df.head())

stacked = new_df.stack()

print("\nStacked DataFrame")
print(stacked)
