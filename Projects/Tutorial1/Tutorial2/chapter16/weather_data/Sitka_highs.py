from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

path = Path(r'C:\Users\nurop\OneDrive\Desktop\pYTHON COURSE\Projects\Tutorial2\chapter16\weather_data\sitka_weather_2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)



#extract info for high temps
dates, highs, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    high = int(row[4])
    low = int(row[5])
    highs.append(high)
    dates.append(current_date)
    lows.append(low)
    
#plot high&low temps
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='green', alpha=0.1)

#formating the polts
ax.set_title("Daily High & low Temperatures, 2021", fontsize=24)
ax.set_xlabel('Days', fontsize = 16)
fig.autofmt_xdate()
ax.set_ylabel("Temprature (F)", fontsize = 16)
ax.tick_params(labelsize=10)

    
plt.show()