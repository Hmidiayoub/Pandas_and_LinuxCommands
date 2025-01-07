import pandas as pd
data = pd.read_csv("top2018.csv")
df = pd.DataFrame(data)

data_wmbr = pd.read_csv("cleaned_wmbr.csv")
df2 = pd.DataFrame(data_wmbr)

artists_df1 = set(df["artists"])
artists_df2 = set(df2["Artist"])
top_artists = artists_df1.intersection(artists_df2)
filtered_artists = df[df["artists"].isin(top_artists)]
filtered_artists = filtered_artists[["artists", "name", "danceability"]].reset_index(drop=True)
filtered_artists = filtered_artists.sort_values(by="danceability", ascending=False).reset_index(drop=True)

filtered_artists.to_csv("Q8.csv")

