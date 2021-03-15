# === iom_forests.py ===========================================================
# Play with some SAR-based forest coverage maps from DLR:
# https://www.dlr.de/hr/en/desktopdefault.aspx/tabid-12538/21873_read-50027/
# Data download GUI: https://download.geoservice.dlr.de/FNF50/
# Data format is a 'GeoTIFF' raster file, readable by rasterio:
# https://rasterio.readthedocs.io/en/stable/

# Joe Kinrade - 5 December 2019 ================================================
import rasterio
import matplotlib.pyplot as plt

# Load file covering the Isle of Man:
forest_file = '/Users/kinrade/Documents/Isle_of_Man/Manx_mounds/SRTM/FNF/TDM_FNF_20_N54W005/FNF/TDM_FNF_20_N54W005.tiff'

dataset = rasterio.open(forest_file)
band1 = dataset.read(1)                 # raster file data accessed by an index
plt.figure()
plt.imshow(band1,cmap='gist_earth')
plt.show()
