import pandas as pd
import gmplot
import matplotlib.pyplot as plt
import numpy as np
from dateutil.parser import parse
import googlemaps

raw_data= pd.read_csv("metro-bike-share-trip-data.csv")

#Creates histogram of ride durations
values= raw_data['Duration']/60

# the histogram of the data
plt.hist(values, bins=100, range=(0, 125))
plt.axvline(np.mean(values), color='k', linestyle='dashed', linewidth=1)
plt.xlabel('Ride Duration (minutes)')
plt.ylabel('Number of Rides')
plt.title('Frequency of Ride Duration')
plt.savefig('hello/static/histogram.png')

print(np.mean(values))
