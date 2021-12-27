def inicializar_contas():
    """
    Devolve um objeto representando o conjunto
    de contas bancárias inicialmente vazio.
    """

    return {}


def inicializar_movimentacoes():
    """
    Devolve um objeto representando o conjunto
    de movimentações inicialmente vazio.
    """

    return []


def verificar_data_mais_recente(data_1, data_2):
    """
    Recebe duas datas e retorna True se a primeira é
    mais nova do que a outra, caso contrário, retorna
    False
    """

    ano_data_1 = int(data_1[2])
    mes_data_1 = int(data_1[1])
    dia_data_1 = int(data_1[0])

    ano_data_2 = int(data_2[2])
    mes_data_2 = int(data_2[1])
    dia_data_2 = int(data_2[0])

    if ano_data_1 == ano_data_2:
        if mes_data_1 == mes_data_2:
            if dia_data_1 < dia_data_2:
                return False
                
            return True
        elif mes_data_1 < mes_data_2:
            return False

        return True
    elif ano_data_1 < ano_data_2:
        return False

    return True


def criar(contas, numero_conta):
    """
    Cria uma nova conta identificada por 'numero_conta' com
    saldo 0 e nenhuma movimentação associada.

    Devolve:
        - True se a conta tenha sido criada com sucesso
         -False se já existir conta com esse numero
    """

    if numero_conta in contas:
        return False
    else:
        contas[numero_conta] = 0
        return True


def consultar_saldo(contas, numero_conta):
    """
    Devolve o saldo da conta identificada por 'numero_conta'.
    """

    if numero_conta in contas:
        saldo = contas[numero_conta]
        return saldo
    else:
        return False


def movimentacoes_da_conta(numero_conta, movimentacoes):
    """
    Recebe uma lista de movimentações e um numero de conta
    e retorna todas as movimentações da conta recebida
    """

    minhas_movimentacoes = []

    for movimento in movimentacoes:
        if(numero_conta == movimento[0]):
            minhas_movimentacoes.append(movimento)

    return minhas_movimentacoes


def fechar_conta(contas, numero_conta):

    if numero_conta in contas:
        saldo = consultar_saldo(contas, numero_conta)
        if saldo == 0:
            contas.pop(numero_conta, False)
            return True
        
    return 3


def movimentar(contas, numero_conta, data, valor, descricao, movimentacoes):
    """
    Realiza uma movimentação na conta 'numero_conta'
    de valor 'valor' no dia 'data' descrita por 'descricao'
    e guarda esse histórico na lista 'movimentacoes'

    Devolve:
        - True se for possível realizar a movimentação
        - False caso contrário.
    """

    if numero_conta in contas:
        saldo_original = consultar_saldo(contas, numero_conta)

        if (saldo_original + valor) < 0:
            return 1

        #Recebe as movimentaçõs da conta com o <numero_conta>
        minhas_movimentacoes = movimentacoes_da_conta(numero_conta, movimentacoes)

        #Verifica se a conta em questão fez alguma outra movimentação para ver se
        #ela é retrograda ou não
        if len(minhas_movimentacoes) > 0:
            ultima_movimentacao = minhas_movimentacoes[len(minhas_movimentacoes) - 1]
            data_ultima_movimentacao = ultima_movimentacao[5]

            if (verificar_data_mais_recente(data_ultima_movimentacao, data)):
                return 2

        #Seta todos os valores que vão ser guardados na movimentação em questão
        if(valor > 0):
            movimento = "Depósito"
        else:
            movimento = "Saque"

        contas[numero_conta] += valor
        saldo_apos = contas[numero_conta]

        movimentacao = (numero_conta, movimento, valor, saldo_apos, descricao, data)
        movimentacoes.append(movimentacao)

        return True

    else:
        return 0


def emitir_extrato(contas, numero_conta, movimentacoes, data_inicial):
    """
    Retorna todas as movimentações de <movimentacoes> feitas pela conta 
    com o <numero_conta> a partir da <data_inicial>
    """


    historico_movimentacoes = []

    if numero_conta in contas:
        minhas_movimentacoes = movimentacoes_da_conta(numero_conta, movimentacoes)

        inicial = -1

        #Verifica a partir de qual data o extrato vai ser emitido
        for i, movimentacao in enumerate(minhas_movimentacoes):

            data_movimentacao = movimentacao[5]

            #Verifica qual data é mais recente, a data da emissão do extrato ou a data
            #da movimentação em questão
            if verificar_data_mais_recente(data_inicial, data_movimentacao):
                continue

            inicial = i
            break

        #Verifica se há alguma movimentação após a data pedida, se sim, guarda todas essas
        #movimentações para retornar depois
        if(inicial >= 0):
            historico_movimentacoes = minhas_movimentacoes[inicial:]

        return historico_movimentacoes

    else:
        return 0
