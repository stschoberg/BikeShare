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

print(start_lats.value_counts())
print(start_longs.value_counts())


heat_map = gmplot.GoogleMapPlotter(34.0522, -118.2473, 13)
heat_map.heatmap(start_lats, start_longs)
heat_map.draw("mymap.html")
