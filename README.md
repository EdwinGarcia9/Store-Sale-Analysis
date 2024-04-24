# PROYECTO STORE SALES ANALYSIS



<h3 align="center">🛠️ Miembros del Equipo</h3>
****
<br>
<div align="center"> 
 
|Participantes|Roles|Redes|
|:---:|:---:|:---:|
|**Edwin Garcia**|![](https://img.shields.io/badge/DATA%20SCIENTIST-blue?style=for-the-badge) | <a target="_blank" rel="noopener noreferrer" href="https://www.linkedin.com/in/edd-garcia/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" /></a> <a target="_blank" rel="noopener noreferrer" href="https://github.com/EdwinGarcia9"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" /></a>   |
|**Leopoldo Flores**|![](https://img.shields.io/badge/DATA%20SCIENTIST-blue?style=for-the-badge)| <a target="_blank" rel="noopener noreferrer" href="https://www.linkedin.com/in/leopoldofloresc/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" /></a> <a target="_blank" rel="noopener noreferrer" href="https://github.com/LeopoldoGitHub"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" /></a>|

[![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/16rBPz1NW1Z4lRXnCLZbR0FyFT5gOZV3X?usp=sharing) 


<h2>🚧 Stack de Tecnologías </h2>

[![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat&logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![Colab](https://img.shields.io/badge/Colab-F9AB00?style=flat&logo=google-colab&logoColor=white)](https://colab.research.google.com/)
[![PowerBI](https://img.shields.io/badge/PowerBI-F2C811?style=flat&logo=power-bi&logoColor=white)](https://powerbi.microsoft.com/)
[![Trello](https://img.shields.io/badge/Trello-0052CC?style=flat&logo=trello&logoColor=white)](https://trello.com/)
[![Discord](https://img.shields.io/badge/Discord-5865F2?style=flat&logo=discord&logoColor=white)](https://discord.com/)

<a target="_blank" rel="noopener noreferrer" href="D:\Data\Proyectos\BootCamp_DS_ProfeAlejo\Store-Sale-Analysis\1_Home.py/"><img src="img/streamlitLogo.jpeg"width="30%"></a>


# PROBLEMA DE NEGOCIO


Una tienda online de moda, con presencia en todo Brasil, necesita impulsar su rendimiento utilizando sus datos de manera estratégica. Como científico de datos, has sido convocado para analizar estos datos y ofrecer insights que guíen sus decisiones y respondan a las siguientes preguntas clave
### **Preguntas**

1. ¿Cual es el Top 5 productos más vendidos históricamente?

2. ¿Cual es la evolución histórica de las ingresos netos?

3. ¿Cuáles son los ingresos netos por vendedor por año?

4. ¿Cuáles son las ciudades que proporcionan mayores ingresos netos?

5. ¿Existe otro insight que puedas proporcionar?

Para esto se han seguido las siguientes etapas de preparación.




## Configuración del ambiente
Se importan las librerias necesarias para el análisis
 ```bash
!pip install geobr
import geobr
import warnings
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import seaborn as sns
from matplotlib.ticker import MaxNLocator
from matplotlib.patches import FancyBboxPatch
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import matplotlib.dates as mdates
from matplotlib.ticker import FuncFormatter
import matplotlib.ticker as ticker
from PIL import Image
from io import BytesIO
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, Float, String, DateTime, inspect, text
global df_items_pedidos, df_pedidos, df_productos, df_vendedores, database
```
## **Obtención, Tratamiento y Análisis Exploratorio (EDA)**
En esta etapa se cargaron los dataframe para luego realizar la limpieza, transformación y tratamiento de los datos.

# ⚡️ Hallazgos

✅  2 productos con código de stock desconocido

✅  1 id_vendedor sin identificar

✅  Datos asociados a la venta de un vendedor sin nombre.

✅  Comuna fecha_de_compra sin formato DateTime

# **EDA visualizaciones**
Se realizaron distintas visualizaciones para explorar los datos de cada dataframe y ver el comportamiento de las variables.


![output](https://github.com/EdwinGarcia9/Store-Sale-Analysis/assets/130804905/3e5f335e-54c7-468d-9edf-de4175fc2eeb)


<p align="center">
  <img src="https://github.com/EdwinGarcia9/Store-Sale-Analysis/assets/130804905/f188008f-86d9-45ec-b547-cd95f3166cbe" alt="Descripción de la imagen">
</p>



# **Banco de Datos**
Nuestro objetivo como científicos de datos fue obtener una perspectiva concisa y clara del comportamiento de los datos y las relaciones que mantienen entre sí. Para lograr esto, recurrimos al diagrama Entidad-Relación (ER) entre las tablas. Esta acción tenía como objetivo mejorar la comprensión de los datos, así como identificar y optimizar posibles redundancias entre ellos.

<p align="center">
  <img src="https://github.com/EdwinGarcia9/Store-Sale-Analysis/assets/130804905/9a4c1833-17d4-4517-bb69-b3dec61b9ac0" alt="Descripción de la imagen">
</p>



Luego en este apartado se realizó la creación de la base de datos y la conexión, mediante la definición de funciones que guardan la base de datos en un repositorio definido por el usuario y agrega tablas provenientes de dataframes ya existentes.

# Función Crear base de datos
```typescript
def crear_base_datos(dataframes, db_name, db_path):
    global df_items_pedidos, df_pedidos, df_productos, df_vendedores

    """
    Crea una base de datos y agrega los DataFrames como tablas.

    Args:
    - dataframes: Un diccionario donde las claves son los nombres de las tablas y los valores son los DataFrames.
    - db_name: El nombre de la base de datos a crear.
    - db_path: La ruta para guardar la base de datos.

    Returns:
    - None
    """
    # Crear engine
    engine = create_engine('sqlite:///' + db_path + db_name, echo=False)

    # Guardar DataFrames en la base de datos como tablas
    for table_name, df in dataframes.items():
        df.to_sql(table_name, con=engine, if_exists='replace', index=False)

    # Cerrar la conexión
    engine.dispose()
```





# Función crear_conexion
```typescript
def crear_conexion(db_name, db_path):
    global df_items_pedidos, df_pedidos, df_productos, df_vendedores, engine
    # Crear la conexión a la base de datos
    engine = create_engine('sqlite:///' + db_path + db_name, echo=False)
    database = engine.connect()
    return database


# Llamar a la función para crear la conexión(Caso de uso)
db_name='database.db'
db_path='/content/drive/MyDrive/Colab Notebooks/Proyecto Store Sales Analysis/'

database = crear_conexion(db_name=db_name, db_path=db_path)

# Ahora puedes acceder a la variable "database"
# Usar el inspector para obtener información sobre las tablas y columnas
inspector = inspect(database)
print('Tablas: ', inspector.get_table_names(), '\n')
print('Columnas de Tabla Pedidos:')
for column in inspector.get_columns('pedidos'):
    print(column)
```

# Resumen

Hasta este punto hemos realizado la carga de la data, a la cual hemos realizado una limpieza y tratamiento, pasando por visualizaciones exploratorias que nos permitieron tener una data coherente y confiable.
Posteriormente utilizamos funciones que sirven para crear la base de datos "database.db" en un repositorio local y agregarle las tablas derivadas de los dataframes ya tratados; y con la función crear conexión
accedimos a la base datos para realizar las consultas que contestarán las preguntas relacionadas con el proyecto.

# Insights del negocio

# **1. ¿Cual es el Top 5 productos más vendidos históricamente?**

### Se realizó una consulta a la base de datos utilizando las funciones ya descritas y tomando en cuenta los productos, cantidad vendida de cada uno y el ingreso asociado a cada  transacción.

<p align="center">
  <img src="https://github.com/EdwinGarcia9/Store-Sale-Analysis/assets/130804905/0502ec63-0f57-41b6-8b77-d9488b4d8fff" alt="Descripción de la imagen">
</p>



## Insight 1
**El análisis histórico de ventas revela que el producto más demandado es el Saia Midi Cinto de la prestigiosa marca Limone By Jade Seba, con un total de 549 unidades vendidas. Sin embargo, cabe destacar que el producto que genera mayores ingresos es el vestido Nude Reta de la reconocida marca Ellus, el cual registra 547 unidades vendidas. Este último producto reporta un rendimiento financiero significativamente superior al Saia Midi Cinto, con ingresos que superan más del doble a los del mencionado producto.**



# **Pregunta 2: ¿Cual es la evolución histórica de las ingresos netos?**
### Para responder a este planteamiento, se realizó la consulta sql sobre la base de datos y se realizó la preparación de varios dataframe que ayudarán a responder a esta y otras interrogantes: Ingreso neto promedio diario total periodo, Ingreso neto promedio diario  por año, Ingreso neto promedio diario  desde 2020 y el  histórico de ingresos netos.

### Gráfico de evolución histórica de ingresos netos

![image](https://github.com/EdwinGarcia9/Store-Sale-Analysis/assets/122738840/c5f9e97c-82e2-402c-85b8-8d2845223bb2)

### Insight 2
**-El valor promedio de ingresos netos, del periodo 2019-2021 es de $1.494 reales.**

**-El valor promedio de ingresos netos, desde el 2020 es de $1.492 reales.**

**-El 24 de Noviembre de 2019 se reportó un ingreso de $290 mil reales generado por la venta de marcas famosas, con Givenchy y Barbara Bela como preferidas.**

**-El año 2021 presento un promedio de ventas netas diarias de $1450 con una baja del 2,9% de la media del periodo, afectado por sólo tener el primer trimestre de ventas en los datos.**




# **Pregunta 3: ¿Cuáles son los ingresos netos por vendedor por año?**


### Se tomó la consulta sql con la tabla de vendedores y los ingresos netos asociados a las ventas realizadas por cada uno de ellos.


### Gráfico de ingresos netos de vendedor por año

![image](https://github.com/EdwinGarcia9/Store-Sale-Analysis/assets/122738840/9676e205-63f3-4afa-adc3-301daefc71fb)


### Insights 3
**-Los vendedores Daniel y Ana aumentaron sus ingresos netos de $2 a $5 millones.**

**-Los vendedores Nadia y Milena aumentaron hasta $4 millones.**

**-El vendedor Paulo muestra una tendencia a la baja que debe ser evaluada, sin embargo es el que mas ingresos en total del periodo 2019-2021 con $7,8 millones .**



# **4. ¿Cuáles son las ciudades que proporcionan mayores ingresos netos?**
### Para resolver este planteamiento se realizó una consulta de la ciudad en la tabla pedidos y se utilizó la libreria geobr para obtener los çodigos de las ciudades de Brasil. Mira lo que sigue a continuación...

### Gráfico de ingresos netos por ciudades de Brasil

![image](https://github.com/EdwinGarcia9/Store-Sale-Analysis/assets/122738840/3259d822-878c-4f70-bb99-c3cd69e5f26e)


### Insights 4
**Las ciudades que destacaron por sus altos ingresos fueron Alagolas, Pernanbuco y Ceará, las cuales registraron un total combinado de más de 1.6 millones. Entre estas, Alagolas sobresale como la de mayor rendimiento financiero.**

**Por otro lado, las ciudades con ingresos más bajos fueron Acre, Mato Grosso do Sul y Amazonas, siendo Acre la que reportó las ventas más modestas.**


# **Recomendaciones**
##### **Es crucial realizar un análisis detallado de las estrategias de ventas implementadas en las ciudades con mayores ingresos. Esto permitirá determinar si dichas estrategias pueden replicarse en las ciudades con menores ventas, o si se requieren enfoques más agresivos para impulsar el rendimiento en estas áreas.**

##### **Dirigir las estrategias de venta hacia la promoción del Vestido Nude Reta para realizar mejoras sustanciales en los ingresos generados.**

##### **Aplicar estrategias de marketing para fidelizar a los clientes que adquieran las 5 marcas mas vendidas: Mixed, Cristian Dior y Bottega Veneta**

##### **Se recomienda impulsar planes de capacitación para ventas efectivas y mantener la motivación con estímulos por venta**

##### **La campaña de los productos nuevo sin etiqueta es susceptible a ser eliminada ya que no esta generando los resultados esperados**





# FAQ

<details>
<summary>Se utilizó algun gestor de datos?</summary>

Se utilizó SQLite para ejecutar la base de datos y realizar las consultas, sin embargo se puede utilizar MySQL, Posgree o cualquier otro que soporte SQL.
</details>

<details>
<summary>Que programa se usó para las visualizaciones?</summary>

Se reealizaron visualizaciones en pandas, sin embargo aprovechando el proyecto para conectar bases de datos, se aplicó Power BI para complementar graficos y probar la interconexión entre los programas para un mismo proyecto.
</details>

<details>
<summary>Se usaron consultas sql y manipulación de datos con Pandas</summary>

Si. Se realizaron las consultas necesarias para construir un dataframe o dataframes que fueran suficiente para manipular con pandas y terminar todas las operaciones necesarias en el notebook de google colab.
</details>






