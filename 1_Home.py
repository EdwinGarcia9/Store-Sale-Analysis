import streamlit as st
import pandas as pd
from PIL import Image
import streamlit.components.v1 as c
import datetime
import numpy as np
import matplotlib.pyplot as plt
# import logging
# logger = logging.getLogger('cmdstanpy')
# logger.addHandler(logging.NullHandler())
# logger.propagate=False
# logger.setLevel(logging.CRITICAL)
# import warnings
# warnings.filterwarnings('ignore')

st.set_page_config(page_title="Store-Sales-Analysis-DATADOS",
                   page_icon="./img/logo.png",
                   layout="wide")


st.title("Proyecto Store Sales Analysis by DATADOS")
st.markdown("_Version 1.0_")
img = Image.open("./img/logo.png")
imagen = img.resize((240, 150))
st.image(imagen)


st.subheader('# PROBLEMA DE NEGOCIO')
texto = """

Una tienda online de moda, con presencia en todo Brasil, necesita impulsar su rendimiento utilizando sus datos de manera estratégica. Como científico de datos, has sido convocado para analizar estos datos y ofrecer insights que guíen sus decisiones y respondan a las siguientes preguntas clave
### **Preguntas**

1. ¿Cual es el Top 5 productos más vendidos históricamente?

2. ¿Cual es la evolución histórica de las ingresos netos?

3. ¿Cuáles son los ingresos netos por vendedor por año?

4. ¿Cuáles son las ciudades que proporcionan mayores ingresos netos?

5. ¿Existe otro insight que puedas proporcionar?

Para esto se han seguido las siguientes etapas de preparación."""
st.write(texto)
