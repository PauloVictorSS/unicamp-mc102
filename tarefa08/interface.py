import controlador as mod_control


erros = [
    "Esta conta não existe",
    "Saldo insuficiente",
    "Movimentação tem data retroativa",
    "A conta não pode ser fechada",
]

def verifica_erro(codigo):

    return erros[codigo]


def main():

    contas, movimentacoes = mod_control.iniciar_contas_e_movimentacoes()

    comando = input("")

    while comando != 'sair':

        if(comando == 'abrir'):
            numero_conta = int(input())

            resultado = mod_control.abrir_conta(contas, numero_conta)

            if resultado:
                print("Conta aberta com sucesso")
            else:
                print("Número de conta já existe")

        elif(comando == 'depositar' or comando == 'sacar'):
            numero_conta, valor, data, descricao = input().split(maxsplit=3)

            if comando == 'sacar':
                valor = -float(valor)

            resultado = mod_control.realizar_movimentacao(contas, numero_conta, valor, data, descricao, movimentacoes)

            if type(resultado) == int:
                print(verifica_erro(resultado))
            elif resultado and comando == 'depositar':
                print("Depósito realizado com sucesso")
            elif comando == 'sacar':
                print("Saque realizado com sucesso")

        elif(comando == 'saldo'):
            numero_conta = input()

            resultado = mod_control.consultar_saldo(contas, numero_conta)

            if type(resultado) == bool:
                print(verifica_erro(0))
            else:
                print(f"O saldo da conta é R$ {resultado:.2f}")

        elif(comando == 'extrato'):
            numero_conta, data_inicial = input().split()

            resultado = mod_control.emitir_extrato(contas, numero_conta, movimentacoes, data_inicial)

            if type(resultado) == bool:
                print(verifica_erro(0))
            else:
                for movimento in resultado:

                    tipo_movimento = movimento[1]
                    valor = movimento[2]
                    saldo_apos = movimento[3]
                    descricao = movimento[4]

                    data = movimento[5]
                    dia = data[0]
                    mes = data[1]
                    ano = data[2]

                    if tipo_movimento == "Saque":
                        valor = -valor

                    print(f"{tipo_movimento} de valor R$ {valor:.2f} realizado em {dia}/{mes}/{ano}")
                    print(f"Descrição adicional: {descricao}")
                    print(f"Saldo após movimentação: R$ {saldo_apos:.2f}")

        elif(comando == 'fechar'):
            numero_conta = input()

            resultado = mod_control.fechar_conta(contas, numero_conta)

            if type(resultado) == bool:
                print("Conta fechada com sucesso")
            else:
                print(verifica_erro(resultado))

        comando = input("")


main()
