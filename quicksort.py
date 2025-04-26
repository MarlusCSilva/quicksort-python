# Quick Sort
def quicksort (arr, left, right):
    pi = partition(arr, left, right)
    # se for menor que o pivor, ira para esquerda
    quicksort(arr, left, pi-1)
    # se for maior que o pivor, ira para direita
    quicksort(arr, pi+1, right)

def partition(arr, left, right):
    pivot = arr[right]
    i = left = 1
    for j in range(left, right):
        if arr[j] <= pivot:
            i = i +1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[right] = arr[right], arr[i+1]
    return i+1

# pora Quick Sort
# Melhor caso O(n log n) 
# Medio caso O(n log n)
# Pior caso O(n²)

#  para Busca Binária
# Melhor caso O(1) - O(log n)
# Medio caso O(log n)
# Pior caso O(log n)