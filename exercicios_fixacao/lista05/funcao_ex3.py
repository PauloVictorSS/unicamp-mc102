lista_numeros = [1,2,3,4,5,6,7,8,9,10,11,12]
lista_meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

def mes_correspodente(n):

    assert n in lista_numeros, "O número deve ser natural entre 1 e 12"

    mes = lista_meses[lista_numeros.index(n)]
    return mes