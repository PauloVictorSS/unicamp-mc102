def calcula_probabilidade(numero_jogadas_restantes, distancia_atual):
    """
        Recebe um número de jogadas restantes e a distância altual para
        calcular a probalidade de se conseguir percorrer exatamente essa
        distância com 'n' jogadas de dados
    """

    if(distancia_atual == 0):
        return 1   

    if(numero_jogadas_restantes == 0):
        return 0

    soma = 0

    for i in range(1,7):
        if(distancia_atual - i >= 0):
            soma += calcula_probabilidade(numero_jogadas_restantes - 1, distancia_atual - i)/6

    return soma


def main():
    numero_jogadas, distancia = map(int, input().split())

    probabilidade = calcula_probabilidade(numero_jogadas, distancia)

    print(f"{probabilidade:.3f}")


main()