import sys


def kernel_do_filtro(nome_filtro):
    """
    Entrada: Uma string que representa um nome de um filtro
    Saída: O uma matriz que representa o'Kernel' correspondente 
    ao nome do filtro recebido
    """

    kernels_filtros = [
        [
            [-1, -1, -1],
            [-1, 8, -1],
            [-1, -1, -1]
        ],
        [
            [0, -1, 0],
            [-1, 5, -1],
            [0, -1, 0]
        ],
        [
            [1, 0, -1],
            [2, 0, -2],
            [1, 0, -1]
        ],
        [
            [-2, -1, 0],
            [-1, 1, 1],
            [0, 1, 2]
        ],
        [
            [0.04, 0.04, 0.04, 0.04, 0.04],
            [0.04, 0.04, 0.04, 0.04, 0.04],
            [0.04, 0.04, 0.04, 0.04, 0.04],
            [0.04, 0.04, 0.04, 0.04, 0.04],
            [0.04, 0.04, 0.04, 0.04, 0.04]
        ],
        [
            [-0.00390625, -0.015625, -0.0234375, -0.015625, -0.00390625],
            [-0.015625, -0.0625, -0.09375, -0.0625, -0.015625],
            [-0.0234375, -0.09375, 1.859375, -0.09375, -0.0234375],
            [-0.015625, -0.0625, -0.09375, -0.0625, -0.015625],
            [-0.00390625, -0.015625, -0.0234375, -0.015625, -0.00390625]
        ]
    ]

    nome_filtros = [
        "bordas",
        "sharpen",
        "left_sobel",
        "emboss",
        "blur",
        "unsharp"
    ]

    return kernels_filtros[nome_filtros.index(nome_filtro)]


def ler_imagem(nome_imagem):
    """
    Entrada: Um caminho de um arquivo ppm
    Saída: A largura, a altura e a matriz com os números que 
    correspondem a imagem em si
    """

    matriz_imagem = []

    with open(nome_imagem) as arquivo:

        tipo = arquivo.readline().strip()
        largura, altura = map(int, arquivo.readline().strip().split())
        tamanho_maximo = arquivo.readline().strip()

        for linha in arquivo:
            linha = list(map(int, linha.split()))
            matriz_imagem.append(linha)

    return largura, altura, matriz_imagem


def calcula_matriz_pixels_convolucao(i, j, fator, matriz_imagem):
    """
    Entrada: posição [i][j] do elemento da [matriz_imagem] e o [fator],
    que serve para saber quantas linhas e colunas serão analisadas para 
    a realização da convolução
    Saída: uma matriz com lista de elementos da [matriz_imagem] que serão 
    usados no cálculo da convolução do elemento na posição [i][j]
    """

    pixels_convolucao = []

    """
    As variáveis 'l' e 'k' serve para saber quantas linhas e colunas, 
    respectivamente, acima e abaixo do elemento na posição [i][j] temos 
    que verificar para achar os outros elementos adjacentes a ele que 
    serão usados para fazer a convolucao
    """

    for l in range(-fator, fator+1):

        linha = []
        for k in range(-fator, fator+1):

            pixel_adjacente = matriz_imagem[i + l][j + k*3]

            linha.append(pixel_adjacente)

        pixels_convolucao.append(linha)

    return pixels_convolucao


def verifica_dentro_range(novo_elemento):

    # Verificando se o elemento não saiu do range(0,255)
    if novo_elemento > 255:
        return 255
    elif novo_elemento < 0:
        return 0

    return novo_elemento


def aplicar_filtro(largura, altura, matriz_imagem, kernel):

    matriz_imagem_filtrada = []

    largura *= 3
    tamanho_kernel = len(kernel)

    # Para saber quantas linhas acima e abaixo do elemento vou ter que usar na soma
    # É necessário para casos onde o kernel é diferente do padrão 3x3
    fator = tamanho_kernel // 2

    for i in range(altura):
        linha = []
        for j in range(largura):
            novo_elemento = 0

            # Verificando se o elemento não está na borda
            if (i >= (1*fator) and i < (altura - (1*fator))) and (j >= (3*fator) and j < (largura - (3*fator))):

                # Chamando a função para achar os elementos que serão usados na convolução
                pixels_para_convolucao = calcula_matriz_pixels_convolucao(
                    i, j, fator, matriz_imagem)

                # Realizando a convolução para achar o novo elemento da posição [i][j]
                for l in range(len(kernel)):
                    for k in range(len(kernel)):
                        novo_elemento += pixels_para_convolucao[l][k] * \
                            kernel[l][k]

                novo_elemento = verifica_dentro_range(novo_elemento)

            linha.append(int(novo_elemento))
        matriz_imagem_filtrada.append(linha)

    return matriz_imagem_filtrada


def escrever_imagem(largura, altura, matriz_filtrada, nome_arquivo):
    """
    Entrada: a largura e a altura da imagem, uma matriz que representa
    a imagem com o filtro aplicado e o nome do arquivo a ser criado
    Saída: Não retorna nada, mas cria um arquivo com o nome recebido
    contendo as informações recebidas
    """

    with open(nome_arquivo, "w") as arquivo:
        arquivo.write("P3\n")
        arquivo.write(f"{largura} {altura}\n")
        arquivo.write(f"255\n")

        for linha in matriz_filtrada:
            linha_arquivo = ' '.join(map(str, linha))

            arquivo.write(f"{linha_arquivo}\n")


def main():

    if(len(sys.argv) >= 4):
        nome_filtro = sys.argv[1]
        nome_imagem = sys.argv[2]
        nome_nova_imagem = sys.argv[3]

        kernel = kernel_do_filtro(nome_filtro)
        largura, altura, matriz_imagem = ler_imagem(nome_imagem)
        matriz_filtrada = aplicar_filtro(largura, altura, matriz_imagem, kernel)

        escrever_imagem(largura, altura, matriz_filtrada, nome_nova_imagem)


if __name__ == "__main__":
    main()
