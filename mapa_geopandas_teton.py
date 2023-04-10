# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
#import numpy as np
import geopandas as gpd
#from pyproj import CRS
import matplotlib.pyplot as plt
from shapely.geometry import Point

df = pd.read_csv(r'C:\Users\Nico\Desktop\UBB\2022-2\Tesis_windows\csv\ih.csv')

df = df[['lat', 'lon', 'ih']]


kings_county_map = gpd.read_file(r'C:\Users\Nico\Desktop\UBB\2022-2\Tesis_windows\Shapefile\Regional.shp')
kings_county_map.plot()
kings_county_map.to_crs(epsg=4326).plot()

crs = {'init':'EPSG:4326'}
#crs=CRS('EPSG:4326')
geometry = [Point(xy) for xy in zip(df['lon'], df['lat'])]
geo_df = gpd.GeoDataFrame(df,
                          crs = crs, 
                          geometry = geometry)

#geo_df.set_crs(epsg=4326, inplace=True)


geo_df['ih']
fig, ax = plt.subplots(figsize = (100,40))
kings_county_map.to_crs(epsg=4326).plot(ax=ax, color='lightgrey')
geo_df.plot(column = 'ih', ax=ax, cmap = 'rainbow',
            legend = True, legend_kwds={'shrink': 0.3}, 
            markersize = 50)
ax.set_title('Indice de Riesgo Hidrico')
plt.savefig('Heat Map')





