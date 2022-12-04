import folium
style_function = lambda x: {'fillColor': '#ffffff', 
                            'color':'#000000', 
                            'fillOpacity': 0.1, 
                            'weight': 0.1}
highlight_function = lambda x: {'fillColor': '#000000', 
                                'color':'#000000', 
                                'fillOpacity': 0.50, 
                                'weight': 0.1}
def get_detail(data):
    return folium.features.GeoJson(
        data = data,
        style_function=style_function, 
        control=False,
        highlight_function=highlight_function, 
        tooltip=folium.features.GeoJsonTooltip(
            fields=['name','population', 'IDH', 'Dette_totale (M. €)', 'PIB/an (M. €)', 'PIB/hbt (€)'],
            aliases=['Pays','Population', 'IDH', 'Dette_totale (M. €)', 'PIB/an (M. €)', 'PIB/hbt en euros'],
            style=("background-color: white; color: #333333; font-family: arial; font-size: 12px; padding: 10px;") 
        )
    )