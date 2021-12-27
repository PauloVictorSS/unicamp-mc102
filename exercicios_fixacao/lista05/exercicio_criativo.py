def numero_palavras(texto):

    lista_palavras = texto.split()
    contador = 0

    for palavra in lista_palavras:

        if eh_plural(palavra)
            contador += 1

    return contador


def eh_plural(palavra):

     ultima_letra = palavra[len(palavra) - 1]

        if(ultima_letra == "s"):
            return True
        
        return False