"""
Author: Jadon Argo
Course: CSD-325
Assignment: Module 4 – Sitka Weather Visualization
Description:
This program allows users to view either high or low daily temperatures for Sitka, Alaska,
based on 2018 weather data. The user can select from a menu to view either data type,
or choose to exit the program. Highs are displayed in red, and lows in blue.
"""

import csv
import matplotlib.pyplot as plt
from datetime import datetime
import sys

filename = 'sitka_weather_2018_simple.csv'

def read_weather_data():
    """Reads the CSV file and returns dates, highs, and lows."""
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        dates, highs, lows = [], [], []
        for row in reader:
            try:
                current_date = datetime.strptime(row[2], '%Y-%m-%d')
                high = int(row[5])
                low = int(row[6])
            except ValueError:
                continue
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)

        return dates, highs, lows

def plot_graph(dates, temps, label, color):
    """Plots temperatures with appropriate title and color."""
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, temps, c=color)
    title = f"Daily {label.capitalize()} Temperatures - 2018"
    plt.title(title, fontsize=20)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=12)
    plt.show()

# Main menu loop
while True:
    print("\nSitka Weather Viewer")
    print("1. View High Temperatures")
    print("2. View Low Temperatures")
    print("3. Exit")
    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == '3':
        print("Thank you for using the Sitka Weather Viewer. Goodbye!")
        sys.exit()

    dates, highs, lows = read_weather_data()

    if choice == '1':
        plot_graph(dates, highs, "high", "red")
    elif choice == '2':
        plot_graph(dates, lows, "low", "blue")
    else:
        print("Invalid choice. Please select 1, 2, or 3.")
