import pandas as pd

with open("wmbr.txt", "r") as file:
    data = file.readlines()

parsed_data = []
for row in data:
    # Split each row into key&value pairs
    row_data = {}
    fields = row.strip().split("/")
    for field in fields:
        if ':' in field:
           key, value = field.split(":", 1)  
           row_data[key.strip()] = value.strip()
    parsed_data.append(row_data)
    
df = pd.DataFrame(parsed_data)

df.to_csv("cleaned_wmbr.csv", index=False)

cleaned_dataset = pd.read_csv("cleaned_wmbr.csv")
unique_artists = cleaned_dataset["Artist"].unique()
print(unique_artists)