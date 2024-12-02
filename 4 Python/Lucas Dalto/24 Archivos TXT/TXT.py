Archivo_sin_leer = open("24 Archivos TXT\\Texto_Jose.txt", encoding="UTF-8")


#Leer una sola linea
linea_1 = Archivo_sin_leer.readline()
print(linea_1)

linea_2 = Archivo_sin_leer.readline()
print(linea_2)

#Leer linea por linea
# lineas = Archivo_sin_leer.readlines()
# print(lineas)


#Si el archivo se lee por completo no se puede leer mas 
#Este codigo es el que hace que se lea todo.
# archivo = Archivo_sin_leer.read()
# print(archivo)

#Esto esto tambien sirve para leer todo el archivo.
#print(archivo.read())



#Cerrar el Archivo
Archivo_sin_leer.close()