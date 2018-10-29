import pandas as pd
import gmplot
import matplotlib.pyplot as plt
import numpy as np
from dateutil.parser import parse


raw_data= pd.read_csv("metro-bike-share-trip-data.csv")
start_lats= raw_data['Starting Station Latitude'].astype(float).dropna()
start_longs= raw_data['Starting Station Longitude'].astype(float).dropna()

#Creates heatmap based on starting longs/lats, Centered on LA
#Saves heatmap to mymap.html file
start_lats.dropna()
start_longs.dropna()


#print(start_lats.value_counts())
heat_map = gmplot.GoogleMapPlotter(34.0522, -118.2473, 13)
heat_map.heatmap(start_lats, start_longs)
heat_map.draw("mymap.html")

#Creates piechart of types of memberships
# Pie chart, where the slices will be ordered and plotted counter-clockwise:

#Counts occurances of each memberships
counts= raw_data['Plan Duration'].value_counts()

labels = 'Yearly memberships', 'Daily Memberships', 'Monthly Memberships'
sizes = [counts[365], counts[0], counts[30]]
explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.savefig('hello/static/membership_pie_chart.png')

plt.cla()
plt.clf()
#Creates histogram of ride durations
values= raw_data['Duration']/60

# the histogram of the data
plt.hist(values, bins=100, range=(0, 125))
plt.xlabel('Ride Duration (hours)')
plt.ylabel('Number of Rides')
plt.title('Frequency of Ride Duration')
plt.savefig('hello/static/histogram.png')

plt.cla()
plt.clf()
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


plt.savefig('hello/static/weekday.png')
