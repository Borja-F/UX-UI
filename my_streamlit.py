import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
import folium
import streamlit_folium

from streamlit_folium import folium_static


st.set_page_config(
    page_title="Mapa Valencia",
    page_icon="map",
    layout="wide",
    initial_sidebar_state="auto",
    
)

option = st.sidebar.selectbox(label= "Selecciona una página", options=["Colegios", "Paradas Metro", "Zonas más Seguras","Zonas de interés cultural","Zonas Verdes"])
st.write(f"Has elegido {option}")


df = pd.read_csv("colegioslimpios.csv", sep=",")

if option == "Zonas más Seguras":
    # Coordenadas de Valencia
    latitud = 39.4699
    longitud = -0.3763

 
    zona_segura = folium.FeatureGroup(name='Zonas Seguras')

    # Crear un objeto de mapa centrado en Valencia
    mapa_valencia = folium.Map(location=[latitud, longitud], zoom_start=12)
    st.markdown(mapa_valencia._repr_html_(), unsafe_allow_html=True)

    # Crear una capa para los marcadores
    capa_marcadores = folium.FeatureGroup(name='Marcadores')

    # Añadir un marcador en Valencia a la capa de marcadores
    folium.Marker(location=[latitud, longitud], popup='Valencia').add_to(capa_marcadores)

    # Colocar Marcadores
    marcador_1 = folium.Marker(location=[39.470000, -0.370000], 
                            popup='Valencia-El Pla de Remei', 
                            icon=folium.Icon(color='green', icon='1', prefix='fa'))
    marcador_2 = folium.Marker(location=[39.383160, -0.466100], 
                            popup='Alcasser', 
                            icon=folium.Icon(color='green', icon='2', prefix='fa'))
    marcador_3 = folium.Marker(location=[39.3968877, -0.4080976], 
                            popup='Alfafar', 
                            icon=folium.Icon(color='green', icon='3', prefix='fa'))
    marcador_4 = folium.Marker(location=[39.509155, -0.422944], 
                popup='Burjassot', 
                icon=folium.Icon(color='green', icon='4', prefix='fa'))
    marcador_5 = folium.Marker(location=[39.544678, -0.331139], 
                popup='Albuixech', 
                icon=folium.Icon(color='green', icon='5', prefix='fa'))
    marcador_6 = folium.Marker(location=[39.470000, -0.395306], 
                popup='Valencia-La Roqueta', 
                icon=folium.Icon(color='green', icon='6', prefix='fa'))
    marcador_7 = folium.Marker(location=[39.475736	, -0.427417], 
                popup='Mislata ', 
                icon=folium.Icon(color='green', icon='7', prefix='fa'))
    marcador_8 = folium.Marker(location=[39.481541, -0.460455], 
                popup='Quart de Poblet', 
                icon=folium.Icon(color='green', icon='8', prefix='fa'))
    marcador_9 = folium.Marker(location=[39.424049, -0.496320], 
                popup='Torrent', 
                icon=folium.Icon(color='green', icon='9', prefix='fa'))



    # Añadir los marcadores a la capa de marcadores
    capa_marcadores.add_child(marcador_1)
    capa_marcadores.add_child(marcador_2)
    capa_marcadores.add_child(marcador_3)
    capa_marcadores.add_child(marcador_4)
    capa_marcadores.add_child(marcador_5)
    capa_marcadores.add_child(marcador_6)
    capa_marcadores.add_child(marcador_7)
    capa_marcadores.add_child(marcador_8)
    capa_marcadores.add_child(marcador_9)

    # Añadir la capa de marcadores al mapa
    mapa_valencia.add_child(capa_marcadores)

    # Añadir control de capas al mapa
    folium.LayerControl().add_to(mapa_valencia)
    st.markdown(mapa_valencia._repr_html_(), unsafe_allow_html=True)

    # Mostrar el mapa
    folium_static(mapa_valencia)

elif option == "Colegios":

    colegioslimpios = pd.read_csv("colegioslimpios.csv", index_col=0)

    mask = colegioslimpios[colegioslimpios["Localidad"] == "VALÈNCIA"]

    mapa_valencia = folium.Map(location=[39.47825415129413, -0.36984913737192593],  zoom_start=16)
    fg = folium.FeatureGroup(name='Colegios')
    mapa_valencia.add_child(fg)
    st.markdown(mapa_valencia._repr_html_(), unsafe_allow_html=True)

    # Colocamos los colegios
    for (index, row) in mask.iterrows():
        folium.Marker(location = [row.loc['lat'], row.loc['long']],
                    popup = row.loc['Denominacion_Generica_ES'], icon=folium.Icon(color='purple'),
                    tooltip = row['Denominacion'], name = "Colegios").add_to(fg)


