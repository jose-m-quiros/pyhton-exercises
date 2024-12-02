def ordenar(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

entrada = input("Ingresa una lista de números separados por comas: ")
numeros = [int(x) for x in entrada.split(",")]
ordenar(numeros)
print(numeros)
