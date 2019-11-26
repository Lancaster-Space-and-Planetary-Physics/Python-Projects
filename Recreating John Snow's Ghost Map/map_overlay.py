# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 22:36:41 2019

@author: chris
"""

import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

# read in data
path = "C:/Users/chris/Documents/Lunchtime_python/Python-Projects/Recreating John Snow's Ghost Map/datasets/"
deaths = pd.read_csv(path + "deaths.csv") 
pumps = pd.read_csv(path + "pumps.csv")
dates = pd.read_csv(path + "dates.csv")

# load our saved OS map of london.
OS_map = Image.open("C:/Users/chris/Documents/Lunchtime_python/Python-Projects/Recreating John Snow's Ghost Map/London_OS_map_1893.png")

# display the map
fig = plt.figure()
ax = fig.add_subplot(111)
ax.imshow(OS_map)

# Using our figure, and the OS map found here: 
# https://maps.nls.uk/geo/explore/#zoom=16.023247652414494&lat=51.5130&lon=-0.1373&layers=163&b=1
# We should define some reference points in order to scale our data onto the map.

# We will use the square at ~(950x, 550y) to construct our reference grid and 
# convert our x,y data coordinates to image coordinates.
