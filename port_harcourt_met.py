import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'data/Port Harcourt Met Data.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    #Get the average temperature
    dates, temps = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            temp = float(row[4])
        except ValueError:
            print(f"Missing data on {current_date}")
        else:
            dates.append(current_date)
            temps.append(temp)

#Plot the temperature using seaborn
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, temps, c='red', alpha=0.5)

#Format the plot
plt.title("Average Temperature in Port Harcourt, 2020 to 2022", fontsize=18)
plt.xlabel("Dates", fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Average Temperature (Celsius)", fontsize=16)      
plt.tick_params(axis='both', which='major', labelsize=14) 

plt.show()