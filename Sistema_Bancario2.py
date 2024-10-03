# Inicialização dos dados da conta
titular = input("Qual o nome do titular da conta? \n")
saldo = round(float(input("Qual valor do seu depósito inicial? ")), 2)
historico = []  # Para armazenar todas as operações
saques_diarios = 0  # Contador para saques no dia

# Função para realizar depósito
def deposito(valor):
    global saldo
    if valor > 0:
        saldo += valor
        historico.append(f"Depósito: R$ {valor:.2f}")
        print(f"Depósito realizado com sucesso! Saldo atual: R$ {saldo:.2f}")
    else:
        print("Valor de depósito inválido!")

# Função para realizar saque
def saque(valor):
    global saldo, saques_diarios
    if saques_diarios >= 3:
        print("Você já realizou 3 saques hoje. Tente novamente amanhã.")
    elif valor > 500:
        print("O valor máximo por saque é R$ 500,00.")
    elif valor > saldo:
        print("Saldo insuficiente para realizar o saque.")
    else:
        saldo -= valor
        saques_diarios += 1
        historico.append(f"Saque: R$ {valor:.2f}")
        print(f"Saque de R$ {valor:.2f} realizado com sucesso! Saldo atual: R$ {saldo:.2f}")

# Função para exibir o extrato
def extrato():
    print(f"\nExtrato da conta de {titular}:")
    for operacao in historico:
        print(operacao)
    print(f"Saldo atual: R$ {saldo:.2f}\n")

# Menu de operações
while True:
    operacao = int(input('''
    -----------------------------------------------------
    Qual operação deseja realizar?
                    
          1- Depósito
          2- Saque
          3- Extrato
          4- Sair
    -----------------------------------------------------
    '''))

    if operacao == 1:
        # Depósito
        valor_deposito = round(float(input("Qual valor do depósito? ")), 2)
        deposito(valor_deposito)

    elif operacao == 2:
        # Saque
        valor_saque = round(float(input("Qual valor do saque? ")), 2)
        saque(valor_saque)

    elif operacao == 3:
        # Extrato
        extrato()

    elif operacao == 4:
        print("Saindo do sistema. Obrigado!")
        break

    else:
        print("Operação inválida. Tente novamente.")
