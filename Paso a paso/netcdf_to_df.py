# -*- coding: utf-8 -*-
"""
Created on Sun May 28 19:59:38 2023

@author: Nico
"""

from netCDF4 import Dataset
import numpy as np
import pandas as pd
from json import loads, dumps
import warnings


#warnings.filterwarnings("ignore")

data_tmin = Dataset(r'C:\Users\Nico\Desktop\ArchivosNetCDF\CR2\1979-2019\CR2MET_tmin_v2.0_mon_1979_2019_005deg.nc')

lat = data_tmin.variables['lat'][:]
lon = data_tmin.variables['lon'][:]
time = data_tmin.variables['time'][:]
tmin = data_tmin.variables['tmin'][:]


starting_date = data_tmin.variables['time'].units[13:23]

ending_date = '1979-01-01'
date_range = pd.date_range(start= starting_date, end= ending_date, freq= 'M')
pos_date = date_range.size + 1

cont = 0

# We create a empty dataframe
df = pd.DataFrame()

# bucle for, for each coord
dlat = np.arange(0, data_tmin.variables['lat'].size)
dlon = np.arange(0, data_tmin.variables['lon'].size)

limit_lat_inicio = -56.90
limit_lat_fin = -70.90

#for i in dlat:
#    # limit for zones
#    #if (i >= limit_lat_inicio and i <= limit_lat_fin):
#        # dentro de la zona
#    #else:
#        # fuera de la zona
#    for j in dlon:
#        print('Count: ', cont)
#        cont = cont + 1
#        tempmin = tmin[pos_date, i, j]
#        df = df.append({'lat': lat[i],  'lon': lon[j], 'tmin': tempmin }, ignore_index=True)
df = df.append({'lat': lat[0],  'lon': lon[0], 'tmin': tmin[0,0,0]}, ignore_index=True)

# we replace -- for NaN value
#df['tmin'] = df['tmin'].replace('--', np.NaN)

# Delete records without data
#df.dropna(inplace=True)

print(df)
df.to_csv('./test.csv')
#print(df.to_json())
result = df.to_json(orient="records")
parsed = loads(result)
dumps(parsed, indent=20)



