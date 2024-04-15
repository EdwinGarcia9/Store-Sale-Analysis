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

Se realizó una consulta a la base de datos utilizando las funciones ya descritas y tomando en cuenta los productos, cantidad vendida de cada uno y el ingreso asociado a cada  transacción.
---





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

# Observaciones
**-El producto mas vendido fue el Saia Midi Cinto Limone de Jade Seba con 549 unidades.**

**-Los ingresos neto del producto mas vendido fue de 115 mil reales, sin embargo nu fue el producto que mas ingreso recaudó.**

**-Los productos mas vendidos fueron prendas para mujeres.**



#**Pregunta 2: ¿Cual es la evolución histórica de las ingresos netos?**
Para responder a este planteamiento, se realizó la consulta sql sobre la base de datos y se realizó la preparación de varios dataframe que ayudarán a responder a esta y otras interrogantes: Ingreso neto promedio diario total periodo, Ingreso neto promedio diario  por año, Ingreso neto promedio diario  desde 2020 y el  histórico de ingresos netos.
---

# Consulta SQL y creación de dataframes
```typescript
/# Definir la consulta SQL
consulta_sql = text("""
SELECT
    p.fecha_compra AS fecha,
    strftime('%Y', p.fecha_compra) AS año,
    strftime('%m', p.fecha_compra) AS mes,
    strftime('%d', p.fecha_compra) AS dia,
    (p.total - i.costo_envio) AS ingreso_neto,
    pr.marca AS marca,
    pr.producto AS producto
FROM
    pedidos p
INNER JOIN
    items_pedidos i ON p.pedido_id = i.pedido_id
INNER JOIN
    productos pr ON i.producto_id = pr.producto_id

""")

# Ejecutar la consulta SQL y cargar los resultados en un DataFrame
resultados = database.execute(consulta_sql)

# Guardar los resultados en un DataFrame
df_ingreso_neto= pd.DataFrame(resultados)
df_ingreso_neto
```

# Gráfico de evolución histórica de ingresos netos

![image](https://github.com/EdwinGarcia9/Store-Sale-Analysis/assets/122738840/c5f9e97c-82e2-402c-85b8-8d2845223bb2)

# **Insights**
**-El valor promedio de ingresos netos, del periodo 2019-2021 es de $1.494 reales.**
---

**-El valor promedio de ingresos netos, desde el 2020 es de $1.492 reales.**
---

**-El 24 de Noviembre de 2019 se reportó un ingreso de $290 mil reales generado por la venta de marcas famosas, con Givenchy y Barbara Bela como preferidas.**
---

**-El año 2021 presento un promedio de ventas netas diarias de $1450 con una baja del 2,9% de la media del periodo, afectado por sólo tener el primer trimestre de ventas en los datos.**
---




#**Pregunta 3: ¿Cuáles son los ingresos netos por vendedor por año?**


Se tomó la consulta sql con la tabla de vendedores y los ingresos netos asociados a las ventas realizadas por cada uno de ellos.
---

# Consulta SQL y creación de dataframes
```typescript
/# Definir la consulta SQL

consulta_sql = text("""
SELECT
    nombre_vendedor,
    SUM((strftime('%Y', fecha_compra) = '2019') * (total - costo_envio)) AS "Año 2019",
    SUM((strftime('%Y', fecha_compra) = '2020') * (total - costo_envio)) AS "Año 2020",
    SUM((strftime('%Y', fecha_compra) = '2021') * (total - costo_envio)) AS "Año 2021"
FROM
    pedidos p
INNER JOIN
    items_pedidos ip ON p.pedido_id = ip.pedido_id
INNER JOIN
    vendedores v ON p.vendedor_id = v.vendedor_id
GROUP BY
    nombre_vendedor;

""")

# Ejecutar la consulta SQL y cargar los resultados en un DataFrame
consulta_vendedor = database.execute(consulta_sql)

# Guardar los resultados en un DataFrame
df_ingreso_vendedor= pd.DataFrame(consulta_vendedor)
df_ingreso_vendedor
```

# Gráfico de ingresos netos de vendedor por año

![image](https://github.com/EdwinGarcia9/Store-Sale-Analysis/assets/122738840/9676e205-63f3-4afa-adc3-301daefc71fb)


# **Insights**
**-Los vendedores Daniel y Ana aumentaron sus ingresos netos de $2 a $5 millones.**
---

**-Los vendedores Nadia y Milena aumentaron hasta $4 millones.**
---

**-El vendedor Paulo muestra una tendencia a la baja que debe ser evaluada, sin embargo es el que mas ingresos en total del periodo 2019-2021 con $7,8 millones .**
---



# **4. ¿Cuáles son las ciudades que proporcionan mayores ingresos netos?


**Para resolver este planteamiento se realizó una consulta de la ciudad en la tabla pedidos y se utilizó la libreria geobr para obtener los çodigos de las ciudades de Brasil. Mira lo que sigue a continuación...**
---

# Consulta SQL y creación de dataframes
```typescript
/consulta_sql = text("""
  SELECT items_pedidos.ciudad,
  SUM(pedidos.total - items_pedidos.costo_envio) AS ingreso_neto
  FROM pedidos
  INNER JOIN items_pedidos ON pedidos.pedido_id = items_pedidos.pedido_id
  GROUP BY items_pedidos.ciudad;
""")


# Ejecutar la consulta SQL y cargar los resultados en un DataFrame
resultados = database.execute(consulta_sql)

# Guardar los resultados en un DataFrame
df = pd.DataFrame(resultados, columns=['ciudad', 'ingreso_neto'])
```

# Gráfico de ingresos netos por ciudades de Brasil

![image](https://github.com/EdwinGarcia9/Store-Sale-Analysis/assets/122738840/3259d822-878c-4f70-bb99-c3cd69e5f26e)



# **Insights**




# **Recomendaciones**






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





# Table

| Tecnologías           | ----              | --- |
| :-------------- | :--------------------- | :----|
| Python	    | -----            | ---- | 
| Google Colab           | ---	       | --- |
| Power BI	  |--------------------  | ---- |
| SQLite	  | ---------------------  | ---- |
| Github	  | ---------------------  | ---- |


