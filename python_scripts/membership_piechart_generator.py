# Sam Schoberg, 2018
#
# This script reads in bikeshare data and
# creates a piechart depicting the percentages
# of each membership type.

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


raw_data= pd.read_csv("metro-bike-share-trip-data.csv")
save_file= '../hello/static/membership_pie_chart.png'

#Counts occurances of each memberships
counts= raw_data['Plan Duration'].value_counts()

labels = 'Yearly memberships', 'Daily Memberships', 'Monthly Memberships'
sizes = [counts[365], counts[0], counts[30]]
explode = (0, 0.1, 0, 0)

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.savefig(save_file)
print("Image created. Saved to" save_file)
