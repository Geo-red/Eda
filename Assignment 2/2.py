import pandas as pd

df = pd.read_csv("auto-mpg.csv")

print("Last 5 Rows:")
print(df.tail())
