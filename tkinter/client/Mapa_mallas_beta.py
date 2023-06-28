# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 21:41:39 2023

@author: nicolas.vasquez
"""

import datetime
import numpy as np
import matplotlib.pyplot as plt
import netCDF4 as nc
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import geopandas as gpd
from geopandas.tools import sjoin
from shapely.geometry import Point
import pandas as pd
from matplotlib.colors import LinearSegmentedColormap

def mapa_ih(ruta_netcdf):
    # archivo = 'C:/Users/Nico/Desktop/UBB/2022-2/Tesis_windows/Paso a paso/output3-nico.nc'
    archivo = ruta_netcdf
    ruta_actual = os.getcwd()
    ruta_completa = os.path.join(ruta_actual, 'Regiones', 'Regional.shp')
    # shapefile = 'C:/Users/Nico/Desktop/UBB/2022-2/Tesis_windows/Paso a paso/Regiones/Regional.shp'
    shapefile = ruta_completa

    # Abrir el archivo netCDF en modo lectura
    data = nc.Dataset(archivo, 'r')

    # Obtener las variables necesarias
    latitudes = data.variables['lat'][:]
    longitudes = data.variables['lon'][:]
    ih = data.variables['ih'][:]

    # Cerrar el archivo netCDF
    data.close()

    # Filtrar valores no válidos o NaN en latitudes y longitudes
    valid_indices = np.isfinite(latitudes) & np.isfinite(longitudes)
    latitudes = latitudes[valid_indices]
    longitudes = longitudes[valid_indices]
    ih = ih[valid_indices]

    # Crear un DataFrame con los datos
    df = pd.DataFrame({
        'lon': longitudes.flatten(),
        'lat': latitudes.flatten(),
        'ih': ih.flatten()
    })

    # Convertir el DataFrame en un GeoDataFrame
    gdf = gpd.GeoDataFrame(df, geometry=[Point(xy) for xy in zip(df['lon'], df['lat'])])

    # Definir la proyección del GeoDataFrame
    gdf.crs = 'EPSG:4326'  # Utilizar la proyección WGS84 (EPSG:4326) como ejemplo, ajusta según la proyección correcta

    # Cargar el shapefile de Chile
    chile = gpd.read_file(shapefile)

    # Convertir la proyección del GeoDataFrame al sistema de coordenadas del shapefile
    gdf = gdf.to_crs(chile.crs)

    # Hacer un 'join' espacial para recortar los datos a la forma de Chile
    clipped = gpd.sjoin(gdf, chile, how='inner', op='within')

    # Eliminar la columna de índice innecesaria generada por sjoin
    clipped = clipped.drop('index_right', axis=1)

    # Crear una figura y un eje de proyección
    fig = plt.figure(figsize=(12, 13), dpi=900)
    ax = plt.axes(projection=ccrs.PlateCarree())

    # Verificar si hay datos válidos después del recorte
    if not clipped.empty:
        # Calcular los límites del eje basados en los datos recortados
        lat_min = np.percentile(clipped['lat'], 5)  # Establecer el límite inferior al percentil 5
        lat_max = np.percentile(clipped['lat'], 95)  # Establecer el límite superior al percentil 95
        lon_min = np.percentile(clipped['lon'], 5)
        lon_max = np.percentile(clipped['lon'], 95)

        # Acotar el mapa en base a las latitudes y longitudes
        ax.set_extent([lon_min-3, lon_max+3, lat_min-2, lat_max+2], crs=ccrs.PlateCarree())

        # Agregar características de mapa
        ax.add_feature(cfeature.LAND, facecolor='#ddc0a1')
        ax.add_feature(cfeature.OCEAN, facecolor='lightblue')
        ax.add_feature(cfeature.COASTLINE, linewidth=0.5)
        ax.add_feature(cfeature.BORDERS, linewidth=0.5)
        ax.add_feature(cfeature.STATES, linewidth=0.5)

        # Ordenar el dataframe por latitud y longitud
        clipped_sorted = clipped.sort_values(['lat', 'lon'])
        
        # Crear un nuevo dataframe con índices múltiples basados en latitud y longitud
        clipped_multi = clipped_sorted.set_index(['lat', 'lon'])
        
        # Crear una matriz 2D con los valores de ih
        unique_latitudes = np.unique(clipped_multi.index.get_level_values(0))
        unique_longitudes = np.unique(clipped_multi.index.get_level_values(1))
        unique_ih = np.empty((len(unique_latitudes), len(unique_longitudes)))
        
        # Llenar la matriz con los valores de ih
        for i, lat in enumerate(unique_latitudes):
            for j, lon in enumerate(unique_longitudes):
                if (lat, lon) in clipped_multi.index:
                    # Tomar el valor medio si hay múltiples valores para la misma latitud y longitud
                    unique_ih[i, j] = clipped_multi.loc[(lat, lon), 'ih'].mean()
                else:
                    unique_ih[i, j] = np.nan  # Puedes cambiar esto a cualquier valor que quieras usar para los "huecos"
        

        # Crear malla de contorno de ih
        xi, yi = np.meshgrid(unique_longitudes, unique_latitudes)
        
            # Niveles para la normalización de los colores
        # Niveles para la normalización de los colores
        niveles = np.arange(1, 4.0, 0.5)
        
        
        cmap = LinearSegmentedColormap.from_list(
            "blue_to_red", 
            [(0, "blue"), (1, "red")]
        )

        # Graficar la malla de contorno con la normalización
        cf = ax.contourf(xi, yi, unique_ih, levels=niveles, cmap=cmap, extend='both', transform=ccrs.PlateCarree())

        # Agregar nombres de las regiones
        region_names = [
            "Arica y Parinacota",
            "Tarapacá",
            "Antofagasta",
            "Atacama",
            "Coquimbo",
            "Valparaíso",
            "Metropolitana",
            "O'Higgins",
            "Maule",
            "Ñuble",
            "Biobío",
            "Araucanía",
            "Los Ríos",
            "Los Lagos",
            "Aysén",
            "Magallanes"
        ]

        region_centers = [
            (-70.3067, -18.4746),    # Arica y Parinacota
            (-69.8173, -20.2098),    # Tarapacá
            (-70.9382, -23.6509),    # Antofagasta
            (-69.8463, -27.3668),    # Atacama
            (-70.4017, -30.3951),    # Coquimbo
            (-71.3779, -33.0472),    # Valparaíso
            (-70.691, -33.460),      # Metropolitana
            (-70.9667, -34.2481),    # O'Higgins
            (-71.4417, -35.6556),    # Maule
            (-71.4428, -36.8278),    # Ñuble
            (-73.0489, -37.4463),    # Biobío
            (-72.6667, -38.9483),    # Araucanía
            (-72.8833, -40.3122),    # Los Ríos
            (-73.1367, -42.9128),    # Los Lagos
            (-72.9467, -45.3906),    # Aysén
            (-70.8017, -53.1622)     # Magallanes
        ]

        for name, center in zip(region_names, region_centers):
            x, y = center
            if lon_min <= x <= lon_max and lat_min <= y <= lat_max:
                ax.text(x, y, name, fontsize=10, ha='center', va='center', color='#ffffff', transform=ccrs.PlateCarree())
            
        # Agregar barra de color
        cbar = fig.colorbar(cf, ax=ax, orientation='vertical', ticks=niveles)

        cbar.set_label('Índice Hidrico')

        # Dibujar líneas de longitud y latitud
        ax.gridlines(draw_labels=True, linewidth=0.5, color='gray', alpha=0.5, linestyle='--')

        # Configurar título y etiquetas
        plt.title('Mapa de calor Índice Hidrico', fontsize=14)
        plt.xlabel('Longitud', fontsize=12)
        plt.ylabel('Latitud', fontsize=12)

        path_img = os.path.basename(archivo)
        name_img = path_img.split(".nc")
        path_img = 'img/' + name_img[0] + '.jpg'

        # Guardar el gráfico en un archivo antes de mostrarlo
        plt.savefig(path_img, format='jpg', dpi=900)

        return path_img
        # Mostrar el mapa
        plt.show()
    else:
        print("No hay datos válidos después del recorte.")
        return False
