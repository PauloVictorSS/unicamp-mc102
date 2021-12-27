def le_arquivo():

    numeros = []

    with open("numeros_inteiros.txt") as arquivo:

        for linha in arquivo:
            numeros.append(int(linha))

    return numeros


def ordena_lista(lista):

    for i in lista:
        for j in range(len(lista)-1):
            valor = lista[j]
            valor_comp = lista[j+1]

            if (valor > valor_comp):
                lista[j+1] = valor
                lista[j] = valor_comp


def escreve_arquivo(lista):

    with open("numeros_inteiros_ordenados.txt", "w") as arquivo:
        for numero in lista:
            arquivo.write(f"{numero}\n")


def main():

    lista = le_arquivo()
    ordena_lista(lista)
    escreve_arquivo(lista)


main()
