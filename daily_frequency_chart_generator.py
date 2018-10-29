import pandas as pd
import gmplot
import matplotlib.pyplot as plt
import numpy as np
from dateutil.parser import parse
import googlemaps

raw_data= pd.read_csv("metro-bike-share-trip-data.csv")


# Creates histogram to display frequency of rides by days of the week
dates= raw_data['Start Time'].dropna()
day_values= [0,1,2,3,4,5,6]
day_totals= [0,0,0,0,0,0,0]
DAYS= ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

for date in dates:
    date_parsed= parse(date)
    day_totals[date_parsed.weekday()]= day_totals[date_parsed.weekday()] + 1



plt.bar(day_values, day_totals, align='center')
plt.xticks(day_values, DAYS)
plt.title('Rental Frequency by Day of the Week')
plt.ylim([15000, 21000])


plt.savefig('/hello/static/weekday.png')
