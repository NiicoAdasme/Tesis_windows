# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 20:45:49 2023

@author: Nico
"""

from netCDF4 import Dataset
import numpy as np
import pandas as pd
import os

def ih_export_csv(ruta):

    data = Dataset(ruta)

    lat = data.variables['lat'][:]
    lon = data.variables['lon'][:]
    ih = data.variables['ih'][:]

    cont = 0

    # We create a empty dataframe
    df = pd.DataFrame()

    # bucle for, for each coord
    dlat = np.arange(0, data.variables['lat'].size)
    dlon = np.arange(0, data.variables['lon'].size)

    ih_size = data.variables['ih'].size
    index_size = data.variables['ih'].size

    # TIENE UNA LONGITUD DE 19.580
    # OBTENIDAS MEDIANTE LA ITERACION ANTERIOR MEDIANTE LAS LAT Y LON.
    # CIERTOS VALORES ERAN NULOS POR LO QUE SE DESCARTARON
    # AHORA LA LONGITUD DIFIERE ENTRE LA QUE SE GENERA AL RECORRER NUEVAMENTE MEDIANTE LAT Y LON
    # Y LA LONGITUD DE LA VARIABLE IH


    for i in dlat:            
        for j in dlon:
            print('i: '+ str(i))
            print('j: '+ str(j))
            print('cont: '+ str(cont))
            varr = ih[cont]
            cont = cont + 1
            df = df.append({'lat': lat[i],  'lon': lon[j], 'ih': ih}, ignore_index=True)


    path_netcdf = os.path.basename(ruta)
    name_netcdf = path_netcdf.split(".nc")
    path_csv = 'csv/' + name_netcdf[0] + '.csv'

    # export to csv, import it, and then we clear the data.
    # when we import the csv, we can handle again like a dataframe, so we can clear the data. Before we can not do that
    df.to_csv(path_csv)

    df = pd.read_csv(path_csv, index_col=0)

    # we replace -- for NaN value
    df['ih'] = df['ih'].replace('--', np.NaN)        

    # Delete records without data
    df.dropna(inplace=True)

    res = df.to_csv(path_csv)
    # if res is 'None' (string) value, then the load to csv is succesfully, otherwise it's wrong
    return res 




