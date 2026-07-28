import pandas as pd
df=pd.read_csv("auto-mpg.csv")
print(df['origin'].value_counts())
