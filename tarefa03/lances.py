comando = input()

codigo_produto, lance_minimo = input().split()
lance_minimo = float(lance_minimo)

maior_lance = -1
maior_lance_nome = ""
cont_lances = 0

print(f"Bem-vindo ao Leilão de Algoritmópolis! Produto {codigo_produto} com lance mínimo R$ {lance_minimo:.2f}")

while comando != "F":
    comando = input()

    if(comando == "L"):
        nome, lance = input().split()
        lance = float(lance)

        if(lance >= lance_minimo and lance > maior_lance):
            print(f"{nome} deu um lance de R$ {lance:.2f}")
            maior_lance = lance
            maior_lance_nome = nome
            cont_lances += 1
        else:
            print(f"Lance inválido de {nome}")

    elif(comando == "S"):
        print(f"Status do Leilão do Produto {codigo_produto}")

        if(cont_lances > 0):
            print(f"{cont_lances} lances até agora")
            print(f"{maior_lance_nome} deu o melhor lance, de valor R$ {maior_lance:.2f}")
        else:
            print("Não houve lances")

print(f"Leilão finalizado com {cont_lances} lances")

if(cont_lances > 0):
    print(f"{maior_lance_nome} venceu com o lance de valor R$ {maior_lance:.2f}")
else:
    print("Não houve vencedor")
