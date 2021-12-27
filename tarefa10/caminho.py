import fileinput


def testa_nova_posicao(labirinto, caminhos_ja_passado, i_atual, j_atual):
    """
        Retorna qual caminho seguir com base nas paredes do
        labirinto (elementos com '#') e também com base em 
        um caminho que ele já passou
    """

    if labirinto[i_atual+1][j_atual] != "#":
        i_novo, j_novo = i_atual+1, j_atual
        caminhos_ja_passado.append([i_novo, j_novo])

    elif labirinto[i_atual][j_atual+1] != "#":
        i_novo, j_novo = i_atual, j_atual+1
        caminhos_ja_passado.append([i_novo, j_novo])

    elif labirinto[i_atual][j_atual-1] != "#":
        i_novo, j_novo = i_atual, j_atual-1
        caminhos_ja_passado.append([i_novo, j_novo])

    elif labirinto[i_atual-1][j_atual] != "#":
        i_novo, j_novo = i_atual-1, j_atual
        caminhos_ja_passado.append([i_novo, j_novo])

    else:
        caminhos_ja_passado.remove([i_atual, j_atual])

        ultimo_caminho = caminhos_ja_passado[len(caminhos_ja_passado) - 1]
        i_novo = ultimo_caminho[0]
        j_novo = ultimo_caminho[1]
        labirinto[i_novo][j_novo] = ' '

    labirinto[i_atual][j_atual] = "#"
    return i_novo, j_novo


def acha_caminho(labirinto, posicao_atual, caminhos_ja_passado):
    """
        Recebe o labirinto, a posição atual e uma lista de
        caminhoa já percorridos e só retorna quando na posicao
        atual estiver o S (resolveu o labirinto)
    """

    i_atual = posicao_atual[0]
    j_atual = posicao_atual[1]

    if labirinto[i_atual][j_atual] == 'S':
        return

    i_novo, j_novo = testa_nova_posicao(
        labirinto, caminhos_ja_passado, i_atual, j_atual)

    acha_caminho(labirinto, [i_novo, j_novo], caminhos_ja_passado)


def main():

    labirinto = []
    caminhos_ja_passado = []

    for linha in fileinput.input():
        linha_final = list(linha.rstrip())
        labirinto.append(linha_final)

    j_atual = labirinto[0].index('E')
    posicao_atual = [0, j_atual]

    caminhos_ja_passado.append(posicao_atual)

    acha_caminho(labirinto, posicao_atual, caminhos_ja_passado)

    for posicao in caminhos_ja_passado:
        print(' '.join(map(str, posicao)))


main()
