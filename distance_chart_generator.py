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
        if(result != 0):
            distances.append(float(result)/1000)

plt.hist(distances, bins=100, range=(0.1, 5))
plt.axvline(np.mean(distances), color='k', linestyle='dashed', linewidth=1)
plt.xlabel('Ride Length (km)')
plt.ylabel('Number of Rides')
plt.title('Frequency of Ride Length')
plt.savefig('hello/static/ride_length.png')
