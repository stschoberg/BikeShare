import pandas as pd
import gmplot
import matplotlib.pyplot as plt
import numpy as np
from dateutil.parser import parse
import googlemaps

#Creates piechart of types of memberships
# Pie chart, where the slices will be ordered and plotted counter-clockwise:

raw_data= pd.read_csv("metro-bike-share-trip-data.csv")

#Counts occurances of each memberships
counts= raw_data['Plan Duration'].value_counts()

labels = 'Yearly memberships', 'Daily Memberships', 'Monthly Memberships'
sizes = [counts[365], counts[0], counts[30]]
explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.savefig('~/hello/static/membership_pie_chart.png')
