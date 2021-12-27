import sys


def ler_imagem(nome_imagem):
    """
    Entrada: Um caminho de um arquivo pbm
    Saída: A largura, a altura e a matriz com os números que 
    correspondem a imagem em si
    """ 

    matriz_imagem = []
    imagem = []

    with open(nome_imagem) as arquivo:
        for linha in arquivo:
            linha = list(linha.split())
            imagem.append(linha)

    largura, altura = map(int, imagem[1])

    for i in range(2, len(imagem)):
        linha = list(map(int, imagem[i]))
        matriz_imagem.append(linha)

    return largura, altura, matriz_imagem


def destacar_bordas(largura, altura, matriz_imagem):
    """
    Entrada: largura, altura e uma matriz que representa a imagem
    em si. Calcula uma matriz que representa as bordas da imagem dada
    Saída: uma matriz que representa a borda da imagem da matriz
    da entrada
    """

    matriz_borda = []

    for i in range(altura):

        linha = []

        for j in range(largura):

            if(matriz_imagem[i][j] == 1):

                elementos_adjacentes = []
                passou = True

                #Matriz dos elementos adjacentes ao elemento [i][j]
                elementos_adjacentes = [
                    matriz_imagem[i-1][j-1],
                    matriz_imagem[i-1][j],
                    matriz_imagem[i-1][j+1],
                    matriz_imagem[i][j-1],
                    matriz_imagem[i][j+1],
                    matriz_imagem[i+1][j-1],
                    matriz_imagem[i+1][j],
                    matriz_imagem[i+1][j+1]
                ]

                #Verifica se algum elemeto adjacamente é igual a 0
                for elemento in elementos_adjacentes:
                    if elemento == 0:
                        passou = False
                        linha.append(1)
                        break

                if passou:
                    linha.append(0)
            else:
                linha.append(0)

        matriz_borda.append(linha)

    return matriz_borda


def escreve_imagem(largura, altura, matriz_imagem, nome_arquivo):
    """
    Entrada: a largura e a altura da imagem, uma matriz que representa
    a borda da imagem e o nome do arquivo a ser criado
    Saída: Não retorna nada, mas cria um arquivo com o nome recebido
    contendo as informações recebidas
    """


    with open(nome_arquivo, "w") as arquivo:
        arquivo.write("P1\n")
        arquivo.write(f"{largura} {altura}\n")

        for linha in matriz_imagem:
            linha_arquivo = ' '.join(map(str, linha))

            arquivo.write(f"{linha_arquivo}\n")


def main():

    if(len(sys.argv) >= 3):
        nome_imagem = sys.argv[1]
        nome_nova_imagem = sys.argv[2]

        largura, altura, matriz_imagem = ler_imagem(nome_imagem)
        matriz_borda = destacar_bordas(largura, altura, matriz_imagem)
        escreve_imagem(largura, altura, matriz_borda, nome_nova_imagem)


if __name__ == "__main__":
    main()
