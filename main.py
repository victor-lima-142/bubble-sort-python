lista = [10, 5, 2, 3, 9, 8, 6, 4, 7, 1]

def bubble_sort(lista):
    lista_ordenada = lista
    for i in range(len(lista_ordenada) - 1):
        for j in range(0, len(lista_ordenada)-i-1):
            if lista_ordenada[j] > lista_ordenada[j + 1]:
                lista_ordenada[j], lista_ordenada[j + 1] = lista_ordenada[j + 1], lista_ordenada[j]
    return lista_ordenada


print(bubble_sort(lista))