import modulo_analise as ma
import sys

def ler_arquivo(info):
    """
    Lê o arquivo filmes.dat, cria diversas listas com
    os indices, paises, anos, classificações e durações
    de cada filme e retorna uma dessas listas com base 
    no parâmtro recebido

    Parâmetros: String com o nome da lista a ser devolvida
    Retorna: Uma lista de strings com as informações pedidas
    """

    indices = []
    paises = []
    anos = []
    classes = []
    duracoes = []

    with open("testes/filmes.dat") as f:

        for linha in f:
            indice, pais, ano, classe, duracao = linha.split()
            indices.append(int(indice))
            paises.append(pais)
            anos.append(int(ano))
            classes.append(classe)
            duracoes.append(int(duracao))

    if(info == "indices"):
        return indices
    elif(info == "paises"):
        return paises
    elif(info == "anos"):
        return anos
    elif(info == "classes"):
        return classes
    elif(info == "duracoes"):
        return duracoes
    

def produtividade(inicio, fim):
    """
    Recebe dois anos e retorna uma lista de strings que 
    informam a quantidade de filmes produzidos em cada ano
    dentro do intervalo recebido

    Parâmetros: Dois inteiros -> Um intervalo de anos 
    Retorna: Uma lista de strings com a quantidade de filmes 
    do ano correspondente e o respectivo ano
    """

    resultado = []

    anos = ler_arquivo("anos")

    for ano in range(inicio, fim+1):
        qtd_filmes = 0

        for lancamento in anos:
            if lancamento == ano:
                qtd_filmes += 1

        texto = str(ano) + ": " + str(qtd_filmes)
        resultado.append(texto)

    return resultado


def anos_presentes(inicio, fim):
    """
    Recebe dois anos e retorna a lista de todos os anos 
    que tiveram filmes dentro desse intervalo

    Parâmetros: Dois inteiros -> Um intervalo de anos 
    Retorna: Uma lista de todos os anos dentro do intervalo
    que tiveram filmes
    """

    resultado = []

    anos = ler_arquivo("anos")
    anos = ma.remove_duplicatas(anos)
    anos.sort()

    for ano in anos:
        if(ano >= inicio) and (ano <= fim):
            resultado.append(ano)

    return resultado


def filmes_por_classificacao(classificacao):
    """
    Recebe uma classificaçao e retorna uma lista de índices
    dos filmes que têm a classificação recebida

    Parâmetros: Uma strig correspondente a classificação do filme
    Retorna: Uma lista dos índices dos filmes que contém a 
    classificação indicativa
    """

    indices = ler_arquivo("indices")
    classes = ler_arquivo("classes")

    indice_filme_classificados = ma.filtrar_caracteristica(indices, classes, classificacao)
    indice_filme_classificados.sort()

    return indice_filme_classificados


def histograma_dos_anos(intervalos):
    """
    Recebe uma lista de intervalos de anos e retorna uma lista de
    strings com a quantidade de filmes no intervalo correspondente 
    e o seu respectivo intervalo

    Parâmetros: Uma lista com inteiros
    Retorna: Uma lista de strings com a quantidade de filmes no 
    intervalo correspondente e o respectivo intervalo
    """

    resultado = []
    anos = ler_arquivo("anos")

    anos = [int(valor) for valor in anos]

    qtd_histograma = ma.histograma(anos, intervalos)

    for i in range(len(intervalos)-1):

        menor = str(intervalos[i])
        maior = str(intervalos[i+1])

        texto = "[" + menor + ", " + maior + "): " + str(qtd_histograma[i])
        resultado.append(texto)
    
    return resultado


def filmes_por_pais_e_classificacao(pais, classificacao):
    """
    Recebe um país e uma classificação e retorna uma lista contendo
    todos os índices dos filmes que foram lançados no país e que tem a
    classificação indicativa que foram recebidos nos parâmetros

    Parâmetros: Duas strings -> Um país e uma classificação
    Retorna: Uma lista dos índices dos filmes que foram lançados no país 
    e que tem a classificação indicativa que foram recebidos nos parâmetros
    """


    indices = ler_arquivo("indices")
    paises = ler_arquivo("paises")
    classes = ler_arquivo("classes")

    filtro_paises = ma.filtrar_caracteristica(indices, paises, pais)

    classifacoes_filmes = []
    for indice in filtro_paises:
        classifacoes_filmes.append(classes[indices.index(indice)])

    filmes_pais_classificacao = ma.filtrar_caracteristica(filtro_paises, classifacoes_filmes, classificacao)
    filmes_pais_classificacao.sort()

    return filmes_pais_classificacao


def main():

    if(len(sys.argv) >= 2):
        acao = sys.argv[1]

        if(acao == "produtividade"):
            anos = list(map(int, input().split()))
            resultados = produtividade(anos[0], anos[1])

        elif(acao == "anos_presentes"):
            anos = list(map(int, input().split()))
            resultados = anos_presentes(anos[0], anos[1])

        elif(acao == "filmes_por_classificacao"):
            classificacao = input()
            resultados = filmes_por_classificacao(classificacao)
        
        elif(acao == "histograma_dos_anos"):
            intervalos = list(map(int, input().split()))
            resultados = histograma_dos_anos(intervalos)

        elif(acao == "filmes_por_pais_e_classificacao"):
            pais, classificacao = input().split()
            resultados = filmes_por_pais_e_classificacao(pais, classificacao)

        for result in resultados:
            print(result)


main()