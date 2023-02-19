import pandas as pd
import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from shapely.geometry import Point, Polygon
import contextily as cx


df = pd.read_csv(r'C:\Users\Nico\Desktop\Tesis-teton\ihf.csv')

kings_county_map = gpd.read_file(r'C:\Users\Nico\Desktop\UBB\2022-2\Tesis_windows\Shapefile\Regional.shp')


#df = pd.read_csv('/home/debian/tesis/tkinter/csv/indice_riesgo_hidrico_1979-12-15.csv')
df = df[['lat', 'lon', 'ih']]



#kings_county_map = gpd.read_file('/home/debian/tesis/Shapefile/Regional.shp')
kings_county_map.plot()
kings_county_map.to_crs(epsg=4326).plot()

crs = {'init':'EPSG:4326'}
geometry = [Point(xy) for xy in zip(df['lon'], df['lat'])]
geo_df = gpd.GeoDataFrame(df,
                          crs = crs, 
                          geometry = geometry)



geo_df['ih']
fig, ax = plt.subplots(figsize = (100,40))
kings_county_map.to_crs(epsg=4326).plot(ax=ax, color='lightgrey',alpha=0.5,edgecolor='k')
geo_df.plot(column = 'ih', ax=ax, cmap = 'rainbow',
            legend = True, legend_kwds={'shrink': 0.3}, 
            markersize = 50)
cx.add_basemap(ax)
#cx.add_basemap(ax, source=cx.providers.OpenTopoMap, zoom=12)
#cx.add_basemap(ax, source=cx.providers.OpenTopoMap, zoom=10)
cx.add_basemap(ax, source=cx.providers.CartoDB.Voyager, zoom=12)
cx.add_basemap(ax, source=cx.providers.CartoDB.Voyager, zoom=10)
#cx.add_basemap(ax, crs)


ax.set_title('Indice de Riesgo Hidrico')
plt.savefig('Heat Map')



