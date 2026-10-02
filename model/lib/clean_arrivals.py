import pandas as pd
from pathlib import Path

df_list = []
dir_path = Path('data/raw/')
prefix = 'den-arrivals-'
for file_path in dir_path.glob(f"{prefix}*"):
    if file_path.is_file():
        df = pd.read_csv(file_path, skiprows=7, on_bad_lines='skip')
        df = df[df["Carrier Code"].str.len() == 2]
        df_list.append(df)

combined_df = pd.concat(df_list, ignore_index=True)            

combined_df.to_csv("data/clean/den-arrivals-cleaned.csv", index=False)