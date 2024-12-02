def suma():
    
    while True:

        a = input("1:")
        b = input("2:")

        try:
            resultado = int(a) + int(b)
        except:
            print("Porfavor Solo Ingresa Numeros")
        else:
            break
        finally:
            print("Manejo De Exepcion Finalizado")

    return resultado


print(f"El resultado es {suma()}")
