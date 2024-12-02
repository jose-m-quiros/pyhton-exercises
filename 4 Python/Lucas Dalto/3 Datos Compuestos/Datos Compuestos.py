#La lista se puede modificar.
#La lista muestra los elementos repetidos
lista = ["Pollo", "Jose", "Caiman", True, 198.9, "Jose"] #Lista
print(lista)
lista[3] = "Porque te cambiaste a Liberty"
print(lista[3]) #Esto es valido
print(lista)


print("------------------------------------------------------------------------")
print("------------------------------------------------------------------------")

#La tupla | tuple NO se puede modificar. 
#La tupla muestra los elementos repetidos
tupla = ("Gerald Pique", "Ibai", "Jirafa", True, 18.9, "Ibai") #Array
print(tupla)
#tupla[0] = "Quedate con TeleCable"
print(tupla[0]) #No valido ya que tira el error
print(tupla)

print("------------------------------------------------------------------------")
print("------------------------------------------------------------------------")


#Creando un conjunto (set) | No accede a los elementos por indice, El conjunto NO muestra los elementos repetidos | Los acomoda Desordenados
conjunto = {"Tarzan", "Manuel", "Perro", False, 1.9, "Tarzan"}
#print(conjunto[0]) ERROR NO ACCEDE A LOS ELEMENTOS
print(conjunto)

#No se puede cambiar o modificar los elementos "Pollo...198.9"
#conjunto[1] = "Porque no se puede cambiar"
#print(conjunto)

#Pero si se puede reconstruir o redefinir 
conjunto = {"Si lo pude cambiar"}
print(conjunto)

print("------------------------------------------------------------------------")
print("------------------------------------------------------------------------")

#Creando un Diccionario (Dict)
diccionario = {
    #La estructura es key : value y separamos por comas
    'nombre' : 'Jose',
    'Empresa' : 'CyberStyle Web',
    'Emocionado' : True,
    'Año De Nacimiento' : 2006,
    'Duplicado?' : 'Jose'
}

print(diccionario['nombre'])
print(diccionario["Año De Nacimiento"])