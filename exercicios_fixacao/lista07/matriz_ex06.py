"""
Funções para resolver o exercício 06 da lista 07,
nesse caso, o programa lê um arquivo que contém a 
matriz a ser somada
"""


def le_matriz_arquivo():

    matriz = []

    with open("matriz.txt") as arquivo:

        for linha in arquivo:
            matriz.append(list(map(int, linha.split())))

    return matriz


def somar_primeira_coluna(matriz):

    soma = 0
    for i in range(len(matriz)):

        soma += matriz[i][0]

    return soma


def somar_diagonal_principal(matriz):

    soma = 0
    for i in range(len(matriz)):

        soma += matriz[i][i]

    return soma


def somar_diagonal_secundaria(matriz):

    posicao_inicial = len(matriz) - 1

    soma = 0
    for i in range(len(matriz)):

        soma += matriz[posicao_inicial - i][i]

    return soma


def somar_todos_elementos_matriz(matriz):

    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz)):

            soma += matriz[i][j]

    return soma


def main():

    matriz = le_matriz_arquivo()

    soma_primeira_coluna = somar_primeira_coluna(matriz)
    soma_diagonal_principal = somar_diagonal_principal(matriz)
    soma_diagonal_secundaria = somar_diagonal_secundaria(matriz)
    soma_todos_elementos_matriz = somar_todos_elementos_matriz(matriz)

    print(f"A soma da primeira coluna vale {soma_primeira_coluna}")
    print(f"A soma da diagonal principal vale {soma_diagonal_principal}")
    print(f"A soma da diagonal secundária vale {soma_diagonal_secundaria}")
    print(
        f"A soma de todos os elementos da matriz vale {soma_todos_elementos_matriz}")


main()
