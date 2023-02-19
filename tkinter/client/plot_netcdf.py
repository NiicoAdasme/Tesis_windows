# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from netCDF4 import Dataset
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import os

def plot(ruta, fecha, tipo= ['tmin', 'tmax', 'pr']):

    data = Dataset(r''+ruta, 'r')

    lats = data.variables['lat'][:]
    lons = data.variables['lon'][:]
    time = data.variables['time'][:]

    if tipo == 'tmin':
        var = data.variables['tmin'][:]
    
    if tipo == 'tmax':
        var = data.variables['tmax'][:]

    if tipo == 'pr':
        var = data.variables['pr'][:]


    # urcrnrlat = upper corner latitude
    # llcrnrlat = lower corner latitude
    # the same for longitude

    mp = Basemap( projection= 'merc',
                llcrnrlon = -76.45172657568239, 
                llcrnrlat = -56.08751754901597,
                urcrnrlon = -65.43100574537897,
                urcrnrlat = -14.858128494096263,
                resolution = 'l')


    plt.rcParams["figure.figsize"] = (12, 12)

    lon, lat = np.meshgrid(lons, lats)
    x, y = mp(lon, lat)


    starting_date = data.variables['time'].units[13:23]
    # var fecha should be a date format eg. 1978-12-15
    ending_date = fecha 


    date_range = pd.date_range(start= starting_date, end= ending_date, freq= 'M')
    #date_range = date_range.date().strftime('%Y-%m-%d')
    pos_date = date_range.size + 1

    # !                                       TIME
    c_scheme = mp.pcolor(x, y, np.squeeze(var[pos_date, :, :]), cmap= 'jet')
    mp.drawstates()
    mp.drawcountries()

    #mp.drawcoastlines()
    mp.drawlsmask(land_color='#a7a7a7', ocean_color='#fafbfd', lakes=True)
    mp.drawrivers()
    mp.warpimage()

    cbar = mp.colorbar(c_scheme, location = 'right', pad= '10%')

    if tipo == 'tmin':
        plt.title('Temperatura minima de '+ str(fecha))
    
    if tipo == 'tmax':
        plt.title('Temperatura maxima de ' + str(fecha))

    if tipo == 'pr':
        plt.title('Precipitaciones de '+ str(fecha))

    path_img = os.path.basename(ruta)
    name_img = path_img.split(".nc")
    path_img = 'img/' + name_img[0] + '-' + str(fecha) + '.jpg'
    plt.savefig(path_img)

    return path_img
