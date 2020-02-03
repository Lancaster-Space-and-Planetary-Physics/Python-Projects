#HGT Files at https://dds.cr.usgs.gov/srtm/version1/Eurasia/

import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-white')
SAMPLES = 1201 # Change this to 3601 for SRTM1


def read_elevation_from_file(hgt_file, lon, lat):
    with open(hgt_file, 'rb') as hgt_data:
        # Each data is 16bit signed integer(i2) - big endian(>)
        elevations = np.fromfile(hgt_data, np.dtype('>i2'), SAMPLES*SAMPLES)\
                                .reshape((SAMPLES, SAMPLES))

        lat_row = int(round((lat - int(lat)) * (SAMPLES - 1), 0))
        lon_row = int(round((lon - int(lon)) * (SAMPLES - 1), 0))

        #return elevations[SAMPLES - 1 - lat_row, lon_row].astype(int)
        return elevations
    
#each file is a 1201 x 1201 grid array
#at each tile, 'data' is the returned elevation from the file
#starting in the bottom left corner, and going along each row, store the elevation...
#then go onto the next row, and store the data again...
        


hgt_file = '/Users/James/Desktop/lunchtime_spp_python/Contour_Mapping/N54W003.hgt'

lon = 3.
lat = 54.
contour_data = read_elevation_from_file(hgt_file,lon,lat)
contour_data = np.array(contour_data,dtype=float)

#needs converting to a floating np array to remove bad data... (set to NaN)

for i in range(0,1201):
    for j in range(0,1201):
       if (contour_data[j,i] < -32000):
           contour_data[j,i] = np.nan 
           #remove bad data
           
       if (contour_data[j,i] < 0):
           contour_data[j,i] = -200
           #if it is below sea level, let's set it to a negative value
           


for i in range(0,1201):
    reversed_contour_y = contour_data[::-1,i]
    contour_data[::,i] = reversed_contour_y
    
    
#there was a small issue where, for some reason the data was flipped in y - probably to do with the
#way in which it was read in. So I had to reverse the values at each x coordinate in each cell



delta_neg = -1.0/1201
delta = 1.0/1201

x = np.arange(3, 2, delta_neg)   #go from 3 to 2 in 1/1201 steps
y = np.arange(54,55, delta)   


X, Y = np.meshgrid(x, y)  #making our grid


        
contours = plt.contour(X, Y, contour_data, 3, colors='black')  #plot data and contour lines
plt.clabel(contours, inline=True, fontsize=8) #label the contour lines

plt.imshow(contour_data, extent=[3,2, 54, 55], origin='lower',
           cmap='terrain', alpha=0.5)   #display data as an image with a colour map


plt.xlabel('Longitude (Degrees)',fontsize = 15)
plt.ylabel('Latitude (Degrees)',fontsize = 15)

plt.annotate('Lancaster',(2.8,54.05),fontsize = 12,color = 'red')
plt.annotate('Forest of Bowland',(2.6,54.1),fontsize = 12,color = 'red')
plt.annotate('Carlisle',(2.93,54.89),fontsize = 12,color = 'red')
plt.annotate('Yorkshire Dales',(2.2,54.08),fontsize = 12,color = 'red')
plt.annotate('Lake District',(2.8,54.55),fontsize = 12,color = 'red')
plt.annotate('North Pennines',(2.2,54.9),fontsize = 12,color = 'red')


cbar = plt.colorbar(boundaries=np.linspace(-50,800, 18));   #colour bar from -50 to 800 in 18 steps
cbar.set_label('Elevation Above Sea-Level (m)',fontsize = 15)

