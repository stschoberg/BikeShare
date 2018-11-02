# Sam Schoberg, 2018
#
# This script reads in bikeshare data and
# creates a histogram plotting distribution
# of the length of rides in km using the
# Google Maps Distance Matrix API.

import pandas as pd
import gmplot
import matplotlib.pyplot as plt
import numpy as np
import googlemaps

# Reads in data and selects relevant columns, drops NULL values
raw_data= pd.read_csv("metro-bike-share-trip-data.csv")
start_lats= raw_data['Starting Station Latitude'].astype(float).dropna()
start_longs= raw_data['Starting Station Longitude'].astype(float).dropna()
end_lats= raw_data['Ending Station Latitude'].astype(float).dropna()
end_longs= raw_data['Ending Station Longitude'].astype(float).dropna()
distances=[]
save_file= '../hello/static/ride_length.png'

# Gets distance traveled and plots to histogram
print("Attempting to accessing Google API")
gmaps = googlemaps.Client(key='AIzaSyCBJ5kRHDzEfzD4Hh6iEt2xkh4L3ZGNgxg')
print("Success")

# For all the data
for i in xrange(0, 1000):
    # Filters empty entries
    if (start_lats[i] != 0 and end_lats[i] != 0):
        origin= (start_lats[i], start_longs[i])
        destination= (end_lats[i], end_longs[i])
        # Calls distance matrix and parses JSON object
        result = gmaps.distance_matrix(origin, destination, mode='bicycling')["rows"][0]["elements"][0]["distance"]["value"]
        # Start/stop stations can't be the same
        if(result != 0):
            distances.append(float(result)/1000)
            print(i, ": Success. API accessed and result appened")

# Chart Formatting
plt.hist(distances, bins=100, range=(0.1, 5))
# Prints mean line
plt.axvline(np.mean(distances), color='k', linestyle='dashed', linewidth=1)
# Prints median line
plt.axvline(np.median(distances), color='red', linestyle='dashed', linewidth=1)
plt.xlabel('Ride Length (km)')
plt.ylabel('Number of Rides')
plt.title('Frequency of Ride Length')

plt.savefig(save_file)
print("Image created. Saved to", save_file)