elif option == "Paradas Metro":
    mapa_valencia = folium.Map(location=[39.47825415129413, -0.36984913737192593],  zoom_start=16)
    paradas_metro = folium.FeatureGroup(name='Paradas Metro')
    mapa_valencia.add_child(paradas_metro)
    # Ruta al archivo GeoJSON
    archivo_geojson = 'fgv-bocas.geojson'

    # Crear una capa a partir del archivo GeoJSON
    capa_geojson = folium.GeoJson(archivo_geojson)

    # Añadir la capa al mapa
    capa_geojson.add_to(paradas_metro)




elif option == "Zonas de interés cultural":
    mapa_valencia = folium.Map(location=[39.47825415129413, -0.36984913737192593],  zoom_start=16)
    st.markdown(mapa_valencia._repr_html_(), unsafe_allow_html=True)

    folium.GeoJson('be-bien-bic.geojson', name='Bienes culturales').add_to(mapa_valencia)
    folium.LayerControl().add_to(mapa_valencia)


elif option == "Zonas Verdes":
    mapa_valencia = folium.Map(location=[39.47825415129413, -0.36984913737192593],  zoom_start=16)
    st.markdown(mapa_valencia._repr_html_(), unsafe_allow_html=True)

    def style_function(style_function): #Definimos la función para cambiar el color a verde
        return {
            'shadowColor': '#00ff00'
        }
    style2 = {'fillColor': '#008000', 'color': '#008000'}

    folium.GeoJson('zonas-verdes.geojson', name='Zonas verdes',style_function=lambda x:style2).add_to(mapa_valencia)
    folium.LayerControl().add_to(mapa_valencia)

# Coordenadas de Valencia
latitud = 39.4699
longitud = -0.3763

# Crear un objeto de mapa centrado en Valencia
mapa_valencia = folium.Map(location=[latitud, longitud], zoom_start=12)
st.markdown(mapa_valencia._repr_html_(), unsafe_allow_html=True)

# Crear una capa para los marcadores
capa_marcadores = folium.FeatureGroup(name='Marcadores')

# Añadir un marcador en Valencia a la capa de marcadores
folium.Marker(location=[latitud, longitud], popup='Valencia').add_to(capa_marcadores)

# Colocar Marcadores
marcador_1 = folium.Marker(location=[39.470000, -0.370000], 
                        popup='Valencia-El Pla de Remei', 
                        icon=folium.Icon(color='green', icon='1', prefix='fa'))
marcador_2 = folium.Marker(location=[39.383160, -0.466100], 
                        popup='Alcasser', 
                        icon=folium.Icon(color='green', icon='2', prefix='fa'))
marcador_3 = folium.Marker(location=[39.3968877, -0.4080976], 
                        popup='Alfafar', 
                        icon=folium.Icon(color='green', icon='3', prefix='fa'))
marcador_4 = folium.Marker(location=[39.509155, -0.422944], 
            popup='Burjassot', 
            icon=folium.Icon(color='green', icon='4', prefix='fa'))
marcador_5 = folium.Marker(location=[39.544678, -0.331139], 
            popup='Albuixech', 
            icon=folium.Icon(color='green', icon='5', prefix='fa'))
marcador_6 = folium.Marker(location=[39.470000, -0.395306], 
            popup='Valencia-La Roqueta', 
            icon=folium.Icon(color='green', icon='6', prefix='fa'))
marcador_7 = folium.Marker(location=[39.475736	, -0.427417], 
            popup='Mislata ', 
            icon=folium.Icon(color='green', icon='7', prefix='fa'))
marcador_8 = folium.Marker(location=[39.481541, -0.460455], 
            popup='Quart de Poblet', 
            icon=folium.Icon(color='green', icon='8', prefix='fa'))
marcador_9 = folium.Marker(location=[39.424049, -0.496320], 
            popup='Torrent', 
            icon=folium.Icon(color='green', icon='9', prefix='fa'))



# Añadir los marcadores a la capa de marcadores
capa_marcadores.add_child(marcador_1)
capa_marcadores.add_child(marcador_2)
capa_marcadores.add_child(marcador_3)
capa_marcadores.add_child(marcador_4)
capa_marcadores.add_child(marcador_5)
capa_marcadores.add_child(marcador_6)
capa_marcadores.add_child(marcador_7)
capa_marcadores.add_child(marcador_8)
capa_marcadores.add_child(marcador_9)

# Añadir la capa de marcadores al mapa
mapa_valencia.add_child(capa_marcadores)

# Añadir control de capas al mapa
folium.LayerControl().add_to(mapa_valencia)
st.markdown(mapa_valencia._repr_html_(), unsafe_allow_html=True)

# Mostrar el mapa
folium_static(mapa_valencia)

    
   
    

    








    
 
