import os
import pandas as pd

MONTHS = ["January","February","March","April","May","June",
          "July","August","September","October","November","December"]

def load_all_data(folder="temperatures"):
    """Load all yearly station CSVs into one DataFrame."""
    dfs = []
    for file in os.listdir(folder):
        if file.endswith(".csv"):
            path = os.path.join(folder, file)
            df = pd.read_csv(path)
            df["Year"] = os.path.splitext(file)[0]  # keep year from filename
            dfs.append(df)
    return pd.concat(dfs, ignore_index=True)

if __name__ == "__main__":
    df = load_all_data("temperatures")
    print("Data loaded successfully with shape:", df.shape)
