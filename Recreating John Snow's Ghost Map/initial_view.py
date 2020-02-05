# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 18:38:22 2019

@author: chris
"""

import datetime
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# read in data
path = os.getcwd()
deaths = pd.read_csv(path + "\\Recreating John Snow's Ghost Map\\datasets\\deaths.csv")
pumps = pd.read_csv(path + "\\Recreating John Snow's Ghost Map\\datasets\\pumps.csv")
dates = pd.read_csv(path + "\\Recreating John Snow's Ghost Map\\datasets\\dates.csv")

# convert dates to datetimes
dates['dt_date'] = [datetime.datetime.strptime(day, "%Y-%m-%d") for day in dates.date]

#plot data associated with dates
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.plot(dates['dt_date'],dates['attacks'], c='k', label = 'Attacks')
ax1.plot(dates['dt_date'],dates['deaths'],c='r', label = 'Deaths')
ax1.legend()
plt.show()

# The sum of the attacks is greater than the sum of deaths in the "dates"
# dataframe. Also the length of the "deaths" dataframe is less than the number
# of deaths in the "dates" dataframe.
print('# deaths in dates: ', np.sum(dates['deaths']))
print('# attacks in dates: ', np.sum(dates['attacks']))
print('length of deaths df: ', len(deaths))

# The max and min x and y coordinates from the dataset
x = [51.510019,51.515834]
y = [-0.140074,-0.132933]
