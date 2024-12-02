#LIST-Crea una lista | FUNCION
print("---------------------LIST-------------------------")
lista = list(["Jose","Manuel",16])
print(lista)

print("--------------------------------------------------")
print("--------------------------------------------------")





#LEN-Cuenta la cantidad de elementos de una lista
print("----------------------LEN-------------------------")
cadena = "Hola"
resu = len(cadena)
print(resu)

print("--------------------------------------------------")
print("--------------------------------------------------")



#APPEND,APPEND & EXTEND: A estos metodos se le pueden agregar: "Numeros: Enteros o Float", "Texto", "Boleans: True or False"
#APPEND-Agrega un elemento a la lista
print("----------------------APPEND----------------------")
lista.append("Racks On Me")
print(lista)
print("--------------------------------------------------")


#INSERT-agrega un elemento a la lista en el indice especificado 
print("----------------------INSERT----------------------")
lista.insert(0, "Baby Father 2.0")
print(lista)
print("--------------------------------------------------")

#EXTEND-Agrega varios elementos a la lista
print("----------------------EXTEND----------------------")
lista.extend([False, "Sufro", "Python", 10.5])
print(lista)
print("--------------------------------------------------")
print("--------------------------------------------------")





#POP-Elimina un elemento de una lista, pide indice y devuelve valor 
print("-----------------------POP------------------------")
lista.pop(1) #Aqui se esta eliminado "JOSE" | Y si quiero eliminar el ultimo elemento de una lista es -1, -2 para eliminar el anteultimo y asi sucesivamente
print(lista)
print("--------------------------------------------------")


#REMOVE-Remueve un elemento de una lista, por su valor
print("----------------------REMOVE----------------------")
lista.remove("Racks On Me")
print(lista)
print("--------------------------------------------------")

#CLEAR-Elimina todos los elementos de una lista
print("----------------------CLEAR-----------------------")
#lista.clear()
#print(lista)
print("--------------------------------------------------")
print("--------------------------------------------------")





#SORT-Ordena una lista de menor a mayor | Sirve para numeros
print("-----------------------SORT-----------------------")
lista1 = list([23,True, False, 55, 77, 10, 9, 79])
print(lista1)

lista1.sort()
print(lista1)
print("--------------------------------------------------")


#REVERSE-Invierte los elementos de una lista de mayor a menor
print("----------------------REVERSE---------------------")
lista1.reverse()
print(lista1)
print("--------------------------------------------------")