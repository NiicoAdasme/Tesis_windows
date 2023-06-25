# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 04:11:05 2023

@author: Nico
"""
import netCDF4 as nc
import pandas as pd
import numpy as np

ruta = r'C:\Users\Nico\Desktop\UBB\2022-2\Tesis\indice_hidrico.nc'
data = nc.Dataset(ruta)

time = data.variables['time'][:]
lat = data.variables['lat'][:]
lon = data.variables['lon'][:]
indice_hidrico = data.variables['indice_hidrico'][:]

df = pd.DataFrame()

dlat = np.arange(0, data.variables['lat'].size)
dlon = np.arange(0, data.variables['lon'].size)

for i in dlat:    
    for j in dlon:
#        df = df.append({'lat': lat[i],  'lon': lon[j], 'tmin': tempmin, 'tmax': tempmax, 'pr': prec, 'ih': indice_hidrico}, ignore_index=True)
        df = df.append({'lat': lat[i],  'lon': lon[j], 'ih': indice_hidrico}, ignore_index=True)

print(df)

df.to_csv('test.csv')
