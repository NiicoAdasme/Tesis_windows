# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 20:45:49 2023

@author: Nico
"""

from netCDF4 import Dataset
import numpy as np
import pandas as pd
import os

def export_csv(ruta, fecha, tipo= ['tmin', 'tmax', 'pr']):

    data = Dataset(ruta)

    lat = data.variables['lat'][:]
    lon = data.variables['lon'][:]
    time = data.variables['time'][:]

    if tipo == 'tmin':
        var = data.variables['tmin'][:]
    
    if tipo == 'tmax':
        var = data.variables['tmax'][:]

    if tipo == 'pr':
        var = data.variables['pr'][:]

    # Latitud y longitud de la region de Ñuble. Consideramos Chillan como par de coordenadas
    #lat_nuble = -36.605117255930786
    #lon_nuble = -72.11779361226445

    # Diferencia cuadrada de lat y lon
    #sq_diff_lat = (lat - lat_nuble)**2
    #sq_diff_lon = (lon - lon_nuble)**2

    #Identificar el indice del minimo valor para lat y lon
    #min_index_lat = sq_diff_lat.argmin()
    #min_index_lon = sq_diff_lon.argmin()
    

    # months since 1978-12-15
    starting_date = data.variables['time'].units[13:23]
    
    # input value of Date is the ending date of the date range + 1 to know the position of the date in the netcdf file
    ending_date = fecha

    # with the date range we can know the dates in format dates, because netcdf works with position about the starting date
    date_range = pd.date_range(start= starting_date, end= ending_date, freq= 'M')
    #date_range = date_range.date().strftime('%Y-%m-%d')
    pos_date = date_range.size + 1

    cont = 0

    #dt = np.arange(0, data.variables['time'].size)

    # We create a empty dataframe
    df = pd.DataFrame()

    # bucle for, for each coord
    dlat = np.arange(0, data.variables['lat'].size)
    dlon = np.arange(0, data.variables['lon'].size)


    for i in dlat:
        #if i == min_index_lat:
        #    break
        
        for j in dlon:
        #    if j == min_index_lon:
        #        break
        #    else:
            print('i: '+ str(i))
            print('j: '+ str(j))
            print('cont: '+ str(cont))
            varr = var[pos_date, i, j]
            cont = cont + 1
            df = df.append({'lat': lat[i],  'lon': lon[j], tipo: varr}, ignore_index=True)

    
    path_netcdf = os.path.basename(ruta)
    name_netcdf = path_netcdf.split(".nc")
    path_csv = 'csv/' + name_netcdf[0] + '-' + str(fecha) + '.csv'

    # export to csv and then import it, and then we clear the data.
    # when we import the csv, we can handle again like a dataframe, so we can clear the data. Before we can not do that
    df.to_csv(path_csv)

    df = pd.read_csv(path_csv, index_col=0)

    # we replace -- for NaN value
    df[tipo] = df[tipo].replace('--', np.NaN)        

    # Delete records without data
    df.dropna(inplace=True)

    res = df.to_csv(path_csv)
    # if res is 'None' (string) value, then the load to csv is succesfully, otherwise it's wrong
    return res 




