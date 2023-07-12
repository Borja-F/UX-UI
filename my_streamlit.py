import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static

st.set_page_config(
    page_title="Mapa Valencia",
    page_icon="map",
    layout="wide",
    initial_sidebar_state="auto"
)

# Coordenadas de Valencia
latitud = 39.4699
longitud = -0.3763

# Crear un objeto de mapa centrado en Valencia
mapa_valencia = folium.Map(location=[latitud, longitud], zoom_start=12)

# Añadir un marcador en Valencia
folium.Marker(location=[latitud, longitud], popup='Valencia').add_to(mapa_valencia)

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
marcador_7 = folium.Marker(location=[39.475736, -0.427417], 
            popup='Mislata', 
            icon=folium.Icon(color='green', icon='7', prefix='fa'))
marcador_8 = folium.Marker(location=[39.481541, -0.460455], 
            popup='Quart de Poblet', 
            icon=folium.Icon(color='green', icon='8', prefix='fa'))
marcador_9 = folium.Marker(location=[39.424049, -0.496320], 
            popup='Torrent', 
            icon=folium.Icon(color='green', icon='9', prefix='fa'))

# Añadir los marcadores al mapa
mapa_valencia.add_child(marcador_1)
mapa_valencia.add_child(marcador_2)
mapa_valencia.add_child(marcador_3)
mapa_valencia.add_child(marcador_4)
mapa_valencia.add_child(marcador_5)
mapa_valencia.add_child(marcador_6)
mapa_valencia.add_child(marcador_7)
mapa_valencia.add_child(marcador_8)
mapa_valencia.add_child(marcador_9)

# Mostrar el mapa en Streamlit
st.folium_chart(mapa_valencia)


    
   
    

    








    
 
