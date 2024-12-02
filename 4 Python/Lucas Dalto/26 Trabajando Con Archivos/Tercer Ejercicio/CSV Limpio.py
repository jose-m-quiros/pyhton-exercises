import pandas as pd

df = pd.read_csv("26 Trabajando Con Archivos\\Tercer Ejercicio\\CSV.csv")

#Creando un CSV con el DataFrame resultante (Vacio)
df.to_csv("26 Trabajando Con Archivos\\Tercer Ejercicio\\Datos_CSV_Clean.csv")