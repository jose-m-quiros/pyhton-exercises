#Operadores Aritmeticos

# + = Suma

# - = Resta

# * = Multiplicacion

# / = Division

# % = Modulo-Devuleve el resto de la divicion

# ** = Exponente-Realiza exponencial

# // = Divicion Baja-Devuelve el entrero de la division


#Suma y resta ( + -)
suma = 12 + 12
resta = 10 - 1
print(suma)
print(resta)

#Multiplicacion y Divicion (* /)
multiplicacion = 12 * 12
division = 12 / 5 #Devuelve un dato float(Flotante)
print(multiplicacion)
print(division)

#Resto o Modulo | Se usa para determinar que cantidad queda entre 
#Ejemplo: Cuantas veces cabe el 5 en el 12? solo 2 veces "5 + 5 = 10", una ves realizada esta operacion lo que hacer es determinar cuanto falta para llegar a 12
#Para llegar a 12 faltan 2 entonces esto es lo que hace resto mostar cuanto hace falta para llegar a la "meta".
resto = 12 % 5
print(resto)


#Exponente
exponentes = 12 ** 5
print(exponentes)

#Division Baja
divi_baja = 12 // 6 #Devuelve entero redondeado hacia abajo
print(divi_baja)




#Para saber que tipo de dato es se puede usar
#type(dato) y esto nos devuelve que tipo de dato es
tipo_dato = type("jose")
print(tipo_dato)