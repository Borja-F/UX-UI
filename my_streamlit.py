import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
import folium
from streamlit_folium import folium_static


st.set_page_config(
    page_title="Happy McAwesome",
    page_icon="random",
    layout="wide",
    initial_sidebar_state="auto",
    
)

option = st.sidebar.selectbox(label= "Selecciona una página", options=["Home", "Charts", "Mapa+Gráficas"])
st.write(f"Has elegido {option}")


df = pd.read_csv("colegioslimpios.csv", sep=",")

uploaded_files = st.sidebar.file_uploader("Choose a CSV file",
                                    accept_multiple_files=False,
                                    type="csv")
if uploaded_files:
    df = pd.read_csv(uploaded_files, sep=";")
    st.balloons()

if option == "Home":

    

 

    with st.expander("Click for details:"):
        st.write("Esto es una aplicacion para mostrar los puntos de recarga en Madrid")




elif option == "Charts":


    

    mapa_valencia = folium.Map(location=[39.47825415129413, -0.36984913737192593],  zoom_start=16)

    fg = folium.FeatureGroup(name='Colegios')
    mapa_valencia.add_child(fg)

    zona_segura = folium.FeatureGroup(name='Zonas Seguras')

    paradas_metro = folium.FeatureGroup(name='Paradas Metro')
    mapa_valencia.add_child(paradas_metro)
    # Ruta al archivo GeoJSON
    archivo_geojson = 'fgv-bocas.geojson'

    # Crear una capa a partir del archivo GeoJSON
    capa_geojson = folium.GeoJson(archivo_geojson)

    # Añadir la capa al mapa
    capa_geojson.add_to(paradas_metro)


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
    zona_segura.add_child(marcador_1)
    zona_segura.add_child(marcador_2)
    zona_segura.add_child(marcador_3)
    zona_segura.add_child(marcador_4)
    zona_segura.add_child(marcador_5)
    zona_segura.add_child(marcador_6)
    zona_segura.add_child(marcador_7)
    zona_segura.add_child(marcador_8)
    zona_segura.add_child(marcador_9)

    # Añadir la capa de marcadores al mapa
    mapa_valencia.add_child(zona_segura)

    # Colocamos los colegios
    for (index, row) in mask.iterrows():
        folium.Marker(location = [row.loc['lat'], row.loc['long']],
                    popup = row.loc['Denominacion_Generica_ES'], icon=folium.Icon(color='purple'),
                    tooltip = row['Denominacion'], name = "Colegios").add_to(fg)

    def style_function(style_function): #Definimos la función para cambiar el color a verde
        return {
            'shadowColor': '#00ff00'
        }
    style2 = {'fillColor': '#008000', 'color': '#008000'}

    folium.GeoJson('zonas-verdes.geojson', name='Zonas verdes',style_function=lambda x:style2).add_to(mapa_valencia)


    folium.GeoJson('be-bien-bic.geojson', name='Bienes culturales').add_to(mapa_valencia)
    folium.LayerControl().add_to(mapa_valencia)
        
    # display map    
    mapa_valencia
    

    
   
    

    






elif option=="Mapa+Gráficas":



   

    df_mapa = df
    
    s_distrito = st.sidebar.checkbox('Distrito')

    s_operador = st.sidebar.checkbox('Operador')

    s_nº_cargadores = st.sidebar.checkbox("Nº Cargadores")

    if s_distrito:
            distrito = st.selectbox(label= "Selecciona distrito", options=df["Codigo_postal"].unique(), index = 0)
            
            mask1 = (df["Codigo_postal"] == distrito) 
            df_mapa = df.loc[mask1].copy()





         



     
    mapa = df_mapa[["lat","long"]]
    mapa = mapa.rename(columns={"lat":"lat","long":"lon"}) 

  


    st.map(mapa)

    
 
