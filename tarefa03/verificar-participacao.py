q = 3
v = 2
m = 120.45
a = "D"
b = "R"

nome = input("Qual o seu nome: ")
n_leilao_anterior = int(input("Quantos leilões já participou antes: "))
n_leilao_venceu = int(input("Quantos lances você já venceu: "))

if(n_leilao_venceu >= v):
    lance1 = float(input("Lance vencedor 1: "))
    lance2 = float(input("Lance vencedor 2: "))
    media_lance = (lance1 + lance2)/2
else:
    media_lance = -1

if (n_leilao_anterior >= q) or (nome[0] == a or nome[0] == b) or (media_lance >= m):
    print("Parabéns! Você pode se inscrever.")   
else:
    print("Infelizmente, você não poderá participar nesse ano.")
