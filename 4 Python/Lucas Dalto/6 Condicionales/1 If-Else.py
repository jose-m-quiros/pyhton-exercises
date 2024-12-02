#if variable condicion a cumplir dato:
#   print("Si se cumple muestra esta linea")
#else:
#   print("Se muestra esta linea si la condicion no se cumple.")


edad = 20
edad = 17

if edad >= 18:
    print("Sos mayor de Edad")
    
else:
    print("Sos menor de Edad")
    
    
print("_____________________________________________________________________________")
print("_____________________________________________________________________________")


#Comparar usuarios
contraseña_almacenada = "Jose-recibe-clases-con-Dalto"
contraseña_escrita = "Jose-cambio-de-html-a-python"
print(contraseña_almacenada == contraseña_escrita)

if contraseña_almacenada == contraseña_escrita:
    print("INICIO DE SESION EXITOSO")
    
else:
    print("PORFAVOR REVISE LA CONTRASEÑA")
    
print("_______________")
print("_______________")

    
    
#Comparar usuarios 2
contraseña_almacenada2 = "Jose-recibe-clases-con-Dalto"
contraseña_escrita2 = "Jose-recibe-clases-con-Dalto"
print(contraseña_almacenada2 == contraseña_escrita2)

if contraseña_almacenada2 == contraseña_escrita2:
    print("INICIO DE SESION EXITOSO")
    
else:
    print("PORFAVOR REVISE LA CONTRASEÑA")