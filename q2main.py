import pandas as pd
from load_data import load_all_data
from seasonal_average import seasonal_average
from temperature_range import temperature_range

MONTHS = ["January","February","March","April","May","June",
          "July","August","September","October","November","December"]

def temperature_stability(df):
    melted = df.melt(id_vars=["STATION_NAME"], value_vars=MONTHS,
                     var_name="Month", value_name="Temp")
    stds = melted.groupby("STATION_NAME")["Temp"].std()

    min_std = stds.min()
    max_std = stds.max()
    stable = stds[stds == min_std]
    variable = stds[stds == max_std]

    with open("temperature_stability_stations.txt","w") as f:
        for station, s in stable.items():
            f.write(f"Most Stable: {station}: StdDev {s:.1f}°C\n")
        for station, s in variable.items():
            f.write(f"Most Variable: {station}: StdDev {s:.1f}°C\n")

def main():
    df = load_all_data("temperatures")
    df[MONTHS] = df[MONTHS].apply(pd.to_numeric, errors="coerce")

    seasonal_average(df)
    temperature_range(df)
    temperature_stability(df)

    print("Analysis complete. Results saved to text files.")

if __name__ == "__main__":
    main()
    input("Press Enter to exit...")
