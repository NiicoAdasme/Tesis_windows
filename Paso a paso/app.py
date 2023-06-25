from fastapi import FastAPI
import netCDF4 as nc
import numpy as np
import pandas as pd

app = FastAPI()

posts = [
    {
        "title": "Hello World",
        "comment": "This is my first post"
    },
    {
        "title": "My second post",
        "comment": "This is my second post"
    }
]

@app.get('/')
def read_root():
    return {"welcome": "Welcome to my rest api"}

@app.get('/posts')
def get_posts():
    return posts

@app.get('/getData')
def get_data():
    dataset = nc.Dataset(r'C:\\Users\\Nico\\Desktop\\ArchivosNetCDF\\CR2\\1979-2019\\CR2MET_tmax_v2.0_mon_1979_2019_005deg.nc')
    variables = dataset.variables
    cont = 0
    # Crear un diccionario para almacenar los datos
    datos = {}

    # Recorrer las variables y extraer los datos
    for variable in variables:
        primera_variable = list(variables.keys())[cont]
        longitud_datos = len(dataset.variables[primera_variable][:])
        
        datos_variable = dataset.variables[variable][:]
        if len(datos_variable) != longitud_datos:
            print(f"La variable '{variable}' tiene una longitud diferente a la primera variable encontrada.")
            print(f"Longitud esperada: {longitud_datos}. Longitud actual: {len(datos_variable)}")
            continue
        datos[variable] = datos_variable
        cont+=1
        
    dataset.close()
    df = pd.DataFrame(datos)
    return df