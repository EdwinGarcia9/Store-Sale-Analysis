import streamlit as st
import pandas as pd
from PIL import Image
import streamlit.components.v1 as c
import datetime
import numpy as np
import matplotlib.pyplot as plt

st.title("Análisis de datos")


st.write("## Análisis de datos:")
st.write("A través de Power BI realizamos un dashboard, que se puede consultar de manera interactiva para la exploración de las ventas del negocio:")

with st.expander('Dashboard'):
    # img = Image.open("./s14-24-m-data-bi/Media/PowerBI_Inicio.jpg")
    # imagen = img.resize((800, 400))
    # st.image(imagen)    

    st.write("<iframe width='1000' height='600' src='https://app.powerbi.com/view?r=eyJrIjoiYmU2ZDBiMTQtMzQ2Yy00Yjg3LWJhN2MtMmE1OTdiYjcxMzMyIiwidCI6ImRmODY3OWNkLWE4MGUtNDVkOC05OWFjLWM4M2VkN2ZmOTVhMCJ9&pageName=ReportSection50328a10d287ea590e77' style='display:block;margin:auto;'></iframe>", unsafe_allow_html=True)