def verifica_eh_k_quase_palindromo(k, palavra, palavra_inversa, posicao_atual):
    """
        Recebe uma palavra e a sua inversa e compara os caracteres de
        mesma posição verificando se ela é 'k' quase palindromo
    """

    if k < 0:
        return "nao"
    elif posicao_atual < 0:
        return "sim"

    if palavra[posicao_atual] != palavra_inversa[posicao_atual]:
        k -= 1
    
    return verifica_eh_k_quase_palindromo(k, palavra, palavra_inversa, posicao_atual - 1)


def main():

    k = int(input())
    palavra = input()

    palavra_inversa = ""

    for i in range(len(palavra)-1, -1, -1):
        palavra_inversa += palavra[i]

    resultado = verifica_eh_k_quase_palindromo(k, palavra, palavra_inversa, len(palavra)-1)

    print(resultado)


main()
