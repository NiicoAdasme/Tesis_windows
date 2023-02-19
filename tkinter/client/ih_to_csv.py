# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 20:45:49 2023

@author: Nico
"""

from netCDF4 import Dataset
import numpy as np
import pandas as pd
import os
import client.calc_ih as ih

def ih_to_csv(ruta_tmin, ruta_tmax, ruta_pr, fecha):

    data_tmin = Dataset(ruta_tmin)
    data_tmax = Dataset(ruta_tmax)
    data_pr = Dataset(ruta_pr)

    lat = data_tmin.variables['lat'][:]
    lon = data_tmin.variables['lon'][:]
    time = data_tmin.variables['time'][:]
    tmin = data_tmin.variables['tmin'][:]
    tmax = data_tmax.variables['tmax'][:]
    pr = data_pr.variables['pr'][:]

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
    starting_date = data_tmin.variables['time'].units[13:23]
    
    # input value of Date is the ending date of the date range + 1 to know the position of the date in the netcdf file
    ending_date = fecha
    month_number = fecha.month

    # with the date range we can know the dates in format dates, because netcdf works with position about the starting date
    date_range = pd.date_range(start= starting_date, end= ending_date, freq= 'M')
    #date_range = date_range.date().strftime('%Y-%m-%d')
    pos_date = date_range.size + 1

    cont = 0

    #dt = np.arange(0, data.variables['time'].size)

    # We create a empty dataframe
    df = pd.DataFrame()

    # bucle for, for each coord
    dlat = np.arange(0, data_tmin.variables['lat'].size)
    dlon = np.arange(0, data_tmin.variables['lon'].size)


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
            cont = cont + 1
            tempmin = tmin[pos_date, i, j]
            tempmax = tmax[pos_date, i, j]
            prec = pr[pos_date, i, j]
            tprom = (tempmin + tempmax) / 2
            
            if month_number == 1:
                indice_hidrico = ih.enero(tprom, prec)
            
            if month_number == 2:
                indice_hidrico = ih.febrero(tprom, prec)
            
            if month_number == 3:
                indice_hidrico = ih.marzo(tprom, prec)
            
            if month_number == 4:
                indice_hidrico = ih.abril(tprom, prec)
                
            if month_number == 5:
                indice_hidrico = ih.mayo(tprom, prec)
            
            if month_number == 6:
                indice_hidrico = ih.junio(tprom, prec)
                
            if month_number == 7:
                indice_hidrico = ih.julio(tprom, prec)
            
            if month_number == 8:
                indice_hidrico = ih.agosto(tprom, prec)
                
            if month_number == 9:
                indice_hidrico = ih.septiembre(tprom, prec)
                
            if month_number == 10:
                indice_hidrico = ih.octubre(tprom, prec)
                
            if month_number == 11:
                indice_hidrico = ih.noviembre(tprom, prec)
            
            if month_number == 12:
                indice_hidrico = ih.diciembre(tprom, prec)    

            df = df.append({'lat': lat[i],  'lon': lon[j], 'tmin': tempmin, 'tmax': tempmax, 'pr': prec, 'tprom': tprom, 'ih': indice_hidrico}, ignore_index=True)
           

    
    #path_netcdf = os.path.basename(ruta)
    #name_netcdf = path_netcdf.split(".nc")
    path_csv = 'csv/indice_riesgo_hidrico_' + str(fecha) + '.csv'

    # export to csv and then import it, and then we clear the data.
    # when we import the csv, we can handle again like a dataframe, so we can clear the data. Before we can not do that
    df.to_csv(path_csv)

    df = pd.read_csv(path_csv, index_col=0)

    # we replace -- for NaN value
    df['tmin'] = df['tmin'].replace('--', np.NaN)
    df['tmax'] = df['tmax'].replace('--', np.NaN)
    df['pr'] = df['pr'].replace('--', np.NaN)

    # Delete records without data
    df.dropna(inplace=True)

    res = df.to_csv(path_csv)
    # if res is 'None' (string) value, then the load to csv is succesfully, otherwise it's wrong
    return res 




