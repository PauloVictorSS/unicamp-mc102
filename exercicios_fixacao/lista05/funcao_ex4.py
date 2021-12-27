

def numeros_romanos(n):

    assert n <= 50 and n > 0, "O número deve ser intero e positivo, menor que 50"

    unidades_em_romano = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

    unidade = unidades_em_romano[n%10]
        
    fator = n // 10

    if fator < 4:
        dezena = ""

        for i in range(fator):
            dezena += "X"
    elif fator == 4:
        dezena = "XL"
    else:
        return "L"

    return dezena + unidade


print(numeros_romanos(int(input())))
