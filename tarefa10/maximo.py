def maior_numero_lista(lista_numeros, posicao_n):
    """
        Determina o maior elemento de uma lista
        recebendo a posição_n de um elemento da lista
        e comparando com o resto
    """

    if posicao_n == 0:
        return lista_numeros[0]

    maior_elemento = maior_numero_lista(lista_numeros, posicao_n - 1)

    if lista_numeros[posicao_n] > maior_elemento:
        return lista_numeros[posicao_n]
    else:
        return maior_elemento


def main():

    lista_numeros = list(map(int, input().split()))

    maior_numero = maior_numero_lista(lista_numeros, len(lista_numeros) - 1)

    print(maior_numero)


main()
