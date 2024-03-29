# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 18:56:01 2023

@author: Nico
"""

import xarray as xr
import os

def combinar_netcdf (netcdf_tmin, netcdf_tmax, netcdf_pr):

    ds1 = xr.open_dataset(r''+netcdf_tmin, decode_times=False)
    ds2 = xr.open_dataset(r''+netcdf_tmax, decode_times=False)
    ds3 = xr.open_dataset(r''+netcdf_pr, decode_times=False)

    combined_ds = xr.merge([ds1['tmin'], ds2['tmax'], ds3['pr']])

    # ruta = './netcdf/archivo_combinado.nc'
    ruta_actual = os.getcwd()
    ruta_completa = os.path.join(ruta_actual, 'netcdf', 'archivo_combinado.nc')

    return combined_ds.to_netcdf(ruta_completa), ruta_completa

