#Load native modules
import sys
import os

#Load other modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Add current directory to path
path = os.getcwd()
sys.path.append("{}".format(str(path)))

#Get files from dataset directory
files = os.listdir("datasets\\")

#Read in all datasets
for i in range(0,len(files)):
	       file = files[i].split('.')
	       d[file[0]] = pd.read_csv('datasets\{}'.format(files[i]))
