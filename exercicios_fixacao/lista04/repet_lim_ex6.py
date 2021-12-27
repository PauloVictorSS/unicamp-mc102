number = int(input())

raiz = number/2

for i in range(1,20):
    raiz = ((raiz ** 2) + number) / (2 * raiz)

print(raiz)