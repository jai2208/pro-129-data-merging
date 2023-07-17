import pandas as pd

df = pd.read_csv("dwarf_stars.csv")
df2 = pd.read_csv("scraped_data.csv")

df.dropna(inplace=True)

df['Mass'] = df['Mass'].astype(float)
df['Radius'] = df['Radius'].astype(float)

df['Radius'] = df['Radius']*0.102763
df['Mass'] = df['Mass']*0.000954588

df.to_csv('main.csv' , index=True, index_label="id")

merged_df = pd.merge(df , df2 , on="id")

merged_df.to_csv("merged_data.csv", index=True, index_label="id")