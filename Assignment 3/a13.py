import pandas as pd

df = pd.read_csv("Auto(1).csv")

series1 = df["mpg"].head(10)
series2 = df["horsepower"].head(10)

multi_series = pd.concat(
    [series1, series2],
    keys=["MPG", "Horsepower"]
)

result = multi_series.unstack()

print("Unstacked MultiIndex")
print(result)
