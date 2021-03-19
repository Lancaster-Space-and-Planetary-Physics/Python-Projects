# === iom_topo.py ==============================================================
# Read in some elevation data from the Shuttle Radar Topography Mission (STRM)
# and make an elevation map. Read-in code taken from from here:
# https://librenepal.com/article/reading-srtm-data-with-python/
# Data from here: https://dds.cr.usgs.gov/srtm/version2_1/
# STRM1 = 1 arcsecond scans ==> ~ 30 m resolution [1201 samples per tile]
# SRTM3 = 3 arcsecond scans ==> ~ 90 m resolution [3601 samples per tile]

# Joe Kinrade - 2 December 2019 ================================================

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as mpl_cm
import cartopy                                  # import cartopy
import cartopy.mpl.ticker as cticker
import cartopy.crs as ccrs

# Source file - coverage is 1x1 degree tile in lat-lon, specified in the
# filename by the bottom-left location in the tile.
hgt_file='/Users/kinrade/Documents/Isle_of_Man/Manx_mounds/SRTM/SRTM3/N54W005.hgt'
lon = 5.    # bottom left tile longitude (West  in this case)
lat = 54.   # bottom left tile latitude  (North in this case)
# Pixel resolution (1201x1201 for SRTM3, 3601 for SRTM1):
SAMPLES = 1201
# Fake up some lon-lat vectors the length of no. of pixels
lons = np.linspace(-5. , -4., SAMPLES)
lats = np.linspace( 54., 55., SAMPLES)

# This function has been adapted from one that returns a point elevation value
# at a certain lat, lon. Currently they aren't used, but might be useful later.
def read_elevation_from_file(hgt_file, lon, lat):
    """Read in an SRTM elevation file and return an array of point altitudes."""
    with open(hgt_file, 'rb') as hgt_data:
        elevations = np.fromfile(hgt_data, np.dtype('>i2'),
                                 SAMPLES*SAMPLES).reshape((SAMPLES, SAMPLES))
        # lat_row = int(round((lat - int(lat)) * (SAMPLES - 1), 0))
        # lon_row = int(round((lon - int(lon)) * (SAMPLES - 1), 0))
        # return elevations[SAMPLES - 1 - lat_row, lon_row].astype(int)
        return elevations

iom_elv = read_elevation_from_file(hgt_file,lon,lat)
iom_elv[iom_elv == -32768] = 0.     # set bad data flag to 0.0
# Debugging stuff:
# print(type(iom_elv))
# print(np.size(iom_elv))
# print('Shape of data is:')
# print(iom_elv.shape)
# print('Min altitude in file:', np.min(iom_elv))
print('Max altitude in file:', np.max(iom_elv))

# plot image data to check it's been read in properly --------------------------
# plt.figure()                                          # create figure canvas
# plt.contourf(np.flip(iom_elv,axis=0), cmap = "viridis",
#              levels = list(range(0, 750, 50)))
# plt.colorbar()
# plt.show()

# try a map projection ---------------------------------------------------------
levels = np.arange(0, 750, 50)
extend = 'both'

f1 = plt.figure(1)                                      # create figure canvas
ax = f1.add_subplot(111)                                # create axes
ax = plt.axes(projection=cartopy.crs.PlateCarree())     # set projection type
# Set projection lat-lon extents:
# ax.set_extent([-11, 2, 49, 60])                       # ~UK extent
ax.set_extent([-5, -4, 54, 55])                         # ~IOM extent
# ax.set_global()                                       # global extent
# Draw coastlines:
# ax.coastlines(resolution='10m', color='black', linewidth=1)   # Default
coast = cartopy.feature.GSHHSFeature(scale='high')      # hi-res coastline
ax.add_feature(coast, edgecolor='black',linewidth=2)

# contour plot:
iomtopo = ax.contourf(lons,lats, np.flip(iom_elv,axis=0), cmap='terrain',
                       levels=levels, extend=extend,
                       transform=cartopy.crs.PlateCarree())
iomtopo.cmap.set_under('gray')                          # sea level colour
# Sort out ticks and format them to show lat-lon bearings:
ax.set_xticks(np.linspace(-5. , -4., 6), crs=ccrs.PlateCarree())
ax.set_xticklabels(np.linspace(-5. , -4., 6), weight='bold')
ax.set_yticks(np.linspace(54. , 55., 6), crs=ccrs.PlateCarree())
ax.set_yticklabels(np.linspace(54. , 55., 6), weight='bold')
lon_formatter = cticker.LongitudeFormatter()
lat_formatter = cticker.LatitudeFormatter()
ax.xaxis.set_major_formatter(lon_formatter)
ax.yaxis.set_major_formatter(lat_formatter)
# Add gridlines:
ax.grid(linewidth=1, color='black', alpha=0.5, linestyle='-')
# gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
#                   linewidth=1, color='gray', alpha=0.5, linestyle='-')
# Colorbar:
cbar = plt.colorbar(iomtopo, ax=ax, extend='both', pad=0.1)
cbar.set_label('Height above sea level (m)')
cbar.ax.tick_params(width=2)
cbar.outline.set_linewidth(2)

# plt.savefig('elevation_mapping_example.png')
plt.show()


# ==============================================================================
# try sub-sampling the image array and making a stylized, stacked line plot
# This kinda works, but there needs to be some scaling of the height information
# for the extents/aspect ratio of the map if it's going to be automated.

data = np.flip(iom_elv,axis=0)
dataf = data.astype('float64')
dataf[dataf <= 0.] = np.nan
data_h = dataf[::5]        # grab every 12th row
lat_h  = lats[::5]
print(f'data_h dims = {data_h.shape}')
data_v = dataf[:, 1::5]    # grab 12th column
print(f'data_v dims = {data_v.shape}')

f2 = plt.figure(1)                                      # create figure canvas
ax = f2.add_subplot(111)
ax.set_facecolor('xkcd:rust')
for ind in range(0,len(lat_h)):
    plt.plot(lons, lat_h[ind]*10000. + data_h[ind,:],color='xkcd:off white',lw=.75)

plt.annotate('ISLE OF MAN', (0.5,0.45), xycoords='axes fraction', ha='center',
             fontfamily = 'Impact', weight = 'heavy', size= 40, color='xkcd:off white')
# total fudge! - plot some lines over the text annotation
lab_lats = np.linspace(544934 , 546230, 40)
for i in range(0,40):
    plt.axhline(lab_lats[i], color='xkcd:rust', lw = .75, zorder=4)

plt.show()
