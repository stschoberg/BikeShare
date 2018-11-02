# Sam Schoberg, 2018
#
# This script reads in bikeshare data and
# creates a histogram plotting the number
# of rides per day of the week to determine
# which days are most popular for bikesharing
# trips.

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from dateutil.parser import parse

# Read in data to DataFrame 
raw_data= pd.read_csv("metro-bike-share-trip-data.csv")
save_file= "../hello/static/weekday.png"

# Gets ride start time data and drops NULL values
dates= raw_data['Start Time'].dropna()
day_values= [0,1,2,3,4,5,6]
day_totals= [0,0,0,0,0,0,0]
DAYS= ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
        'Saturday', 'Sunday']

for date in dates:
    # Parse the date structure given
    date_parsed= parse(date)
    # Increment that days total rides
    day_totals[date_parsed.weekday()]= day_totals[date_parsed.weekday()] + 1


# Formatting for chart
plt.bar(day_values, day_totals, align='center')
plt.xticks(day_values, DAYS)
plt.title('Rental Frequency by Day of the Week')
plt.ylim([15000, 21000])

# Save to file
plt.savefig(save_file)
print("Image created. Saved to", save_file)
