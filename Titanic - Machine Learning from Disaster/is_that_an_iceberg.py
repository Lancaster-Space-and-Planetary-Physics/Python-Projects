# === _is_that_an_iceberg ======================================================
# Joe's futile attempts at predicting passenger survival onboard the Titanic
# using machine learning tools.
# 26 March 2021
# ==============================================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

train_df = pd.read_csv('/Users/kinrade/Repos/Python-Projects/Titanic - Machine Learning from Disaster/data/train.csv')
index = train_df.index      # extract dataframe components into variables
cols  = train_df.columns
vals  = train_df.values
print(cols)                 # show column names

# Get the number of rows and columns
nrows = train_df.shape[0]
print('Total number of passengers:',nrows)
ncols = train_df.shape[1]

# Isolate single column as new Series object:
cabs = train_df['Cabin']
# Isolate single column as new DataFrame:
cabs_df = train_df[['Cabin']]

# Isolate several columns in a new dataframe
name_fare_age = train_df[['Name','Fare','Age']]

# Selecting rows ---------------------------------------------------------------

# # Get single row as a series e.g. first passenger on manifesto:
# pax_one = train_df.loc[0]
# print(pax_one)
#
# # Get multiple rows in a new dataframe e.g. first three passengers:
# pax_123 = train_df.loc[[0,1,2]]
# print(pax_123)
#
# # Use slicing to get multiple rows e.g. pax 10-20:
# pax10_20 = train_df.loc[10:20]
# print(pax10_20)
#
# # Use slicing to get first 5 passengers:
# pax1_5 = train_df.loc[:5]
# print(pax1_5)
#
# # And the last 5 passengers (note use of iloc!):
# pax_end5 = train_df.iloc[-5:]
# pax_end5 = train_df.loc[nrows-5:]
# print(pax_end5)

# Selecting rows and columns ---------------------------------------------------

# Select a slice of rows and single column:
# pax_123_names = train_df.loc[:3,'Name']
# print(pax_123_names)
#
# # Select slice of rows and multiple columns:
# pax_end5_names_embarked = train_df.loc[nrows-5:,['Name','Embarked']]
# print(pax_end5_names_embarked)
#
# # A single row and column returns a single value:
# pax_one_age = train_df.loc[0,'Age']
# print(pax_one_age)

# Conditional selection (more useful) ------------------------------------------

# Select only passengers who embarked in Southampton:
pax_southampton = train_df[train_df['Embarked'].isin(['S'])]
# print no. of pax embarked at southampton:
print(pax_southampton.shape[0])

# How do I plot ticket fare in Southampton versus elsewhere?

S_fares = train_df['Fare'][train_df['Embarked'].isin(['S'])]
C_fares = train_df['Fare'][train_df['Embarked'].isin(['C'])]
Q_fares = train_df['Fare'][train_df['Embarked'].isin(['Q'])]

plt.figure()
kwargs = dict(bins=[0,50,100,150,200,250,300,350,400,450,500,550],
              histtype='bar',orientation='horizontal')#, density=True, stacked=True)
plt.hist([S_fares,C_fares,Q_fares],**kwargs,label=['S','C','Q'],log = 'True')
# plt.hist(C_fares,**kwargs,label='C')
# plt.hist(Q_fares,**kwargs,label='Q')
plt.ylabel('Fare (USD)')
plt.xlabel('No. of pax')
plt.legend()

plt.show()





# # Example plot: Passenger class versus Fare paid.
# train_df.plot.scatter(x="Pclass", y="Fare")
# plt.show()
#
#
# # Locating data based on criteria using dataframe indexing. Who paid the most
# # money for a ticket?
# high_rollers = train_df.loc[train_df.Fare == max(train_df.Fare)]
# print(high_rollers.Name)
