#Função da letra B do exercício
def letra_B():
    A = [5, 8, 3, 0, 15, 7, 20, 13, 30, 31]
    B = [valor for valor in A if(valor % A[0] == 0)]

    print(B)


#Funções da letra D do exercício
def eh_primo(numero):

    if(numero == 2):
        return True

    for i in range(2, (numero//2)+1):
        if (numero % i == 0):
            return False

    return True

def letra_D():

    a = [2, 8, 3, 11, 4, 5, 6, 7]
    b = [numero for numero in a if eh_primo(numero)]
    print(b)

