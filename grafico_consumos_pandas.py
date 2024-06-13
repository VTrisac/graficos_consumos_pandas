import pandas as pd
import sqlite3 as sql
import matplotlib.pyplot as plt
import os

ruta = os.getcwd() + "\\Documents\\"
conex = sql.connect(ruta + "automocion_tablas.sqlite")

datos= pd.read_sql("SELECT * FROM consumos WHERE carroceria not in('convertible')",
       con=conex, index_col="carroceria")
print("\nDataFrame resultante de la lectura SQL:\n", datos)

datos.plot(kind="barh")
plt.xlabel("Consumos (l/km)")
plt.ylabel("Carrocerías")
plt.title("Media de consumos en ciudad")
plt.show()
