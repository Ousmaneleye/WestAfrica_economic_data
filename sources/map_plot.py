import folium
from utils import get_detail
from geojson_df import get_geojson_df
from westafrica import westafrica_df
import pandas as pd

######## MERGE geojson_df and westafrica_df

geojson_df = get_geojson_df()

final_df = pd.merge(geojson_df, westafrica_df, left_on="name", right_on="pays")
final_df.drop(['pays'], axis=1, inplace=True)

detail = get_detail(final_df)

map = folium.Map(location=[11.9, -1.29], 
                tiles='cartodbpositron', 
                min_zoom=5, max_zoom=5.3,
                width="%90", height="%100",
                zoom_start=5)

folium.Choropleth(final_df,                                # geo data
                data=final_df,                           # data
                key_on='feature.properties.name', # feature.properties.key
                columns=['name', 'population'],   # [key, value]
                fill_color='Reds',                     # cmap
                line_weight=0.8,                       # line wight (of the border)
                line_opacity=0.5,                    # line opacity (of the border)
                name="Population par pays (Afrique de l'Ouest)",
                show=True,
                legend_name='Population par pays').add_to(map)
folium.Choropleth(final_df,                                
                  data=final_df,                           
                  key_on='feature.properties.name', 
                  columns=['name', 'IDH'],   
                  fill_color='Blues',                     
                  line_weight=0.8,                       
                  line_opacity=0.5,                    
                  name="IDH par pays (Afrique de l'Ouest)",
                  show=False,
                  legend_name='IDH par pays').add_to(map)
folium.Choropleth(final_df,                                
                  data=final_df,                           
                  key_on='feature.properties.name', 
                  columns=['name', 'Dette (%PIB)'],   
                  fill_color='Greens',                     
                  line_weight=0.8,                       
                  line_opacity=0.5,                    
                  name="Dette (%PIB) par pays (Afrique de l'Ouest)",
                  show=False,
                  legend_name='Dette (%PIB) par pays').add_to(map)
folium.Choropleth(final_df,                                
                  data=final_df,                           
                  key_on='feature.properties.name', 
                  columns=['name', 'PIB/hbt (€)'],   
                  fill_color='YlOrRd',                     
                  line_weight=0.8,                       
                  line_opacity=0.5,                    
                  name="PIB/hbt (€) par pays (Afrique de l'Ouest)",
                  show=False,
                  legend_name='PIB/hbt (€) par pays').add_to(map)
folium.Choropleth(final_df,                                
                  data=final_df,                           
                  key_on='feature.properties.name', 
                  columns=['name', 'PIB/an (M. €)'],   
                  fill_color='Greys',                     
                  line_weight=0.8,                       
                  line_opacity=0.5,                    
                  name="PIB/an (M. €) par pays (Afrique de l'Ouest)",
                  show=False,
                  legend_name='PIB/an (M. €) par pays').add_to(map)
folium.Choropleth(final_df,                                
                  data=final_df,                           
                  key_on='feature.properties.name', 
                  columns=['name', 'Déficit (%PIB)'],   
                  fill_color='Purples',                     
                  line_weight=0.8,                       
                  line_opacity=0.5,                    
                  name="Déficit (%PIB) par pays (Afrique de l'Ouest)",
                  show=False,
                  legend_name='Déficit (%PIB) par pays').add_to(map)

folium.LayerControl(position='topright', collapsed=True).add_to(map)
map.add_child(detail)
map.keep_in_front(detail)
file_html = input("Give the name or path of the output as a file (.html) : ")
map.save(file_html)