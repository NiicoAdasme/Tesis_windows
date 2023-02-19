# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 21:04:54 2022

@author: Nico
"""

from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap


# temperaturas minimas por dia 1979 - 2020 5.1GB
# data = Dataset(r'C:\Users\Nico\Desktop\UBB\2022-2\Proyecto de título\ArchivosNetCDF\CR2\CR2MET_tmin_v2.0_day_1979_2020_005deg.nc')

# temperaturas minimas por mes 1979 - 2018 330MB
#data = Dataset(r'C:\Users\Nico\Desktop\UBB\2022-2\Proyecto de título\ArchivosNetCDF\CR2\CR2MET_tmin_v2.0_mon_1979_2018_005deg.nc')

# temperaturas minimas por mes 1979 - 2019 338MB
data = Dataset(r'C:\Users\Nico\Desktop\UBB\2022-2\Proyecto de título\ArchivosNetCDF\CR2\1979-2019\CR2MET_tmin_v2.0_mon_1979_2019_005deg.nc')

# temperaturas maximas por dia 1979 - 2018 5GB
#data = Dataset(r'C:\Users\Nico\Desktop\UBB\2022-2\Proyecto de título\ArchivosNetCDF\CR2\CR2MET_tmin_v2.0_mon_1979_2019_005deg.nc')



lats = data.variables['lat'][:]
lons = data.variables['lon'][:]
time = data.variables['time'][:]
tmin = data.variables['tmin'][:]

# urcrnrlat = upper corner latitude
# llcrnrlat = lower corner latitude
# the same for longitude

#mp = Basemap( projection= 'merc',
#             llcrnrlon = -76.45172657568239, 
#             llcrnrlat = -56.08751754901597,
#             urcrnrlon = -65.43100574537897,
#             urcrnrlat = -14.858128494096263,
#             resolution = 'f')

mp = Basemap( projection= 'merc',
             llcrnrlon = -91.24611168924429, 
             llcrnrlat = -56.29899605299054,
             urcrnrlon = -34.545298646617624, 
             urcrnrlat = 1.821391227346372,
             resolution = 'f')


lon, lat = np.meshgrid(lons, lats)
x, y = mp(lon, lat)

months = np.arange(0, 491)

for i in months:
    
    c_scheme = mp.pcolor(x, y, np.squeeze(tmin[i, :, :]), cmap= 'jet')
    mp.drawcoastlines()
    mp.drawstates()
    mp.drawcountries()
    mp.drawlsmask()
    mp.etopo()
    mp.warpimage()
    
    cbar = mp.colorbar(c_scheme, location = 'right', pad= '10%')
    
    month = i+1
    
    plt.title('Temperatura minima del mes ' + str(month) + ' desde 1979 hasta 2019')
    plt.clim(-40, 40)
    plt.savefig(r'C:\Users\Nico\Desktop\UBB\2022-2\Tesis\images_gif'+'\\'+ str(month)+'.jpg')
    plt.clf()

    

