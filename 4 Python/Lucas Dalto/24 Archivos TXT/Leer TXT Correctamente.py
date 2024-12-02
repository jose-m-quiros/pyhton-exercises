#Abriendo el Archivo
with open("24 Archivos TXT\\Texto_Jose.txt", encoding="UTF-8") as Archivo:
    
    #Leemos el Archivo
    Contenido = Archivo.read()
    
    print(Contenido)
    
#No es necesario cerrarlo al usar with open