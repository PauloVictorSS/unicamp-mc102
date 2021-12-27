number_list = list(map(int, input().split()))

cont_list = []

#Coloca a quantidade de vezes que cada número apareceu em uma lista chamada "cont_list"
for i in range(1,10):
    cont = 0

    for number in number_list:
        if number == i:
            cont += 1
    
    cont_list.append(cont)

qtd_bigger = cont_list[0]

#Verifica qual a maior quantidade de vezes que certo número apareceu
for qtd_number in cont_list:
    if qtd_number > qtd_bigger:
        qtd_bigger = qtd_number


print("\n+-------------------+")

#Cria o histograma com base na quantidade de vezes que cada número aparece
while qtd_bigger > 0:

    print("|", end=" ")

    for cont_number in cont_list:
        
        if cont_number >= qtd_bigger:
            print("*", end=" ")
        else: 
            print(" ", end=" ")

    qtd_bigger -= 1
    print("|")

print("+-------------------+")
print("  1 2 3 4 5 6 7 8 9  ")
