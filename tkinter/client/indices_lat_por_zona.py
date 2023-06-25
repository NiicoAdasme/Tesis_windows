# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 00:19:38 2023

@author: Nico
"""

from netCDF4 import Dataset
import numpy as np


# Limites de las zonas (DESTINO, ORIGEN)
limites_zonas = {
    '12': (-26.025, -17.025),
    '3': (-32.025, -26.075),
    '4': (-36.475, -32.075),
    '5': (-44.025, -36.525),
    '6': (-51.025, -44.075),
    '7': (-56.975, -51.075),
}

def indices_lat_zona(ruta_netcdf, zona):
    # Abre el archivo
    ds = Dataset(ruta_netcdf)
   
    # Obtiene la variable latitud
    latitudes = ds.variables['lat'][:]

    lat_origen, lat_final = limites_zonas[zona]

    # Encuentra los índices que caen dentro del rango de latitud
    indices_lat = np.where((latitudes >= lat_origen) & (latitudes <= lat_final))

    return indices_lat

