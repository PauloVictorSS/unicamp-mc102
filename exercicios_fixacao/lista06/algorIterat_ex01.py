def print_impares(m, n):

    for i in range(1, m+1):

        maior_elemento_linha = 2*n*i

        lista = [number for number in range((maior_elemento_linha - 2*n)+1, maior_elemento_linha, 2)]

        if i % 2 == 0:
            lista.sort(reverse=True)

        for numero in lista:
            if(numero < 10):
                print("0", end="")
            print(f"{numero}", end="  ")

        print()


def main():

    m, n = input().split()
    print()
    print_impares(int(m), int(n))


main()
