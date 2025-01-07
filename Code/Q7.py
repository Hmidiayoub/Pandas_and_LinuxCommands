import pandas as pd
data = pd.read_csv("Q5.csv")
df = pd.DataFrame(data)
print(data.head())
aggre_data = df[df["Artist"] == "Lizzo"].groupby(df['Song']).size().reset_index(name='Count')
aggre_data_sorted = aggre_data.sort_values(by="Count", ascending=False).reset_index(drop=True)
cols = {"Song_name", "num_plays"}
aggre_data_sorted.columns = cols
#print(aggre_data_sorted)
aggre_data_sorted.to_csv("Q7.csv")