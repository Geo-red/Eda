import pandas as pd

df = pd.read_csv("Auto(1).csv")

horsepower_series = df["horsepower"]

print("Horsepower Series")
print(horsepower_series)
