import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

dates_data = pd.read_csv('/Users/James/Desktop/lunchtime_spp_python/Python-Projects/Recreating_John Snows_Ghost_Map/datasets/dates.csv',delimiter = ',')
death_data = pd.read_csv('/Users/James/Desktop/lunchtime_spp_python/Python-Projects/Recreating_John Snows_Ghost_Map/datasets/deaths.csv',delimiter = ',')
pump_locations = pd.read_csv('/Users/James/Desktop/lunchtime_spp_python/Python-Projects/Recreating_John Snows_Ghost_Map/datasets/pumps.csv',delimiter = ',')
#Setting delimiter = , is important so that the function reading in the file recognises where a 'new' column begins


#type e.g. pump_locations.columns to see what the columns are
pump_x = np.array(pump_locations['X coordinate']) 
#create an array of the 'X_coordinate' column of the pump_locations file named pump_x
#e.g. pump_x[0] - access first element of pump_x


pump_y = np.array(pump_locations['Y coordinate'])


death_x = np.array(death_data['X_coordinate'])
death_y = np.array(death_data['Y_coordinate'])
#we need to do it as an np.array to get it into something we can inevitably plot



#NOTE THAT PUMP_X IS LATITUDE AND PUMP_Y IS LONGITUDE, BUT WE WANT TO PLOT LONGITUDE VS LATITUDE
#SO PLOT PUMP_Y,PUMP_X IN THAT ORDER...

f = plt.figure(1)
plt.scatter(pump_y,pump_x,label='Pump')  #plot the pump y and x coordinates on an axis
plt.scatter(death_y,death_x,label = 'Deaths')  #plot the death y and x coordinates on the same axis
plt.axis([-0.142,-0.130,51.508,51.518])  #define axis size: x0,x1,y0,y1

plt.xlabel("Geographic Longitude (Deg)")  #label y-axis
plt.ylabel("Geographic Latitude (Deg)")  #label y-axis
plt.legend(loc="upper left")
f.show()
#Rather than plt.show(), label each figure individually then do e.g. f.show()


#Let's try to understand more about the location of the deaths...
#Firstly, looking at the latitude...

ordered_deaths_x = sorted(death_x)
ordered_deaths_y = sorted(death_y)  #order the x/y death arrays into ascending order...

#we cant use np.where on a list so need to turn it into an array
ordered_deaths_x_array = np.asarray(ordered_deaths_x)
ordered_deaths_y_array = np.asarray(ordered_deaths_y)

#Check the max and min values of the array and then begin to bin...


bin1 = np.where((ordered_deaths_x_array > 51.511) & (ordered_deaths_x_array <= 51.512))
bin_1_freq = len(ordered_deaths_x_array[bin1])
#see how many points (deaths) lie between latitudes of 51.511 and 51.512
#save that number



bin2 = np.where((ordered_deaths_x_array > 51.512) & (ordered_deaths_x_array <= 51.513))
bin_2_freq = len(ordered_deaths_x_array[bin2])

bin3 = np.where((ordered_deaths_x_array > 51.513) & (ordered_deaths_x_array <= 51.514))
bin_3_freq = len(ordered_deaths_x_array[bin3])

bin4 = np.where((ordered_deaths_x_array > 51.514) & (ordered_deaths_x_array <= 51.515))
bin_4_freq = len(ordered_deaths_x_array[bin4])

bin5 = np.where((ordered_deaths_x_array > 51.515) & (ordered_deaths_x_array <= 51.516))
bin_5_freq = len(ordered_deaths_x_array[bin5])


latitude_bins = ['51.511 to 51.512','51.512 to 51.513','51.513 to 51.514','51.514 to 51.515','51.515 to 51.516']
x = np.arange(len(latitude_bins))
y = [bin_1_freq,bin_2_freq,bin_3_freq,bin_4_freq,bin_5_freq]


g = plt.figure(2)
plt.bar(x,y,align='center', alpha=0.5)
plt.xticks(x,latitude_bins)
plt.xlabel('Latidudinal Range')
plt.ylabel('Frequency (No of Deaths)')

#What I've basically done here is a really convoluted way of making a histogram..
g.show()



#Next, looking at the longitudes...

bin6 = np.where((ordered_deaths_y_array > -0.141) & (ordered_deaths_y_array <= -0.140))
bin_6_freq = len(ordered_deaths_y_array[bin6])

