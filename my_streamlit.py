import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np


st.set_page_config(
    page_title="Happy McAwesome",
    page_icon="random",
    layout="wide",
    initial_sidebar_state="auto",
    
)

option = st.sidebar.selectbox(label= "Selecciona una página", options=["Home", "Charts", "Mapa+Gráficas"])
st.write(f"Has elegido {option}")


df = pd.read_csv("colegioslimpios.csv", sep=",")
zonas_verdes = pd.read_csv("zonas-verdes.csv", sep= ";")

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



    with st.echo():
        #La gorronea es una terrible enfermedad que destruye tus relaciones sociales
        st.dataframe(df)


elif option=="Mapa":

    df_mapa = df
    
    s_distrito = st.sidebar.checkbox('Colegios')

    s_operador = st.sidebar.checkbox('Operador')

    s_nº_cargadores = st.sidebar.checkbox("Nº Cargadores")

    if s_distrito:
            distrito = st.selectbox(label= "Selecciona distrito", options=df["Codigo_postal"].unique(), index = 0)
            
            mask1 = (df["Codigo_postal"] == distrito) 
            df_mapa = df.loc[mask1].copy()





         



     
    mapa = df_mapa[["lat","long"]]
    mapa = mapa.rename(columns={"lat":"lat","long":"lon"}) 

  


    st.map(mapa)

    
 
