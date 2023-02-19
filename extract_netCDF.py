# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 19:37:52 2022

@author: Nico
"""

from netCDF4 import Dataset
import numpy as np
import pandas as pd

data = Dataset(r'C:\Users\Nico\Desktop\UBB\2022-2\Proyecto de título\ArchivosNetCDF\CR2\1979-2019\CR2MET_tmax_v2.0_mon_1979_2019_005deg.nc')

lat = data.variables['lat'][:]
lon = data.variables['lon'][:]

lat_stgo = -33.444975556593064 
lon_stgo = -70.66282775086775

# Diferencia cuadrada de lat y lon
sq_diff_lat = (lat - lat_stgo)**2
sq_diff_lon = (lon - lon_stgo)**2

#Identificar el indice del minimo valor para lat y lon
min_index_lat = sq_diff_lat.argmin()
min_index_lon = sq_diff_lon.argmin()

tmax = data.variables['tmax']

# Creamos un panda dataframe
starting_date = data.variables['time'].units[13:23] # 1978-12-15
ending_date = data.variables['time'].units[11:11]+ '2019-12-15'
date_range = pd.date_range(start = starting_date, freq= 'MS',end = ending_date)
df = pd.DataFrame(0, columns= ['Temp Maximas'], index= date_range)

dt = np.arange(0, data.variables['time'].size)

for time_index in dt:
    df.iloc[time_index] = tmax  [time_index, min_index_lat, min_index_lon]


df.to_csv('temp_max_santiago.csv')
    