bin7 = np.where((ordered_deaths_y_array > -0.140) & (ordered_deaths_y_array <= -0.139))
bin_7_freq = len(ordered_deaths_y_array[bin7])

bin8 = np.where((ordered_deaths_y_array > -0.139) & (ordered_deaths_y_array <= -0.138))
bin_8_freq = len(ordered_deaths_y_array[bin8])

bin9 = np.where((ordered_deaths_y_array > -0.138) & (ordered_deaths_y_array <= -0.137))
bin_9_freq = len(ordered_deaths_y_array[bin9])

bin10 = np.where((ordered_deaths_y_array > -0.137) & (ordered_deaths_y_array <= -0.136))
bin_10_freq = len(ordered_deaths_y_array[bin10])


bin11 = np.where((ordered_deaths_y_array > -0.136) & (ordered_deaths_y_array <= -0.135))
bin_11_freq = len(ordered_deaths_y_array[bin11])


bin12 = np.where((ordered_deaths_y_array > -0.135) & (ordered_deaths_y_array <= -0.134))
bin_12_freq = len(ordered_deaths_y_array[bin12])


bin13 = np.where((ordered_deaths_y_array > -0.134) & (ordered_deaths_y_array <= -0.133))
bin_13_freq = len(ordered_deaths_y_array[bin13])

bin14 = np.where((ordered_deaths_y_array > -0.133) & (ordered_deaths_y_array <= -0.132))
bin_14_freq = len(ordered_deaths_y_array[bin14])



long_bins = ['-0.141 to -0.140','-0.140 to -0.139','-0.139 to -0.138', '-0.138 to -0.137','-0.137 to -0.136','-0.136 to -0.135', '-0.135 to -0.134', '-0.134 to -0.133','-0.133 to -0.132']
x = np.arange(len(long_bins))
y = [bin_6_freq,bin_7_freq,bin_8_freq,bin_9_freq,bin_10_freq,bin_11_freq,bin_12_freq,bin_13_freq,bin_14_freq]


k = plt.figure(3)
plt.bar(x,y,align='center', alpha=0.5,color = 'red')
plt.xticks(x,long_bins)
plt.xlabel('Longitudinal Range')
plt.ylabel('Frequency (No of Deaths)')

k.show()







#OR, IF WE WANT TO DO IT USING THE HISTOGRAM FUNCTION: SEE BELOW
#LET'S DO OUR LONGITUDE PLOT AGAIN BUT USING HISTOGRAMS...


binwidth = 0.001

h = plt.figure(4)
#plt.hist(ordered_deaths_y_array, bins=range(min(ordered_deaths_y_array), max(ordered_deaths_y_array) + binwidth, binwdith = 0.001))
#THE ABOVE COMMENTED OUT STATEMENT ONLY WORKS WHEN WE ARE USING INTEGERS...OTHERWISE WE HAVE TO USE THE BELOW ONE

plt.hist(ordered_deaths_y_array, bins=np.arange(min(ordered_deaths_y_array), max(ordered_deaths_y_array) + binwidth, binwidth),color = 'blue',edgecolor = 'black')
plt.xlabel('Longitude Bins')
plt.ylabel('Frequency (No of Deaths)')
h.show()







#Maybe now we want to make it into a density plot?

s = plt.figure(5)
sns.distplot(ordered_deaths_y_array, hist=True, kde=True, 
             bins=np.arange(min(ordered_deaths_y_array), max(ordered_deaths_y_array) + binwidth, binwidth), color = 'darkblue', 
             hist_kws={'edgecolor':'black'},
             kde_kws={'linewidth': 4})
plt.xlabel('Longitude Bins')
plt.ylabel('Frequency (No of Deaths)')

s.show()




#Now let's try and make a time series plot of the attacks and deaths...

time = np.array(dates_data['date'])
attacks = np.array(dates_data['attacks'])
deaths = np.array(dates_data['deaths'])



t = plt.figure(6)
plt.plot(time,attacks,color = 'red')
plt.plot(time,deaths,color = 'black')
plt.xticks(plt.xticks()[0],time,rotation = 90)
plt.tight_layout()
plt.xlabel('Date')
plt.ylabel('Attacks (Red), Deaths (Black)')
t.show()



