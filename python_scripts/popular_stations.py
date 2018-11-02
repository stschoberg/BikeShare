# Sam Schoberg, 2018
#
# This script reads in bikeshare data and
# prints the counts of number of rides at
# various bike start/stop stations in descending
# order to be put into markers on the HTML page
# to mark the most popular start/stop stations.

import pandas as pd

raw_data= pd.read_csv("metro-bike-share-trip-data.csv")
start_lats= raw_data['Starting Station Latitude'].astype(float).dropna()
start_longs= raw_data['Starting Station Longitude'].astype(float).dropna()

# Drops NULL values
start_lats.dropna()
start_longs.dropna()

print(start_lats.value_counts())
print(start_longs.value_counts())
