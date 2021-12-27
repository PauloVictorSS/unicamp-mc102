def elementosNaoListados(lista_1, lista_2):
    """
        Recebe duas listas e retorna os elementos da 
        lista 1 que não tem na lista 2
    """

    lista_elementos_faltam = []
    i = 0
    j = 0

    max_lista_2 = max(lista_2)

    """
        Com as listas ordenadas vamos comparar os elementos
        de mesma posição, a princípio e, com base no resultado,
        vamos para os próximos elementos ou não
    """

    while i < len(lista_1) and j < len(lista_2):

        """
            Se o elemento da lista 1 for menor que o da lista 2,
            ou maior que o maior elemento da lista 2, como as
            listas estão ordenadas, não tem como comprarmos o
            elemento da lista 1
        """
        if(lista_2[j] > lista_1[i] or lista_1[i] > max_lista_2):
            lista_elementos_faltam.append(lista_1[i])
            i += 1
            continue
        if (lista_2[j] < lista_1[i]):
            j += 1
            continue

        i += 1
        j += 1

    if i < len(lista_1):
        for k in range(i, len(lista_1)):
            lista_elementos_faltam.append(lista_1[k])

    return lista_elementos_faltam


def main():

    lista_1 = list(map(int, input().split()))
    lista_2 = list(map(int, input().split()))

    lista_1.sort()
    lista_2.sort()

    lista_elementos_faltam = elementosNaoListados(lista_1, lista_2)

    for elemento in lista_elementos_faltam:
        print(elemento, end=" ")


main()
