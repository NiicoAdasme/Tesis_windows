import netCDF4 as nc
import numpy as np
import pandas as pd
from datetime import datetime
from WaterRiskIndex import get_index_month_zone
import os


#ruta = r'C:\Users\Nico\Desktop\UBB\2022-2\Tesis_windows\Paso a paso\archivo_combinado.nc'
#ruta = r'C:\Users\Nico\Desktop\ArchivosNetCDF\CR2\1979-2019\CR2MET_merged.nc'
#ruta = r'C:\Users\Nico\Desktop\UBB\2022-2\Tesis_windows\tkinter\netcdf\archivo_combinado.nc'
ruta_actual = os.getcwd()
ruta = os.path.join(ruta_actual, 'netcdf', 'archivo_combinado.nc')
data = nc.Dataset(ruta)

lat = data.variables['lat'][:]
lon = data.variables['lon'][:]
time = data.variables['time'][:]
tmin = data.variables['tmin'][:]
tmax = data.variables['tmax'][:]
pr = data.variables['pr'][:]

limites_zonas = {
    '12':(-26.025, -17.025),
    '03': (-32.025, -26.075),
    '04': (-36.475, -32.075),
    '05': (-44.025, -36.525),
    '06': (-51.025, -44.075),
    '07': (-56.975, -51.075),
}

ending_date = '2017-01-01'
zona_interes = "03"  # corregir según corresponda

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


#ruta_netcdf = 'C:/Users/Nico/Desktop/UBB/2022-2/Tesis_windows/tkinter/netcdf/output4-nico.nc'  # Ruta del archivo netCDF de salida
ruta_actual = os.getcwd()
ruta_netcdf = os.path.join(ruta_actual, 'netcdf', 'output2.nc')

# Crear el archivo netCDF
nc_file = nc.Dataset(ruta_netcdf, 'w', format='NETCDF4')

# Definir las dimensiones
nc_file.createDimension('lat', len(df))
nc_file.createDimension('lon', len(df))
nc_file.createDimension('index', len(df))

# Crear las variables
var_lat = nc_file.createVariable('lat', 'f4', ('lat',))
var_lon = nc_file.createVariable('lon', 'f4', ('lon',))
var_index = nc_file.createVariable('index', 'i4', ('index',))
var_ih = nc_file.createVariable('ih', 'f4', ('index',))

# Asignar los datos a las variables
var_lat[:] = df['lat'].values
var_lon[:] = df['lon'].values
var_index[:] = df.index.values
var_ih[:] = df['ih'].values

# Cerrar el archivo netCDF
nc_file.close()