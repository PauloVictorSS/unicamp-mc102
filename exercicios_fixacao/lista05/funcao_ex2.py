def fatorial(n):

    fatorial = n
    cont = n - 1

    while cont >= 1:
        
        fatorial *= (cont)
        cont -= 1

    return fatorial

def main():

    for i in range(1, 21):

        print(f"{i}! = {fatorial(i)}")

main()