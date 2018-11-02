# Sam Schoberg, 2018
#
# This script reads in bikeshare data and
# creates a histogram plotting the distribution
# of the ride duration in minutes.

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

raw_data= pd.read_csv("metro-bike-share-trip-data.csv")
save_file= '../hello/static/histogram.png'
# Standardizes to minutes
values= raw_data['Duration']/60

# Formats histogram
plt.hist(values, bins=100, range=(0, 125))
# Prints mean line
plt.axvline(np.mean(values), color='k', linestyle='dashed', linewidth=1)
# Prints median line
plt.axvline(np.median(values), color='red', linestyle='dashed', linewidth=1)
plt.xlabel('Ride Duration (minutes)')
plt.ylabel('Number of Rides')
plt.title('Frequency of Ride Duration')

plt.savefig(save_file)
print("Image created. Saving to", save_file)
