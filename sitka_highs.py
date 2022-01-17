import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    #Get the high temperatures
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)
        
#Plot the high temperatures using seaborn
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5) #An alpha value of 0 is completely transparent and 1 is completely opaque
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows,facecolor='blue', alpha=0.1)

#Format the plot
plt.title("Daily High and Low Temperatures, 2018", fontsize=24)
plt.xlabel('Dates', fontsize=16)
fig.autofmt_xdate()  #Draws the date labels diagonally to prevent overlapping
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()