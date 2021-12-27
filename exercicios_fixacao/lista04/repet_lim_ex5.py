rebar_size = int(input("Entre com o tamanho do vergalhão: "))
max_volume = int(input("Entre com o volume máximo da caixa: "))

total_possibilities = []

max_edge = rebar_size//4

x = 0
y = 0
z = 0

for x in range(1, max_edge):
    possibilitie = []
    
    if (x + y + z) == (max_edge):
        if ((x * y * z) <= max_volume):
            possibilitie.append(x)
            possibilitie.append(y)
            possibilitie.append(z)

            total_possibilities.append(possibilitie)

    for y in range(1, max_edge):
        possibilitie = []

        if (x + y + z) == (max_edge):
            if ((x * y * z) <= max_volume):
                possibilitie.append(x)
                possibilitie.append(y)
                possibilitie.append(z)

                total_possibilities.append(possibilitie)

        for z in range(1, max_edge):
            possibilitie = []

            if (x + y + z) == (max_edge):
                if ((x * y * z) <= max_volume):
                    possibilitie.append(x)
                    possibilitie.append(y)
                    possibilitie.append(z)

                    total_possibilities.append(possibilitie)

print(total_possibilities)