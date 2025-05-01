def quicksort(lista):
    if len(lista) <= 1:
        return lista
    pivo = lista[0]
    menores = [x for x in lista[1:] if x <= pivo]
    maiores = [x for x in lista[1:] if x > pivo]
    return quicksort(menores) + [pivo] + quicksort(maiores)

# Lista original
numeros = [7, 2, 9, 1, 15, 76, 3, 4, 5]

# Ordenar com quicksort
ordenada = quicksort(numeros)
print("Lista ordenada:", ordenada)

def busca_binaria(lista, )
