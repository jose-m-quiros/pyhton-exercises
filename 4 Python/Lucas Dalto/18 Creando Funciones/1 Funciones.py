#Creando una funcion simple
def pollo():
    print("Dalto es mi profesor de HTML, CSS, JAVASCRIPT, PYTHON, COMING SOON: SQL, Inteligencia Artificial")

#Imprime la funcion
pollo()


print("--------------------------------------------")


#Que es un parametro: Es una variable |  Solo que existente dentro de una funcion afuera no existe
#Los parametros son variables que se crean para ser usadas dentro de la funcion y despues ya no se hace mas 
#Creando una funcion con parametros
def saludar(nombre, sexo):
    sexo.lower()
    if (sexo == "mujer"):
        adjetivo = "Amiga"
    
    elif (sexo == "hombre"):
        adjetivo = "Amigo"
    
    else:
        adjetivo = ""
    
        
    print(f"Hola {nombre}")
    print(f"Gracias {adjetivo} por contratar un servicio CSW")
    
    
saludar("Jose", "hombre")
print("--------------------------------------------")
saludar("Camila", "mujer")
print("--------------------------------------------")
saludar("Pollo", "No se sabe")


print("--------------------------------------------")

#Creando una funcion que nos retorna valores
def crear_contra(num):
    chars = "ABcDefGhIjKlMnOpQ@!#&%"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num -2
    c2 = num
    c3 = num -5
    c4 = num -1
    c5 = num
    c6 = num -3
    c7 = num -7
    c8 = num
    c9 = num -6
    c10 = num -8
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{chars[c4]}{chars[c5]}{chars[c6]}{chars[c7]}{chars[c8]}{chars[c9]}{chars[c10]}{num * 2}"
    return contraseña
    
password = crear_contra(2)
pas = f"Tu nueva contraseña a sido asignada: {password}"
print(pas)


print("--------------------------------------------")

#Creando una funcion que nos retorne multiples valores
def crear_contra_multiple(num_multiple):
    chars_multiple= "ABcDefGhIjKlMnOpQ@!#&%"
    num_entero_multiple = str(num_multiple)
    num_multiple = int(num_entero_multiple[0])
    c11 = num_multiple -2
    c12 = num_multiple
    c13 = num_multiple -5
    c14 = num_multiple -1
    c15 = num_multiple
    c16 = num_multiple -3
    c17 = num_multiple -7
    c18 = num_multiple
    c19 = num_multiple -6
    c20 = num_multiple -8
    contraseña_multiple = f"{chars_multiple[c11]}{chars_multiple[c12]}{chars_multiple[c13]}{chars_multiple[c14]}{chars_multiple[c15]}{chars_multiple[c16]}{chars_multiple[c17]}{chars_multiple[c18]}{chars_multiple[c19]}{chars_multiple[c20]}{num_multiple * 2}"
    return contraseña_multiple, num_multiple

#Desempaquetando la funcion
password_multiple, primer_numero = crear_contra_multiple(630)
    
#Mostrando los resultados obtenidos y los utilizados para obtenerlo 
print(f"Tu contraseña nueva es: {password_multiple}")
print(f"El numero que se utilizo fue: {primer_numero}")

