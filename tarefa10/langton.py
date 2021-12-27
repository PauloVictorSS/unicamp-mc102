def calcula_nova_posicao(direcoes, direcao_atual, linha_formiga, coluna_formiga):
    """
        Calcula qual vai ser a nova posição da formiga 
        com base aonde está sua direção atual
    """

    if direcoes[direcao_atual] == "N":
        return linha_formiga - 1, coluna_formiga

    if direcoes[direcao_atual] == "L":
        return linha_formiga, coluna_formiga + 1

    if direcoes[direcao_atual] == "S":
        return linha_formiga + 1, coluna_formiga

    if direcoes[direcao_atual] == "O":
        return linha_formiga, coluna_formiga - 1


def aplica_langton(tabuleiro, numero_interacoes, linha_formiga, coluna_formiga, direcoes, direcao_atual):
    """
        Recebe o atual tabuleiro, o numero de interações restantes e a posição/direção atual
        da formiga para aplicar langton e fazer a formiga 'andar' com base no estado
        atual dela
    """

    if numero_interacoes == 0:
        return

    posicao_atual_formiga = tabuleiro[linha_formiga][coluna_formiga]

    if posicao_atual_formiga == ".":
        tabuleiro[linha_formiga][coluna_formiga] = "#"

        if (direcao_atual + 1) > 3:
            direcao_atual = 0
        else:
            direcao_atual += 1
    else:
        tabuleiro[linha_formiga][coluna_formiga] = "." 

        if (direcao_atual - 1) < 0:
            direcao_atual = 3
        else:
            direcao_atual -= 1  

    nova_linha_formiga, nova_coluna_formiga = calcula_nova_posicao(direcoes, direcao_atual, linha_formiga, coluna_formiga)

    aplica_langton(tabuleiro, numero_interacoes-1, nova_linha_formiga, nova_coluna_formiga, direcoes, direcao_atual)


def main():

    numero_interacoes, numero_linhas, numero_colunas = map(int, input().split())

    tabuleiro = []
    direcoes = ["N", "L", "S", "O"]

    for _ in range(numero_linhas):
        string = input()
        linha = []
        for elemento in string:
            linha.append(elemento)

        tabuleiro.append(linha)

    linha_formiga = int((numero_linhas - 1) / 2)
    coluna_formiga = int((numero_colunas - 1) / 2)

    aplica_langton(tabuleiro, numero_interacoes, linha_formiga, coluna_formiga, direcoes, 2)

    for linha in tabuleiro:
        for elemento in linha:
            print(elemento, end="")
        print()


main()
