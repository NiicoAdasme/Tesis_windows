# Calculate water of risk index

## Install anaconda

## Create a new environment
`conda create -n ih_env`

## Activate environment
`conda activate ih_env`

## Modules required
`conda install netCDF4`

`pip install tkcalendar`

## Add channel conda-forge and install modules
`conda config --env --add channels conda-forge`

`conda install python=3 basemap basemap-data-hires geopandas fiona shapely pyproj rtree`
## or
`conda install python=3 -c conda-forge basemap basemap-data-hires geopandas fiona shapely pyproj rtree`

## At least, inside tkinter folder, to run the app
`python index.py`