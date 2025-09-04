import numpy as np

SEASON_MAP = {
    "Summer": ["December","January","February"],
    "Autumn": ["March","April","May"],
    "Winter": ["June","July","August"],
    "Spring": ["September","October","November"]
}

def seasonal_average(df):
    results = {}
    for season, months in SEASON_MAP.items():
        values = df[months].values.flatten()
        values = values[~np.isnan(values)]
        results[season] = round(values.mean(), 1)

    with open("average_temp.txt","w") as f:
        for season in ["Summer","Autumn","Winter","Spring"]:
            f.write(f"{season}: {results[season]}°C\n")

if __name__ == "__main__":
    print("seasonal_average function is ready ")
