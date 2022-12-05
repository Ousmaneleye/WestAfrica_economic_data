################ Get Dataframe from geojson ###############

import geopandas
import pandas as pd

countries = [
    'benin', 'burkina_faso', 'cap_vert', 'gambia', 'ghana',
    'guinea', 'guinea_bissau', 'ivory_coast', 'liberia',
    'mali', 'niger', 'nigeria', 
    'senegal', 'sierra_leone', 'togo'
]
def get_geojson_df():
    frames = []
    for country in countries:
        gdf = geopandas.read_file(f"../countries_geojson/{country}.geojson")
        frames.append(gdf)
    gdf = pd.concat(frames)
    gdf.index = range(len(frames))
    return gdf