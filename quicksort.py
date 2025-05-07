#Funcão Quicksort para ordernar os elementos/vetores.
def quicksort(lista):
    if len(lista) <= 1: # Se a lista tem 1 ou nenhum elemento, ela já está ordenada, então retornamos a lista.
        return lista
    pivo = lista[0]  # Pivô escolhido como o primeiro elemento da lista.
    menor = [x for x in lista[1:] if x <= pivo] # quando o elemento for menor ou igual que o pivor, vai para a esqueda .
    maior = [x for x in lista[1:] if x > pivo] # quando o elemento for maior que o pivor, vai pra esqueda.
    return quicksort(menor) + [pivo] + quicksort(maior)  
# Chamamos o quicksort nas listas menor e maior, e retornamos a junção delas com o pivô no meio.

# Lista não ordenada
ListaNodernada = [7, 2, 9, 1, 15, 76, 3, 4, 5] # [1, 2, 3, 4, 5, 7, 9, 15, 76]
print("Lista Não ordernada:", ListaNodernada)

# Ordenar com quicksort
ordenada = quicksort(ListaNodernada)
print("Lista ordenada:", ordenada)

#Numero que o usuario procura na lista que foi disponibilizada
numeroPd = int(input("Escolha um numero da lista: "))

#Função Busca Binaria
def busca_binaria(lista, numeroPd, inicio, fim):
    # numero não encontrado, ou seja o numero procurado não estava no inicio, meio e final, não havendo necessidade de verificar dnv.
    if inicio > fim:
        return -1 
    
    # Calcula o índice do meio da lista.
    meio = (inicio + fim) // 2

    # Verifica se o número do meio é o número procurado
    if lista[meio] == numeroPd:
        return meio  # Retorna a posição onde o número foi encontrado.
    
    elif lista[meio] < numeroPd: # Se o número do meio for menor que o numeroPd, busca na metade direita da lista.
        return busca_binaria(lista, numeroPd, meio + 1, fim)
    
    else: # Se o número do meio for maior que o numeroPd, busca na metade esquerda da lista.
        return busca_binaria(lista, numeroPd, inicio, meio - 1)

# Chamada inicial da função, passando os limites da lista (0 ao último índice).
position = busca_binaria(ordenada, numeroPd, 0, len(ordenada) - 1)

# Verifica o resultado da busca e imprime a posição, se encontrada.
if position != -1:
    print(f"O número {numeroPd} foi encontrado na posição {posi}.")
else:
    print(f"O número {numeroPd} não foi encontrado na lista de elementos.")