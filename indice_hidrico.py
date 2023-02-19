# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 16:23:55 2022

@author: Nico
"""

from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap



data = Dataset(r'C:\Users\Nico\Desktop\UBB\2022-2\Proyecto de título\ArchivosNetCDF\INDICE_HIDRICO_REGION_NUBLE05-2000.nc')

lats = data.variables['lat'][:]
lons = data.variables['lon'][:]
ih = data.variables['ih'][:]

# urcrnrlat = upper corner latitude
# llcrnrlat = lower corner latitude
# the same for longitude


mp = Basemap( projection= 'merc',
             llcrnrlon = -74.12781716194432,  
             llcrnrlat = -39.56411594239592,
             urcrnrlon = -69.91944506776058,  
             urcrnrlat = -34.48729972248022,
             resolution = 'f')

plt.rcParams["figure.figsize"] = (12, 12)

lon, lat = np.meshgrid(lons, lats)
x, y = mp(lon, lat)

c_scheme = mp.pcolor(x, y, np.squeeze(ih[:, :]), cmap= 'jet')
mp.drawstates()
mp.drawcountries()

mp.drawcoastlines()
mp.drawlsmask(land_color='#a7a7a7', ocean_color='#fafbfd', lakes=True)
mp.drawrivers()
mp.warpimage()

cbar = mp.colorbar(c_scheme, location = 'right', pad= '10%')


plt.title('Indice hidrico de la region de  Ñuble del año 2000')
plt.show()