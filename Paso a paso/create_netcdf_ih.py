# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 21:04:03 2023

@author: Nico
"""

import netCDF4 as nc
import numpy as np
import netCDF4 as nc
import pandas as pd
from datetime import datetime
from WaterRiskIndex1 import get_index_month_zone
from create_range import create_range
from constantes import (
LIMIT_ZONA_12_LAT_ORIGEN,
LIMIT_ZONA_12_LAT_FINAL,
LIMIT_ZONA_3_LAT_ORIGEN,
LIMIT_ZONA_3_LAT_FINAL,
LIMIT_ZONA_4_LAT_ORIGEN, 
LIMIT_ZONA_4_LAT_FINAL,
LIMIT_ZONA_5_LAT_ORIGEN,
LIMIT_ZONA_5_LAT_FINAL,
LIMIT_ZONA_6_LAT_ORIGEN,
LIMIT_ZONA_6_LAT_FINAL,
LIMIT_ZONA_7_LAT_ORIGEN,
LIMIT_ZONA_7_LAT_FINAL,
ZONE12,
ZONE3,
ZONE4,
ZONE5,
ZONE6,
ZONE7
)

zonas = [ZONE12, ZONE3, ZONE4, ZONE5, ZONE6, ZONE7]

# Se espera recibir una fecha(mes), coordenadas(lat,lon) y la zona.

# Abrir los archivos netCDF y leer las variables

# temperaturas minimas por mes 1979 - 2019
data = nc.Dataset(r'C:\Users\Nico\Desktop\UBB\2022-2\Tesis\archivo_combinado.nc')


ending_date = '1979-01-01'
lat_interes = -18.5305935155566
lon_interes = -70.35870464930689
zona_interes = "12"

temp_min_var = data.variables['tmin']
temp_min_vals = temp_min_var[:]
temp_max_var = data.variables['tmax']
temp_max_vals = temp_max_var[:]
precip_var = data.variables['pr']
precip_vals = precip_var[:]

starting_date = data.variables['time'].units[13:23]

date_range = pd.date_range(start= starting_date, end= ending_date, freq= 'M')

pos_date = date_range.size

tmin = data.variables['tmin'][pos_date, lat_interes, lon_interes]
print('Temperatura minima: ', tmin)

tmax = data.variables['tmax'][pos_date, lat_interes, lon_interes]
print('Temperatura maxima: ', tmax)

tprom = (tmin + tmax) / 2
print('Temperatura promedio: ', tprom)

pr = data.variables['pr'][pos_date, lat_interes, lon_interes]
print('Precipitacion: ', pr)


print('Fecha: ', ending_date, '| Posicion de la fecha: ', pos_date)
print('Zona: ', zona_interes)

fecha = datetime.strptime(ending_date, '%Y-%m-%d')
mes = fecha.strftime('%m')
print('Mes: ', mes)

indice_hidrico = get_index_month_zone(tprom, pr, mes, zona_interes)
print('Indice hidrico: ', indice_hidrico)

# We create a empty dataframe
df = pd.DataFrame()

# step by step for coords
step_size = 0.05

# bucle for, for each coord
#dlat = np.arange(0, data.variables['lat'].size)
origen = LIMIT_ZONA_12_LAT_ORIGEN
final = LIMIT_ZONA_12_LAT_FINAL
#dlat = create_range(origen, final, 0.05)

dlon = np.arange(0, data.variables['lon'].size)
#print(dlat)



if (zona_interes in zonas):
    print('Zona elegida es valida: ', zona_interes)
    #for LIMIT_ZONA_12_LAT_ORIGEN in LIMIT_ZONA_12_LAT_FINAL:
     #   print('Hello')
#        for j in dlon:
            

# Crear un nuevo archivo netCDF y escribir la variable del índice hidrológico
#nc_out = nc.Dataset('indice_hidrico.nc', 'w', format='NETCDF4')

#time_dim = nc_out.createDimension('time', None)
#lat_dim = nc_out.createDimension('lat', temp_min_vals.shape[1])
#lon_dim = nc_out.createDimension('lon', temp_min_vals.shape[2])

#time_var = nc_out.createVariable('time', 'f4', ('time',))
#lat_var = nc_out.createVariable('lat', 'f4', ('lat',))
#lon_var = nc_out.createVariable('lon', 'f4', ('lon',))
#ih_var = nc_out.createVariable('indice_hidrico', 'f4', ('time', 'lat', 'lon',))

#time_var[:] = data.variables['time'][:]
#lat_var[:] = data.variables['lat'][:]
#lon_var[:] = data.variables['lon'][:]
#ih_var[:] = h[:]

#nc_out.close()
