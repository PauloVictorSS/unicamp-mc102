def trios_formados(pares_moleculas):
    """
        Recebe um diocnário que representa diversas
        ligações entre os elementos e retorna os trios
        formados por elementos que ligam-se entre si
    """

    trios_formados = []

    # Para cada chave no dicionário 'pares_moleculas', pegamos os
    # elementos que se ligam nessa chave
    for key1 in pares_moleculas:
        elementos_ligados_1 = pares_moleculas[str(key1)]

        # Para cada elemento desses elementos ligados, verificamos quais
        # são os elementos que se ligam a eles e vemos se eles também se
        # ligam no key1
        for key2 in elementos_ligados_1:
            if str(key2) in pares_moleculas:
                elementos_ligados_2 = pares_moleculas[str(key2)]

                for elemento_comparar in elementos_ligados_2:
                    if (elemento_comparar in elementos_ligados_1):

                        trio = [int(key1), key2, elemento_comparar]
                        trio.sort()

                        trios_formados.append(trio)

    return trios_formados


def transforma_dicionario(lista_pares_moleculas):
    """
        Recebe uma lista de pares de moleculas e coloca em um formato de 
        dicionário, onde a chave representa o primeiro elemento do par e 
        o valor é uma lista com todos os elementos que esse elemento se liga
    """

    pares_moleculas = {}

    for par in lista_pares_moleculas:
        par.sort()
        elemento_1 = par[0]
        elemento_2 = par[1]

        if str(elemento_1) in pares_moleculas:
            elementos_ja_conectados = pares_moleculas[str(elemento_1)]
            elementos_ja_conectados.append(elemento_2)

            pares_moleculas[str(elemento_1)] = elementos_ja_conectados
        else:
            pares_moleculas[str(elemento_1)] = [elemento_2]

    return pares_moleculas


def main():

    numero_pares_moleculas = int(input())

    # Colocando todos os pares em uma lista
    lista_pares_moleculas = []
    for _ in range(numero_pares_moleculas):
        par = list(map(int, input().split()))
        par.sort()

        lista_pares_moleculas.append(par)
    lista_pares_moleculas.sort()

    # Chamando a função para formatar em um formato de dicionário
    pares_moleculas = transforma_dicionario(lista_pares_moleculas)

    # Chamando a função para achar os trios formados
    lista_trios_formados = trios_formados(pares_moleculas)

    for trio in lista_trios_formados:
        for elemento in trio:
            print(elemento, end=" ")
        print()


main()
