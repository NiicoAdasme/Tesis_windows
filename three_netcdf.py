# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 21:36:44 2023

@author: Nico
"""

from netCDF4 import Dataset

data = Dataset(r'C:\Users\Nico\Desktop\UBB\2022-2\Proyecto de título\ArchivosNetCDF\CR2\1979-2019\CR2MET_merged.nc')

# temperaturas minimas por mes 1979 - 2019
data_tmin = Dataset(r'C:\Users\Nico\Desktop\UBB\2022-2\Proyecto de título\ArchivosNetCDF\CR2\1979-2019\CR2MET_tmin_v2.0_mon_1979_2019_005deg.nc')

# temperaturas maxima por mes 1979 - 2019
data_tmax = Dataset(r'C:\Users\Nico\Desktop\UBB\2022-2\Proyecto de título\ArchivosNetCDF\CR2\1979-2019\CR2MET_tmax_v2.0_mon_1979_2019_005deg.nc')

# precipitaciones por mes 1979 - 2019
data_pr = Dataset(r'C:\Users\Nico\Desktop\UBB\2022-2\Proyecto de título\ArchivosNetCDF\CR2\1979-2019\CR2MET_pr_v2.0_mon_1979_2019_005deg.nc')

