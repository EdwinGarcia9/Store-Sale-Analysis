import streamlit as st
import pandas as pd
from PIL import Image
import streamlit.components.v1 as c
import datetime
import numpy as np
import matplotlib.pyplot as plt
import base64 
import logging
logger = logging.getLogger('cmdstanpy')
logger.addHandler(logging.NullHandler())
logger.propagate=False
logger.setLevel(logging.CRITICAL)
import warnings
warnings.filterwarnings('ignore')

st.title("ETL")



st.subheader('Extracción inicial de datos:')
texto = """Se obtienen los datos del acceso directo a la información del histórico de ventas de la empresa en formato csv:
        """
st.write(texto)

with st.expander('Df pedidos'):
    df = pd.read_csv("./Data/df_pedidos.csv")
    st.write(df)
with st.expander('Df items_pedidos'):
    df = pd.read_csv("./Data/df_items_pedidos.csv")
    st.write(df)
    
with st.expander('Df productos'):
    df = pd.read_csv("./Data/df_productos.csv")
    st.write(df)

with st.expander('Df vendedores'):
    df = pd.read_csv("./Data/df_vendedores.csv")
    st.write(df)

st.subheader('Transformación y limpieza de los datos:')

texto = """Se realizó la revisión y limpieza de los dataset segun se muestra en el link siguiente:
"""
st.write(texto)
st.markdown("[Store_Sales_Analysis_Completo.ipynb](https://colab.research.google.com/drive/16rBPz1NW1Z4lRXnCLZbR0FyFT5gOZV3X?usp=sharing)")

st.subheader('## Creación de tablas y relaciones:')
texto ="""
    Mediante cambios en la estructura de los datos, se definieron distintas tablas en las que dividimos los registros, para su escalabilidad.
    De esta manera la base de datos no solo es más eficiente y optimiza el rendimiento, sino que permite hacer análisis más detallados de algunos puntos importantes, como las ventas por productos."""
st.write(texto)


st.subheader('Estructura final de nuestra base de datos:')
texto ="""Relaciones entre las distintas tablas:"""
st.write(texto)    

# with st.expander('Relaciones'):
img = Image.open("./img/relation.png")
imagen = img.resize((800, 400))
st.image(imagen)    