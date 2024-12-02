frase = input("Dame una Frase y te calculo cuanto tardarias en decirla: ")

palabras_separadas = frase.split(" ") #Le estoy pidiendo que me separe las palabras

cantidad_de_palabras = len(palabras_separadas) #Cantidad de elementos

print(f'Dijistes {cantidad_de_palabras} palabras y tardarias {cantidad_de_palabras/2} segundos en decirlo')

print(f'Dalto lo diria en {cantidad_de_palabras * 100 // 2 * 1.3 / 100} segundos')

if cantidad_de_palabras > 20:
    print("Eso es mucho texto")