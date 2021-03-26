# === _is_that_an_iceberg ======================================================
# Joe's futile attempts at predicting passenger survival onboard the Titanic
# using machine learning tools.
# 26 March 2021
# ==============================================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

train_data = pd.read_csv('/Users/kinrade/Repos/Python-Projects/Titanic - Machine Learning from Disaster/data/train.csv')
print(train_data.head())

# plt.figure()
train_data.plot.scatter(x="Pclass", y="Fare")
plt.show()


# women = train_data.loc[train_data.Sex == 'female']

pcl = train_data.loc[train_data.Fare == max(train_data.Fare)]
print(pcl)

# train_data.loc[train_data['Name'] == train_data['Fare'].max()]
