import pandas as pd

df1 = pd.read_csv("Auto(1).csv")
df2 = pd.read_csv("auto-mpg(1).csv")

series1 = df1["horsepower"]
series2 = df2["horsepower"]

result = pd.concat([series1, series2], ignore_index=True)

print("Concatenated Series")
print(result)
