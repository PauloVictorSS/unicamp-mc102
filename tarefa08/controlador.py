"""
Arquivo para alterar algumas informações importantes e
controlar o fluxo do sistema, ligando a interface com o
modelo
"""

import contas as modulo_contas


def iniciar_contas_e_movimentacoes():

    contas = modulo_contas.inicializar_contas()
    movimentacoes = modulo_contas.inicializar_movimentacoes()

    return contas, movimentacoes


def abrir_conta(contas, numero_conta):

    if modulo_contas.criar(contas, numero_conta):
        return True
    return False


def realizar_movimentacao(contas, numero_conta, valor, data, descricao, movimentacoes):

    numero_conta = int(numero_conta)
    valor = float(valor)
    data = tuple(data.split("/"))

    resultado = modulo_contas.movimentar(contas, numero_conta, data, valor, descricao, movimentacoes)

    return resultado


def consultar_saldo(contas, numero_conta):

    numero_conta = int(numero_conta)
    resultado = modulo_contas.consultar_saldo(contas, numero_conta)

    return resultado


def emitir_extrato(contas, numero_conta, movimentacoes, data_inicial):

    numero_conta = int(numero_conta)
    data_inicial = tuple(data_inicial.split("/"))

    resultado = modulo_contas.emitir_extrato(contas, numero_conta, movimentacoes, data_inicial)

    return resultado


def fechar_conta(contas, numero_conta):

    numero_conta = int(numero_conta)
    resultado = modulo_contas.fechar_conta(contas, numero_conta)

    return resultado
