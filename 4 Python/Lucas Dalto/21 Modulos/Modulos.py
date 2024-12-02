#Importando un modulo y asignandole un nombre mas pequeño con as
import Saludar as Sal

saludin = Sal.saludar("Manuel")
print(saludin)
print(type(Sal))
print(dir(Sal))
print(" ")


#Importando desde el modulo solo la funcion | Importando por el momento 2 funciones
#from Saludar import saludar, pollo

# saludo_1 = saludar("Quiros")
# print(saludo_1)

# saludo_2 = pollo("Chaves")
# print(saludo_2)


#Accedemos al nombre de este modulo
print(__name__)

#Accedemos al nombre del modulo llamado
print(Sal.__name__)