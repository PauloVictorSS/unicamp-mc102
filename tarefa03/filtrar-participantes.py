n, q, v, m, a, b = input().split()
    
n = int(n)
q = int(q)
v = int(v)
m = float(m)

cont_1 = 0
aprovados = []

while cont_1 < n:
    nome, q_user, v_user = input().split()

    q_user = int(q_user)
    v_user = int(v_user)

    cont_2 = 0
    media = -1
    soma = 0

    while cont_2 < v_user:
        soma += float(input())
        media = soma/v_user
        cont_2 += 1
        

    if (nome[0] == a or nome[0] == b) or (q_user >= q) or (v_user >= v and media >= m):
        aprovados.append(nome)
    
    cont_1 += 1

for a in aprovados:
    print(a)