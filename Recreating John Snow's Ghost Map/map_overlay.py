# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 22:36:41 2019

@author: chris

Improvements to be made:
- Use all 4 coordinate points to get an average dlon/dx and average dlat/dy 
  which would be more accurate / correct the offset? 
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
d_p = pd.read_csv(path + "deaths_and_pumps.csv")
# load our saved OS map of london.
OS_map = Image.open("C:/Users/chris/Documents/Lunchtime_python/Python-Projects/Recreating John Snow's Ghost Map/London_OS_map_1893_2.png")
# Convert OS_map to an array to get exact coordinates
arr = np.asarray(OS_map)
# display the map
fig = plt.figure()
ax = fig.add_subplot(111)
ax.imshow(arr)

# Using our figure, and the OS map found here: 
# https://maps.nls.uk/geo/explore/#zoom=16.023247652414494&lat=51.5130&lon=-0.1373&layers=163&b=1
# We should define some reference points in order to scale our data onto the map.

# We will use the square at ~(1554x, 148y) to construct our reference grid.
# We will use this to convert a lat/lon grid using the pixel coordinates.
# in a diamond form, from top clockwise, the lat/lon values are:

im_latlon = np.array([[-0.1321,51.5157], [-0.1317,51.5151], [-0.1325,51.5149], [-0.1329,51.5154]])
# the corresponding pixel coordinates are:
im_xy = np.array([[1576,103],[1604,170],[1542,198],[1511,127]])
# From this we can conclude that:
ax.scatter(im_xy[:,0],im_xy[:,1], c='k', marker='+')

# get lon/x change
delta_lon = im_latlon[0][0] - im_latlon[1][0]
delta_x = im_xy[0][0] - im_xy[1][0]

# get lat/y change
delta_lat= im_latlon[0][1] - im_latlon[1][1]
delta_y = im_xy[0][1] - im_xy[1][1]

## we now know how a change in lon/lat translates to a change in change in x/y


deaths['dlon'] = deaths['Y coordinate'] - im_latlon[0][0]
deaths['dlat'] = deaths['X coordinate'] - im_latlon[0][1]

deaths['dx'] = (deaths['dlon']/delta_lon)*delta_x
deaths['x'] = im_xy[0][0] + deaths['dx'] # get x coordinate wrt reference point

deaths['dy'] = (deaths['dlat']/delta_lat)*delta_y
deaths['y'] = im_xy[0][1] + deaths['dy'] # get y coordinate wrt reference point

ax.scatter(deaths['x'],deaths['y'],s=15,c='r',alpha=0.2, label='death') # plot the death data

pumps['dlon'] = pumps['Y coordinate'] - im_latlon[0][0]
pumps['dlat'] = pumps['X coordinate'] - im_latlon[0][1]

pumps['dx'] = (pumps['dlon']/delta_lon)*delta_x
pumps['x'] = im_xy[0][0] + pumps['dx'] # get x coordinate wrt reference point

pumps['dy'] = (pumps['dlat']/delta_lat)*delta_y
pumps['y'] = im_xy[0][1] + pumps['dy'] # get y coordinate wrt reference point

ax.scatter(pumps['x'],pumps['y'],s=25,c='b',marker='d', label = 'pump') # plot the death data
ax.legend()