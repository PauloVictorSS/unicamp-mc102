import random


def embaralha_lista(lista):

    tamanho_lista = len(lista)

    for i in range(random.randint(10, 100)):

        posi_aux_1 = random.randint(0, (tamanho_lista-1))
        posi_aux_2 = random.randint(0, (tamanho_lista-1))

        aux = lista[posi_aux_1]
        lista[posi_aux_1] = lista[posi_aux_2]
        lista[posi_aux_2] = aux

    return lista


def main():

    lista = list(map(int, input().split()))
    lista_embaralhada = embaralha_lista(lista)

    print(lista_embaralhada)


main()
