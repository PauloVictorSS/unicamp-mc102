def calcula_fatorial(numero):
    """
        Calcula o fatorial de um número recursivamente
    """

    if numero == 0:
        return 1

    return numero * calcula_fatorial(numero - 1)


def main():

    numero = int(input())

    fatorial = calcula_fatorial(numero)

    print(fatorial)


main()
