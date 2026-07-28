import pandas as pd
df=pd.read_csv("auto-mpg.csv")
sorted_df=df.sort_values(by='mpg',ascending=False)
print(sorted_df)
