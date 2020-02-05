# Let’s Get High

In this project we’ll get to grips with mapping some elevation data in python, and see how point coordinates relate to map projections.

<div align="center">
<img src="sweden_contour_graphic.jpeg" alt="Contour map of Sweden" width=200px>
</div>

The first task is to hunt down some open-source landscape elevation data. This can be from anywhere you like, in whatever format you find. LIDAR scans of Lancashire. SAR scans of the grand canyon from space. Lunar craters. Sonar sweeps of the Mariana trench. All that matters is that you can find some altitude data, read them in, and visualise the stuff on a map.

Here are some data sources to get you started:
* **OS OpenData Supply:** Includes a 50 m contour elevation model of the British Isles, plus other ancillary data like river paths and boundary lines.
[https://www.ordnancesurvey.co.uk/opendatadownload/products.html](https://www.ordnancesurvey.co.uk/opendatadownload/products.html)
* **Shuttle Radar Topography Mission:** Global height-above-sea level points based on radar scans from space! Global coverage at 90m resolution, the US at 30m resolution. Fill your boots.
[https://www2.jpl.nasa.gov/srtm/](https://www2.jpl.nasa.gov/srtm/)
* **data.gov.uk:** Portal to the government’s open source data archives. You’ll find LIDAR composite scans on here right down to 25 cm resolution. That’s enough to see the anguish on a second-year PhD student’s face. I’m not telling you where it is, have a root around.
[https://data.gov.uk/](https://data.gov.uk/)
* **DLR Microwaves and Radar Institute:** An example of land-use data that we could combine with elevation data. Radar-derived forest/non-forest maps. Raster map information on tree coverage and urbanised areas. No, I don’t know why the url is so dumb.
[https://www.dlr.de/hr/en/desktopdefault.aspx/tabid-12538/21873_read-50027/](https://www.dlr.de/hr/en/desktopdefault.aspx/tabid-12538/21873_read-50027/)

Here are some potentially helpful Python packages for reading in and mapping data:
* **Geopandas:** [http://geopandas.org](http://geopandas.org)
* **Cartopy:** [https://scitools.org.uk/cartopy](https://scitools.org.uk/cartopy)
* **Rasterio:** [https://rasterio.readthedocs.io/en/latest/](https://rasterio.readthedocs.io/en/latest/)
* **Pyproj:** [https://pypi.org/project/pyproj/](https://pypi.org/project/pyproj/)

What are we going to do with all this glorious height information? Whatever we like. Find the closest pub using cycle paths only. Work out how safe your house is from sealevel rises. Make cool designs for t-shirts automatically from a webscript. This’ll hopefully be a fun bit that develops as we go along.
