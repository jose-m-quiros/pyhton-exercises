import pandas as pd

#Usando la funcion read.csv para leer el archivo CSV
df = pd.read_csv("25 Archivos CSV\\CSV.csv")
df2 = pd.read_csv("25 Archivos CSV\\CSV.csv")


#Obteniendo los datos de la columna nombre
nombres = df["Nombre"]

cadena = "0123456789"


#Ordenando el DataFrames por la edad
df_ordenando_ascendente = df.sort_values("Edad")
print(df_ordenando_ascendente)


print(".............................")


#Ordenando de forma desendente
df_ordenando_desendente = df.sort_values("Edad", ascending=False)
print(df_ordenando_desendente)


print(".............................")



#Concatenando los 2 DataFrames
df_concatenando = pd.concat([df, df2])
print(df_concatenando)


print(".............................")


#Accediendo a la primer fila con head()
first_row = df.head(1)
print(first_row) 


print(".............................")


#Accediendo a las ultimas filas con tail()
ultimas_filas = df.tail(1)
print(ultimas_filas)


print(".............................")


#Accediendo a la cantidad de filas y columnas con shape
row_and_columns = df.shape
print(row_and_columns)


print(".............................")


#Accediendo a las row and columns con shape
Row_And_Columns = row_totals, columns_totals = df.shape
print(row_totals)
print(columns_totals)
print(Row_And_Columns)


print(".............................")


#Obteniendo Data Estadistica del DataFrame:
df_info = df.describe()
print(df_info)


print(".............................")


#Accediendo a un elemento especifico del df con iloc
elemento_especifico_iloc = df.iloc[2, 2]
print(elemento_especifico_iloc)

print("")

#Accediendo a todas las filas de una columna 
Apellidos = df.iloc[1,:]
print(Apellidos)


print(".............................")


#Accediendo a un elemento especifico del df con loc
elemento_especifico_loc = df.loc[2, "Edad"]
print(elemento_especifico_loc)

print("")

#Accediendo a una fila con loc
fila = df.loc[2, :]
print(fila)


print(".............................")


#Accediendo a las filas con edad mayor a 30
mayor_30 = df.loc[df["Edad"]>30,:]
print(mayor_30)