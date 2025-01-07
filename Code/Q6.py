import pandas as pd
import numpy as np
cleaned_dataset = pd.read_csv("cleaned_wmbr.csv")
df = pd.DataFrame(cleaned_dataset)
Live_songs = df["Song"].str.contains("live @ Wmbr", case=False, na=False) | df["Album"].str.contains("live", case=False, na=False)
Live_songs = df[Live_songs].reset_index(drop=True)
#print(Live_songs)

Live_songs.to_csv("Q6.csv")