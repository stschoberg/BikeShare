import pandas as pd
import gmplot
import matplotlib.pyplot as plt
import numpy as np
from dateutil.parser import parse
import googlemaps


raw_data= pd.read_csv("metro-bike-share-trip-data.csv")
start_lats= raw_data['Starting Station Latitude'].astype(float).dropna()
start_longs= raw_data['Starting Station Longitude'].astype(float).dropna()
end_lats= raw_data['Ending Station Latitude'].astype(float).dropna()
end_longs= raw_data['Ending Station Longitude'].astype(float).dropna()


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

plt.cla()
plt.clf()
# Gets distance traveled and plots to histogram
print('accesing api clinet')
gmaps = googlemaps.Client(key='AIzaSyCBJ5kRHDzEfzD4Hh6iEt2xkh4L3ZGNgxg')
print('success')
distances=[]
for i in xrange(0, 1000):
    if (start_lats[i] != 0 and end_lats[i] != 0):
        origin= (start_lats[i], start_longs[i])
        destination= (end_lats[i], end_longs[i])
        result = gmaps.distance_matrix(origin, destination, mode='bicycling')["rows"][0]["elements"][0]["distance"]["value"]
        distances.append(float(result)/1000)
        print(float(result)/1000)
        print(i)


plt.hist(distances, bins=100, range=(0, 5))
plt.xlabel('Ride Length (km)')
plt.ylabel('Number of Rides')
plt.title('Frequency of Ride Length')
plt.savefig('hello/static/ride_length.png')
