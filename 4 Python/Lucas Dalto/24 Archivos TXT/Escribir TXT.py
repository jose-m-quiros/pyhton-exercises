with open("24 Archivos TXT\\Texto_Jose.txt", "w", encoding="UTF-8") as Escritura:
                                         #La "w" es para sobreEscribir.
                                          #Y "a" lo que hace es agregar cada vez que se ejecuta el codigo
    
    #SobreEscribiendo el Archivo
    #Escritura.write("Jajajaj Te Cambie")
    
                                             #Aqui lo que estoy asiendo es convertir
                                             #los numeros a cadenas de texto
                                             #Pero tambien se pueden poner entre comillas
    Escritura.writelines(["Lista de super \n",  str(1333) + "\n", str(3222) + "\n", "Esto es pura Practica \n", "233 \n", "Money Wayy \n"])