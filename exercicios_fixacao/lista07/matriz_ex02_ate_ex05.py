"""
Conjunto de funções dos exercícios 2,3,4 e 5
da lista 07 sobre matriz
"""


def eh_quadrada(matriz):

    numero_linhas = len(matriz)

    for linha in matriz:
        if(len(linha) != numero_linhas):
            return False

    return True


def eh_simetrica(matriz):

    if eh_quadrada(matriz):

        numero_linhas = len(matriz)
        numero_colunas = len(matriz[0])

        for i in range(numero_linhas):
            for j in range(numero_colunas):

                if(matriz[i][j] != matriz[j][i]):
                    return False

        return True
    else:
        return False


def calcula_matriz_transposta(matriz):

    numero_linhas = len(matriz)
    numero_colunas = len(matriz[0])

    matriz_transposta = []

    for i in range(numero_linhas):

        linha = []
        for j in range(numero_colunas):

            linha.append(matriz[j][i])

        matriz_transposta.append(linha)

    return matriz_transposta


def calcula_determinante_3(matriz):

    determinante = 0

    for j in range(3):

        multiplic = 1
        multiplic2 = 1
        for k in range(3):

            multiplic *= matriz[0 + k][(j + k) % 3]
            multiplic2 *= matriz[2 - k][(j + k) % 3]

        determinante += multiplic - multiplic2

    return determinante
