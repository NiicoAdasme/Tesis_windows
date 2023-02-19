# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 21:04:54 2022

@author: Nico
"""

from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import os
import PIL

def gen_timelapse(ruta, tipo= ['tmin', 'tmax', 'pr']):

    data = Dataset(ruta)

    lats = data.variables['lat'][:]
    lons = data.variables['lon'][:]
    time = data.variables['time'][:]
    
    if tipo == 'tmin':
        var = data.variables['tmin'][:]
        title = 'Temperatura minima del mes '
        name_gif = 'Temperatura minima de 1979 a 2019'
    
    if tipo == 'tmax':
        var = data.variables['tmax'][:]
        title = 'Temperatura maxima del mes '
        name_gif = 'Temperatura maxima de 1979 a 2019'

    if tipo == 'pr':
        var = data.variables['pr'][:]
        title = 'Precipitaciones del mes '
        name_gif = 'Precipitaciones de 1979 a 2019'

    # urcrnrlat = upper corner latitude
    # llcrnrlat = lower corner latitude
    # the same for longitude

    mp = Basemap( projection= 'merc',
                llcrnrlon = -91.24611168924429, 
                llcrnrlat = -56.29899605299054,
                urcrnrlon = -34.545298646617624, 
                urcrnrlat = 1.821391227346372,
                resolution = 'f')


    lon, lat = np.meshgrid(lons, lats)
    x, y = mp(lon, lat)

    months = np.arange(0, data.variables['time'].size)

    ruta = os.path.basename(ruta)
    ruta = ruta.split('.nc')

    # Create a folder to store the images
    if os.path.isdir('img/timelapse/'+ ruta[0]):
        pass
    else:
        os.mkdir(os.path.join('img', 'timelapse', ruta[0]))

    path_abs = os.path.join('img','timelapse', ruta[0])

    for i in months:
    #for i in range(0, 5):        
        c_scheme = mp.pcolor(x, y, np.squeeze(var[i, :, :]), cmap= 'jet')
        mp.drawcoastlines()
        mp.drawstates()
        mp.drawcountries()
        mp.drawlsmask()
        mp.etopo()
        mp.warpimage()
        
        cbar = mp.colorbar(c_scheme, location = 'right', pad= '10%')
        
        month = i+1
        
        plt.title(title + str(month) + ' desde 1979 hasta 2019')
        plt.clim(-40, 40)
        path_img = os.path.join('img','timelapse', ruta[0], str(month) + '.jpg')
        plt.savefig(path_img)
        plt.clf()

    image_frames = []

    for i in months:
    #for i in range(1, 5):
        path_abs = os.path.join('img', 'timelapse', ruta[0], str(i) + '.jpg')
        new_frame = PIL.Image.open(path_abs)
        image_frames.append(new_frame)
    
    path_gif = os.path.join('img', 'timelapse', name_gif + '.gif')
    image_frames[0].save(path_gif, format= 'GIF',
                        append_images= image_frames[1: ],
                        save_all= True, duration= 300,
                        loop= 0)

    return path_gif