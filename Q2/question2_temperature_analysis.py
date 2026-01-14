import os
import csv
import math
from collections import defaultdict

# Folder that contains all temperature CSV files
DATA_FOLDER = "temperatures"

# Output files required by the assignment
AVG_FILE = "average_temp.txt"
RANGE_FILE = "largest_temp_range_station.txt"
STABILITY_FILE = "temperature_stability_stations.txt"

# Month names used in the CSV files
MONTHS = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

# Australian seasons and their months
SEASONS = {
    "Summer": ["December", "January", "February"],
    "Autumn": ["March", "April", "May"],
    "Winter": ["June", "July", "August"],
    "Spring": ["September", "October", "November"]
}


def load_all_data():
    """
    Reads all CSV files in the temperatures folder
    and collects valid temperature values.
    """
    all_records = []

    for file in os.listdir(DATA_FOLDER):
        if file.endswith(".csv"):
            path = os.path.join(DATA_FOLDER, file)

            with open(path, newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)

                for row in reader:
                    station = row["STATION_NAME"]

                    # Read monthly temperatures for each station
                    for month in MONTHS:
                        value = row.get(month)

                        # Ignore missing (NaN) values
                        if value and value.lower() != "nan":
                            all_records.append({
                                "station": station,
                                "month": month,
                                "temp": float(value)
                            })

    return all_records


def seasonal_average(data):
    """
    Calculates average temperature for each Australian season
    across all stations and years.
    """
    season_temps = defaultdict(list)

    for record in data:
        for season, months in SEASONS.items():
            if record["month"] in months:
                season_temps[season].append(record["temp"])

    with open(AVG_FILE, "w") as f:
        for season, temps in season_temps.items():
            average = sum(temps) / len(temps)
            f.write(f"{season}: {average:.2f}°C\n")


def largest_temperature_range(data):
    """
    Finds the station(s) with the largest temperature range.
    """
    station_temps = defaultdict(list)

    for record in data:
        station_temps[record["station"]].append(record["temp"])

    max_range = 0
    results = []

    for station, temps in station_temps.items():
        temp_range = max(temps) - min(temps)

        if temp_range > max_range:
            max_range = temp_range
            results = [(station, max(temps), min(temps))]
        elif temp_range == max_range:
            results.append((station, max(temps), min(temps)))

    with open(RANGE_FILE, "w") as f:
        for station, max_t, min_t in results:
            f.write(
                f"{station}: Range {max_t - min_t:.2f}°C "
                f"(Max: {max_t:.2f}°C, Min: {min_t:.2f}°C)\n"
            )


def temperature_stability(data):
    """
    Determines the most stable and most variable stations
    using standard deviation.
    """
    station_temps = defaultdict(list)

    for record in data:
        station_temps[record["station"]].append(record["temp"])

    std_devs = {}

    for station, temps in station_temps.items():
        mean = sum(temps) / len(temps)
        variance = sum((t - mean) ** 2 for t in temps) / len(temps)
        std_devs[station] = math.sqrt(variance)

    min_std = min(std_devs.values())
    max_std = max(std_devs.values())

    with open(STABILITY_FILE, "w") as f:
        for station, value in std_devs.items():
            if value == min_std:
                f.write(f"Most Stable: {station}: StdDev {value:.2f}°C\n")

        for station, value in std_devs.items():
            if value == max_std:
                f.write(f"Most Variable: {station}: StdDev {value:.2f}°C\n")


def main():
    """
    Main program execution.
    """
    data = load_all_data()
    seasonal_average(data)
    largest_temperature_range(data)
    temperature_stability(data)
    print("Temperature analysis completed.")


if __name__ == "__main__":
    main()
