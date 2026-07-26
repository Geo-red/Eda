import pandas as pd

df = pd.read_csv("Auto(1).csv")

new_df = df[["mpg", "cylinders", "horsepower", "weight"]]

stacked = new_df.stack()

unstacked = stacked.unstack()

print("Unstacked DataFrame")
print(unstacked)
