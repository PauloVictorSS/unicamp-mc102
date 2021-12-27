def ordena(lista, maior):
    """
    Ordena 'lista' do maior para o menor, caso 'maior' seja True; caso
    contrário, ordena do menor para o maior. Essa função modifica a lista
    passada por parâmetro.

    Parâmetros: lista de números ou strings e um booleano.
    Retorna: nada.
    """

    if maior:
        for i in lista:
            for j in range(len(lista)-1):
                valor = lista[j]
                valor_comp = lista[j+1]

                if (valor < valor_comp):
                    lista[j+1] = valor
                    lista[j] = valor_comp
    else:
        for i in lista:
            for j in range(len(lista)-1):
                valor = lista[j]
                valor_comp = lista[j+1]

                if (valor > valor_comp):
                    lista[j+1] = valor
                    lista[j] = valor_comp


def moda(lista):
    """
    Encontra a moda de 'lista', isto é, o valor que mais se repete; em caso de
    empate, retorne o que aparece primeiro.

    Parâmetros: lista de strings.
    Retorna: a moda de 'lista'.
    """

    """
    Nesse caso, optei por verificar quantas vezes cada elemento aparece na lista
    para depois verificar quais desses números é maior e, assim, achar a moda
    """
    elementos_ja_verificados = []
    posicao_elemento_da_suposta_moda = []
    qtd_elem_repetiu = []

    for elemento in lista:

        if elemento in elementos_ja_verificados:
            continue

        elementos_ja_verificados.append(elemento)
        posicao_elemento_da_suposta_moda.append(lista.index(elemento))

        cont = 0
        for elemento_comp in lista:
            if (elemento == elemento_comp):
                cont += 1

        qtd_elem_repetiu.append(cont)

    maior = qtd_elem_repetiu[0]
    moda = lista[posicao_elemento_da_suposta_moda[0]]

    for elemento in qtd_elem_repetiu:

        if elemento > maior:
            maior = elemento
            moda = lista[posicao_elemento_da_suposta_moda[qtd_elem_repetiu.index(elemento)]]

    return moda


def mediana(valores):
    """
    Encontra a mediana de 'valores', isto é, o valor que ocupa a posição
    central da lista ordenada. Quando a lista tem tamanho par,
    definimos a mediana como o valor da primeira posição na segunda
    metada da lista ordenada.

    Parâmetros: lista de floats.
    Retorna: a mediana de 'valores'.
    """

    valores.sort()

    if (len(valores) % 2 == 1):
        mediana = valores[int(((len(valores)+1) / 2) - 1)] 
    else:
        mediana = valores[int((len(valores) / 2))] 

    return mediana


def media(valores):
    """
    Encontra a média de 'valores'.

    Parâmetros: lista de floats.
    Retorna: a média de 'valores'.
    """

    soma = 0

    for valor in valores:
        soma += valor

    return soma/(len(valores))


def media_ponderada(valores, pesos):
    """
    Encontra a média ponderada de 'valores'.

    Parâmetros: listas de floats.
    Retorna: a média ponderada de 'valores'.
    """

    soma_media = 0
    soma_peso = 0

    for i in range(len(valores)):
        soma_media += valores[i]*pesos[i]
        soma_peso += pesos[i]

    return soma_media/soma_peso


def filtrar_entre(valores, menor, maior):
    """
    Cria uma lista com os números de 'valores' que estejam no intervalo
    ['menor', 'maior') (o primeiro intervalo é fechado e o segundo é aberto).

    Parâmetros: lista de floats e os limites.
    Retorna: a lista filtrada.
    """

    nova_lista = []

    for valor in valores:
        if (valor >= menor) and (valor < maior):
            nova_lista.append(valor)

    return nova_lista


def filtrar_caracteristica(lista, caracteristica, alvo):
    """
    Cria uma lista com os elementos de 'lista' cuja posição em 'caracteristica'
    seja igual a 'alvo'. Por exemplo, com a entrada abaixo, retornaríamos
    ['Alemanha', 'Portugal']:
    lista = ['Brasil', 'Alemanha', 'Angola', 'Portugal']
    caracteristica = ['América do Sul', 'Europa', 'África', 'Europa']
    alvo = 'Europa'

    Parâmetros: listas de números ou strings e um valor alvo.
    Retorna: a lista com a característica filtrada.
    """

    nova_lista = []

    for i in range(len(caracteristica)):

        if caracteristica[i] == alvo:
            nova_lista.append(lista[i])

    return nova_lista


def histograma(valores, intervalos):
    """
    Cria uma lista com as frequências do histograma de 'valores', divididas nas
    classes conforme a lista 'intervalos'. Por exemplo, se temos [10, 20, 30]
    como intervalos, devemos obter as frequências dos intervalos [10, 20) e [20,
    30).

    Parâmetros: listas de números.
    Retorna: lista de frequência do histograma.
    """

    histograma = []

    for i in range(len(intervalos)-1):

        histograma.append(0)

        menor = intervalos[i]
        maior = intervalos[i+1]

        for valor in valores:
            if (valor >= menor) and (valor < maior):
                histograma[i] += 1

    return histograma


def maiores_k(valores, k):
    """
    Cria uma lista com os 'k' maiores números de 'valores'.

    Parâmetros: lista de inteiros e um número inteiro.
    Retorna: lista com os 'k' maiores números.
    """

    nova_lista = []

    valores.sort(reverse = True)

    for i in range(k):
        nova_lista.append(valores[i])

    return nova_lista


def menores_k(valores, k):
    """
    Cria uma lista com os 'k' menores números de 'valores'.

    Parâmetros: lista de inteiros e um número inteiro.
    Retorna: lista com os 'k'menores números.
    """

    nova_lista = []

    valores.sort()

    for i in range(k):
        nova_lista.append(valores[i])

    return nova_lista


def remove_duplicatas(lista):
    """
    Cria uma lista removendo todos os elementos duplicados de 'lista', mantendo
    a ordem relativa original. Use somente listas, for/while e variáveis
    simples para implementar essa função.

    Parâmetros: listas de strings.
    Retorna: 'lista' sem duplicatas.
    """

    elementos_ja_verificados = []

    for elemento in lista:

        if elemento in elementos_ja_verificados:
            continue
        else:
            elementos_ja_verificados.append(elemento)

    return elementos_ja_verificados
