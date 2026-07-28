import pandas as pd
df = pd.read_csv("auto-mpg.csv")
df["horsepower"] = pd.to_numeric(df["horsepower"], errors="coerce")
df["Power_to_Weight"] = df["horsepower"] / df["weight"]
print(df)
