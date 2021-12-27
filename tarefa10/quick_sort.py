def particionar(lista, inicio, fim):
    """
        Com base em um elemento pivo, coloca a esquerda dele
        todos os elementos menores que ele e a direita todos 
        os elementos maiores que ele. Retornando a real posição
        desse pivo
    """

    pivo = lista[inicio]
    i = inicio
    j = fim

    terminou = False

    while not terminou:
        
        while j > inicio:

            if j == i:
                terminou = True
                break

            if lista[j] < pivo:
                lista[i] = lista[j]
                break

            j-=1

        while i < fim:

            if j == i:
                terminou = True
                break

            if lista[i] > pivo:
                lista[j] = lista[i]
                break

            i+=1
    
    lista[j] = pivo
    return j


def quick_sort(lista, inicio, fim):
    """
        Realiza o quick_sort para ordenar uma lista de
        forma recursiva
    """

    if inicio < fim:
        posicao_pivo = particionar(lista, inicio, fim)
        quick_sort(lista, inicio, posicao_pivo - 1)
        quick_sort(lista, posicao_pivo + 1, fim)


def main():

    lista = list(map(int, input().split()))

    quick_sort(lista, 0, len(lista)-1)

    print(' '.join(map(str, lista)))


main()
