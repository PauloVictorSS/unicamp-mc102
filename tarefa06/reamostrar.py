import math


def listas_mesmo_tamanho(lista_de_listas):
    """
    Recebe uma lista de listas e retorna 'True' caso todas as listas
    sejam de mesmo tamanho e 'False', caso contrário
    """

    tamanho_padrao = len(lista_de_listas[0])

    for lista in lista_de_listas:
        if(len(lista) != tamanho_padrao):
            return False

    return True


def computa_menor_tamanho_lista(lista_de_listas):
    """
    Recebe uma lista de listas e retorna o tamanho da menor lista
    """

    menor_lista = len(lista_de_listas[0])

    for lista in lista_de_listas:
        if(len(lista) < menor_lista):
            menor_lista = len(lista)

    return menor_lista


def reamostragem(lista_sinais, menor_sinal):
    """
    Recebe uma lista de lista de números que representam sinais 
    sonoros e o tamanho do menor sinal e retorna uma nova lista
    de sinais sonoros com todos os sinais reamostrados e de mesmo
    tamanho 
    """

    nova_lista_sinais = []

    for sinal in lista_sinais:
        sinal_reamostrado = []
        d = len(sinal)/menor_sinal

        for j in range(menor_sinal):

            fator_dj = math.ceil(d * j)
            fator_dj_mais_j = math.ceil(d * j + d)

            soma = 0
            termos = 0

            if(len(sinal) <= fator_dj_mais_j):
                fator_dj_mais_j = len(sinal)

            for i in range(fator_dj, fator_dj_mais_j):
                termos += 1
                soma += sinal[i]

            amostra = soma/termos
            sinal_reamostrado.append(amostra)

        nova_lista_sinais.append(sinal_reamostrado)

    return nova_lista_sinais


def media_listas(matriz):
    """
    Recebe uma matriz de números e retorna uma lista sendo o 
    elemento da i-ésima posição a média de todos os elementos 
    da i-ésima coluna da matriz
    """

    total_listas = len(matriz)
    tamanho_listas = len(matriz[0])

    nova_lista_media = []

    for i in range(tamanho_listas):
        soma = 0
        for lista in matriz:
            soma += lista[i]

        media = soma/total_listas
        nova_lista_media.append(round(media, 2))

    return nova_lista_media


def main():

    numero_sinais = int(input())
    lista_sinais = []

    for _ in range(numero_sinais):
        sinal = list(map(float, input().split()))
        lista_sinais.append(sinal)

    if not listas_mesmo_tamanho(lista_sinais):
        tamanho_menor = computa_menor_tamanho_lista(lista_sinais)

        if(tamanho_menor == 0):
            return

        lista_sinais = reamostragem(lista_sinais, tamanho_menor)

    sinais_combinados = media_listas(lista_sinais)

    for amostra in sinais_combinados:

        print(f"{amostra:.2f}", end=" ")


main()
