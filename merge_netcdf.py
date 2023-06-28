# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 22:18:17 2023

@author: Nico
"""
import xarray as xr
import os

netcdf_tmin = r'C:\Users\Nico\Desktop\ArchivosNetCDF\CR2\1979-2019\CR2MET_tmin_v2.0_mon_1979_2019_005deg.nc' 
netcdf_tmax = r'C:\Users\Nico\Desktop\ArchivosNetCDF\CR2\1979-2019\CR2MET_tmax_v2.0_mon_1979_2019_005deg.nc'
netcdf_pr = r'C:\Users\Nico\Desktop\ArchivosNetCDF\CR2\1979-2019\CR2MET_pr_v2.0_mon_1979_2019_005deg.nc'

ds1 = xr.open_dataset(r''+netcdf_tmin, decode_times=False)
ds2 = xr.open_dataset(r''+netcdf_tmax, decode_times=False)
ds3 = xr.open_dataset(r''+netcdf_pr, decode_times=False)

combined_ds = xr.merge([ds1['tmin'], ds2['tmax'], ds3['pr']])

# ruta = './netcdf/archivo_combinado.nc'
ruta_actual = os.getcwd()
ruta_completa = os.path.join(ruta_actual, 'tkinter','netcdf', 'archivo_combinado.nc')

combined_ds.to_netcdf(ruta_completa)