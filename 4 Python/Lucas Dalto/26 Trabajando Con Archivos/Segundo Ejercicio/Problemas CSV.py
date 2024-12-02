#Cambiar el tipo de dato de una Columna
import pandas as pd

df = pd.read_csv("26 Trabajando Con Archivos\\Segundo Ejercicio\\CSV.csv")


#Convirtiendo a String los datos de una columna
df["Edad"] = df["Edad"].astype(str)


#Mostrando el tipo de dato del primer elemento de la columna Edad
print(type(df["Edad"][0]))


print(":::::::::::::::::::::::::::")


#Remplazando los datos
df["Apellido"].replace("Quesadilla", "Franco", inplace=True)
# print(df["Apellido"])
print(df)

print(":::::::::::::::::::::::::::")

#Eliminando las filas con datos faltantes 
df = df.dropna()
print(df)

print(":::::::::::::::::::::::::::")

#Eliminando las filas repetidas
df = df.drop_duplicates()
print(df)