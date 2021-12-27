def calcula_sequencia_pedrinho(numero, valores_ja_calculados):

    """
        Recebe um número e uma lista de valores já calculados para
        calcular a sequencia do Pedrinho, retornando o valor da sequência
        com base no 'numero'
    """

    if numero <= 3:
        return numero

    if numero in valores_ja_calculados:
        return valores_ja_calculados[numero]
    else:
        p_N1 = calcula_sequencia_pedrinho(numero - 1, valores_ja_calculados)
        p_N2 = 2 * calcula_sequencia_pedrinho(numero - 2, valores_ja_calculados)
        p_N3 = 3 * calcula_sequencia_pedrinho(numero - 3, valores_ja_calculados)

        resultado = p_N1 + p_N2 + p_N3
        valores_ja_calculados[numero] = resultado

        return resultado


def main():
    numero = int(input())

    valores_ja_calculados = {}

    numero_Pn = calcula_sequencia_pedrinho(numero, valores_ja_calculados)

    print(numero_Pn)


main()
