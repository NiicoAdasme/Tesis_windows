# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 01:25:54 2023

@author: Nico
"""

import netCDF4 as nc
import numpy as np
import pandas as pd
import xarray as xr
from datetime import datetime
from WaterRiskIndex1 import get_index_month_zone

ruta = r'C:\Users\Nico\Desktop\UBB\2022-2\Tesis\archivo_combinado.nc'
data = nc.Dataset(ruta)

lat = data.variables['lat'][:]
lon = data.variables['lon'][:]
time = data.variables['time'][:]
tmin = data.variables['tmin'][:]
tmax = data.variables['tmax'][:]
pr = data.variables['pr'][:]

temp_min_var = data.variables['tmin']
temp_min_vals = temp_min_var[:]
temp_max_var = data.variables['tmax']
temp_max_vals = temp_max_var[:]
precip_var = data.variables['pr']
precip_vals = precip_var[:]


limites_zonas = {
    'zona_12':(-26.025, -17.025),
    'zona_3': (-32.025, -26.075),
    'zona_4': (-36.475, -32.075),
    'zona_5': (-44.025, -36.525),
    'zona_6': (-51.025, -44.075),
    'zona_7': (-56.975, -51.075),
}

ending_date = '1979-01-01'
zona_interes = "zona_12"  # corregir según corresponda

starting_date = data.variables['time'].units[13:23]
print('Fecha de inicio: ', starting_date)

date_range = pd.date_range(start= starting_date, end= ending_date, freq= 'M')
pos_date = date_range.size

print('Posicion a buscar: ', pos_date)
print('Fecha: ', ending_date, '| Posicion de la fecha: ', pos_date)
print('Zona: ', zona_interes)

fecha = datetime.strptime(ending_date, '%Y-%m-%d')
mes = fecha.strftime('%m')

df = pd.DataFrame()
cont = 0

# Obtén los límites de latitud de la zona
lat_min, lat_max = limites_zonas[zona_interes]

# Encuentra los índices de las latitudes que se corresponden con los límites de la zona
dlat = np.where((lat >= lat_min) & (lat <= lat_max))

dlon = np.arange(0, data.variables['lon'].size)

for i in dlat[0]:    
    for j in dlon:
        cont += 1
        print('\nCont: ', cont)

        tempmin = tmin[pos_date, i, j]
        print('Temperatura minima: ', tempmin)

        tempmax = tmax[pos_date, i, j]
        print('Temperatura maxima: ', tempmax)

        tprom = (tempmin + tempmax) / 2
        print('Temperatura promedio: ', tprom)

        prec = pr[pos_date, i, j]
        print('Precipitacion: ', prec)

        indice_hidrico = get_index_month_zone(tprom, prec, mes, zona_interes)
        print('Indice hidrico: ', indice_hidrico)

        df = df.append({'lat': lat[i],  'lon': lon[j], 'tmin': tempmin, 'tmax': tempmax, 'pr': prec, 'ih': indice_hidrico}, ignore_index=True)

print(df)
df.to_csv('df.csv')

#ds = xr.Dataset.from_dataframe(df)
#ds.to_netcdf('indice_hidrico.nc')


# Crear un nuevo archivo netCDF y escribir la variable del índice hidrico
nc_out = nc.Dataset('indice_hidrico.nc', 'w', format='NETCDF4')

time_dim = nc_out.createDimension('time', None)
lat_dim = nc_out.createDimension('lat', lat.shape[0])
lon_dim = nc_out.createDimension('lon', lon.shape[0])

time_var = nc_out.createVariable('time', 'f4', ('time',))
lat_var = nc_out.createVariable('lat', 'f4', ('lat',))
lon_var = nc_out.createVariable('lon', 'f4', ('lon',))
ih_var = nc_out.createVariable('ih', 'f4', ('time', 'lat', 'lon',))

time_var[:] = data.variables['time'][:]
lat_var[:] = data.variables['lat'][:]
lon_var[:] = data.variables['lon'][:]
ih_var[:] = np.array(df['ih']).reshape(time.shape[0], lat.shape[0], lon.shape[0])


nc_out.close()










