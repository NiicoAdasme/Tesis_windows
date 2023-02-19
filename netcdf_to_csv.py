# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 23:20:20 2022

@author: Nico
"""

import netCDF4
from netcdf2csv import convert_file
import pandas as pd
import xarray as xr

ds = xr.open_dataset(r'C:\Users\Nico\Desktop\UBB\2022-2\Proyecto de título\ArchivosNetCDF\CR2\1979-2019\CR2MET_tmax_v2.0_mon_1979_2019_005deg.nc', decode_times=False)
units, reference_date = ds.time.attrs['units'].split('since')
ds['time'] = pd.date_range(start=reference_date, periods=ds.sizes['time'], freq='MS')


convert_file(ds, r'C:\Users\Nico\Desktop\UBB\2022-2\Proyecto de título\ArchivosNetCDF\CR2', r'C:\Users\Nico\Desktop\UBB\2022-2\Proyecto de título\ArchivosNetCDF\CR2',clean_choice=1)