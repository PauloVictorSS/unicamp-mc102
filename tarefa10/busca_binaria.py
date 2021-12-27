def busca_binaria(lista_numeros, inicio, fim, numero_buscavel):
    """
    Recebe uma lista de números, e duas posições realizar a busca
    binária do 'numero_buscavel'
    """

    if fim < inicio:
        return -1

    posicao_meio = (inicio + fim) // 2

    if lista_numeros[posicao_meio] == numero_buscavel:
        return posicao_meio

    elif lista_numeros[posicao_meio] > numero_buscavel:
        return busca_binaria(lista_numeros, inicio, posicao_meio - 1, numero_buscavel)

    else:  
        return busca_binaria(lista_numeros, posicao_meio + 1, fim, numero_buscavel)


def main():

    lista_numeros = list(map(int, input().split()))
    numero_buscavel = int(input())

    resultado = busca_binaria(lista_numeros, 0, len(lista_numeros)-1, numero_buscavel)

    print(resultado)


main()
