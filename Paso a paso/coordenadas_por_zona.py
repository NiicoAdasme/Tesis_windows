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
def obtener_coordenadas_zona(archivo, zona):
    # Abre el archivo
    ds = Dataset(archivo)
   
    # Obtiene la variable latitud
    latitudes = ds.variables['lat'][:]
   
    # Obtiene la variable longitud
    #longitudes = ds.variables['lon'][:]

    # Obtiene los limites de la zona
    lat_origen, lat_final = limites_zonas[zona]
    #print(lat_origen)
    #print(lat_final)
    
    # Encuentra los índices que caen dentro del rango de latitud
    indices_lat = np.where((latitudes >= lat_origen) & (latitudes <= lat_final))
    #print(indices_lat)
    
    # Usa esos índices para seleccionar las latitudes correspondientes
    #lat_seleccionadas = latitudes[indices_lat]
    #print(lat_seleccionadas)
    
    # Genera un array de los pares de coordenadas
    #lat, lon = np.meshgrid(lat_seleccionadas, longitudes)
    #coordenadas = np.dstack([lat.flatten(), lon.flatten()])[0]
    #print(coordenadas)
    #return coordenadas
    return indices_lat

# Asigna la zona que quieres utilizar
#zona = '12'

# Llama a la función con el archivo y la zona seleccionada
#archivo = r'C:\Users\Nico\Desktop\UBB\2022-2\Tesis\archivo_combinado.nc'
#coordenadas = obtener_coordenadas_zona(archivo, zona)
#print(coordenadas)

#for cords in coordenadas:
#    print(cords)


