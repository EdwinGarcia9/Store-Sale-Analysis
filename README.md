# PROYECTO STORE SALES ANALYSIS


# Authors

- [@EdwinGarcia9](https://github.com/EdwinGarcia9)
- [@LeopoldoGitHub](https://github.com/LeopoldoGitHub)



## **Problema de negocio**


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

# **Banco de Datos**
En este apartado se realizó la creación de la base de datos y la conexión , mediante la definición de funciones que guardan la base de datos en un repositorio definido por el usuario y agrega tablas provenientes de dataframes ya existentes.





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

Se realizó una consulta a la base de datos utilizando las funciones ya descritas y tomando en cuenta los productos, cantidad vendida de cada uno y el ingreso asociado cada  transacción





# Consulta SQL y creación de dataframes
```typescript
/consulta_sql = text("""
SELECT p.producto_id, p.producto, p.marca,
      SUM(i.cantidad) AS cantidad_vendida,
      SUM(i.cantidad * pr.precio) AS monto_total
FROM productos p
INNER JOIN items_pedidos i ON p.producto_id = i.producto_id
INNER JOIN productos pr ON p.producto_id = pr.producto_id
GROUP BY p.producto_id, p.producto, p.marca
ORDER BY cantidad_vendida DESC
LIMIT 5

""")


# Ejecutar la consulta SQL y cargar los resultados en un DataFrame
resultados = database.execute(consulta_sql)

# Guardar los resultados en un DataFrame
df = pd.DataFrame(resultados, columns=['producto_id', 'producto', 'marca', 'cantidad_vendida', 'monto_total'])
df["monto_total"] = (df["monto_total"]/1000).apply(lambda x: f'${x:.0f}K')
};
```




#**Pregunta 2: ¿Cual es la evolución histórica de las ingresos netos?**


#**Pregunta 3: ¿Cuáles son los ingresos netos por vendedor por año?**


# **4 ¿Cual es el Top 5 productos más vendidos históricamente?**







# Status badges

[![Netlify Status](https://api.netlify.com/api/v1/badges/8f784d8e-d28d-43a2-b892-39cddea52192/deploy-status)](https://app.netlify.com/sites/charming-eclair-87aaaww7301a/deploys)

![Status GitHub Action](https://github.com/nelsoncode019/screenshotsite/actions/workflows/codeql-analysis.yml/badge.svg)

[![Website shields.io](https://img.shields.io/website-up-down-green-red/http/shields.io.svg)](https://github.com)


## Installation

 ```bash
pip install fastapi
```


# Support
[!["Buy Me A Coffee"](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://www.buymeacoffee.com/NelsonCodeDev)
[!["Patreon"](https://img.shields.io/badge/Patreon-F96854?style=for-the-badge&logo=patreon&logoColor=white)](https://www.patreon.com/nelsoncode)
[!["PayPal"](https://img.shields.io/badge/PayPal-00457C?style=for-the-badge&logo=paypal&logoColor=white)](https://www.paypal.com/paypalme/nelsonher019)




# ⚡️ Features

✅  Search in Editor

✅  Download README.md file

✅  Upload README.md file

✅  Docker version

✅  Friendly UI

❌  Light Mode


# API Reference

> Version 1.0

## Path for tables
  
  | Method | Path                                                     | Description              | Information                            |
| ------ | -------------------------------------------------------- | ------------------------ | -------------------------------------- |
| GET    | [/api/get/table/all](get/table/all.ts)                   | Get all tables by region | [Reference](#get-all-tables-by-region) |
  
```bash
 GET /api/get/table/all
```

  | Header            | Type     | Description                                | Required |
  | :---------------- | :------- | :----------------------------------------- | :------- |
  | ```accesskeyid```       | ```string```   | The access key ID for your AWS account     | True     |
  | ```secretaccesskey```   | ```string```   | The secret access key for your AWS account | True     |
  | ```region```            | ```string```   | The region you want to use                 | True     |
  
### Responses

  - 200 OK
  
```json
{
    "TableNames": ["students", "teachers", "admins"]
}
```

# FAQ

<details>
<summary>What is GitHub and how does it work?</summary>

GitHub is the home for all developers—a platform where you can share code, contribute to open source projects, or even automate your workflow with tools like GitHub Actions and Packages. If you’re just getting started with GitHub, you may know us best as a place for version control and collaboration.
</details>

<details>
<summary>Who is GitHub for?</summary>

You! And it’s not just developers who build on GitHub—Fortune 500 companies, small teams, project managers, and college professors all use GitHub to do their best work, in one place.
</details>

<details>
<summary>Do people use GitHub only for code?</summary>

Nope. Like we mentioned above, different people and teams use GitHub for different projects. While we got our start as a version control platform, GitHub is now used to manage teams, share resumes, find new projects, track work, and host discussions, just to name a few.
</details>





# Table

| Song            | Artist                 | Year |
| :-------------- | :--------------------- | :----|
| Moscow Mule	    | Bad Bunny              | 2022 | 
| Stars           | Malcolm Lockyer	       | 1961 |
| Shining Star	  | Earth, Wind, and Fire  | 1975 |


