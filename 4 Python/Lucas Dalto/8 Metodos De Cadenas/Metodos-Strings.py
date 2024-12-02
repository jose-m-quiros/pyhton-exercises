#Metodo y funcion no es lo mismo, porque todo los metodos son funciones pero no todas las funciones son metodos
#Porque los metodos son funciones especificas de objetos, y si no es una funcion de un objeto no es un metodo


#Ejemplos
#Nombre De Funcion(Parametros)
print("Pollo") #Imprime lo que se le esta indicando

type(2) #Deveuelve que tipo de dato es si es number, strings o alguno otro
print("--------------------------------------------------")


cadena1 = "Estamos recibiendo Clases con el profe Dalto"
cadena2 = "Bienvenido"
cadena2_5 = 56
cadena3 = "1234567890"
cadena4 = "todoPegadoesunaalfanumerico" #NO CUENTAN LOS ESPACIOS NI NINGUNO

# DIR-devuelve la lista de atributos válidos del objeto pasado. | No es un metodo es una funcion
print("-----------------------DIR------------------------")
print("----------------------Texto-----------------------")
print(dir(cadena1))#Esto que nos devuelve son todas las cosas que podemos hacer con esto
print("--------------------------------------------------")
print("----------------------Number----------------------")
print(dir(1))
print("--------------------------------------------------")
print("----------------------Strings---------------------")
print(dir("Baby Father 2.0"))
print("--------------------------------------------------")
print("----------------------Lista-----------------------")
print(dir(["Lista"]))
print("--------------------------------------------------")
print("--------------------------------------------------")




print("-------------------UPPER--------------------------")
#UPPER-CONVIERTE A MAYUSCULA TODO 
#Metodo: Dato.Metodo()
pollo = cadena1.upper()
print(pollo)
print("--------------------------------------------------")


print("-------------------LOWER--------------------------")
#lower-convierte a minuscula
pollo2 = cadena1.lower()
print(pollo2)
print("--------------------------------------------------")


print("-----------------CAPITALIZE-----------------------")
#Capitalize-primera en mayuscula
primletM = cadena1.capitalize()
print(primletM)
print("--------------------------------------------------")
print("--------------------------------------------------")





print("--------------------FIND--------------------------")
#FIND-Metodo-Encuentra la primera aparición del valor especificado, sino devuelve una excepción | Sencible a mayusculas y minusculas
find = cadena1.find("z") #Si FIND te tira -1 es que el valor solicitado no esta.
print(find)
print("--------------------------------------------------")

print("-------------------INDEX--------------------------")
find2 = cadena1.index("a") #Si INDEX te tira un error es que el valor solicitado no esta. Tiene que estar el mismo valor
                           #Es decir si busco 5 y el valor que esta almacenado en la variable es 56 va a tirar un error 
                           # ya que el busca lo que sea igual a lo que se le esta pidiendo
print(find2)
print("--------------------------------------------------")
print("--------------------------------------------------")





print("------------------ISNUMERIC-----------------------")
#ISNUMERIC-Si es numerico devuelve true si no nos devuelve false
numerico = cadena3.isnumeric()
print(numerico)
print("--------------------------------------------------")


print("-------------------ISALPHA------------------------")
#ISALPHA-Si es alfa-numérico devuelve true si no nos devuelve false
alfa = cadena3.isalpha()
print(alfa)

alfa2 = cadena4.isalpha()
print(alfa2)
print("--------------------------------------------------")
print("--------------------------------------------------")






print("--------------------COUNT-------------------------")
#COUNT-Cuenta las coincidencias de una cadena, dentro de otra cadena, devuelve la cantidad de coincidencias
contar_coincidencia = cadena1.count("e") #Y si no lo encuentra da 0
print(contar_coincidencia)
print("--------------------------------------------------")


print("---------------------LEN--------------------------")
#LEN-Cuenta los caracteres de una cadena | Len es una funcion pero no es un metodo.
contar = len(cadena1)
print(contar)
print("--------------------------------------------------")
print("--------------------------------------------------")





print("-------------------ENDSWITH-----------------------")
#ENDSWITH-verifica si una cadena termina con otra cadena dada, si es asi devuelve True
termina = cadena1.endswith("o")
print(termina)
print("--------------------------------------------------")


print("------------------STARTSWITH----------------------")
#STARTSWITH-verifica si una cadena comienza con otra cadena dada, si es asi devuelve True
empieza = cadena1.startswith("H")
print(empieza)
print("--------------------------------------------------")
print("--------------------------------------------------")





print("--------------------REPLACE-----------------------")
#REPLACE-Remplaza un fracmento del valor dado por otro dado
#Si el valor 1 se encuentra en la cadena original remplaze el valor 1 por el valor 2
remplaze = cadena1.replace("Dalto","Lucas") #Si encuentra una coincidencia en la cadena que le pasamos esa coincidencia la va a remplazar por lo que le pasemos despues
                                            #Pero si no encuentra coincidencia devuelve la cadena anterior.
print(remplaze)
remplaze_new = remplaze.upper() #Esto es opcional
print(remplaze_new)
print("--------------------------------------------------")


print("---------------------SPLIT------------------------")
#SPLIT-Separa cadenas con la cadena que le pasemos
cad_sep = cadena1.split(" ")
print(cad_sep)
