# Sistema Bancário em Python

Este projeto é um sistema bancário simples implementado em Python, permitindo a realização de operações básicas como **depósitos**, **saques** e a consulta de **extrato**.

## Funcionalidades

- **Depósito**: Permite que o usuário realize depósitos em sua conta, atualizando o saldo.
- **Saque**: Possibilita que o usuário realize até 3 saques por dia, com um valor máximo de R$500,00 por saque. O sistema verifica se há saldo suficiente para cada operação.
- **Extrato**: Exibe o histórico de transações realizadas (depósitos e saques), além do saldo atual da conta.
- **Controle de Saques Diários**: Limita o número de saques por dia, garantindo que não sejam realizados mais do que 3 saques.
  
## Como usar

1. O sistema solicita o nome do titular da conta e um valor de depósito inicial.
2. Em seguida, um menu será exibido com as seguintes opções:
   - `1`: Realizar um depósito
   - `2`: Realizar um saque
   - `3`: Exibir o extrato
   - `4`: Sair do sistema
3. Ao selecionar a opção desejada, o usuário poderá interagir com o sistema conforme a operação escolhida.
4. O programa continuará em loop até que a opção "Sair" seja escolhida.

## Requisitos

- Python 3

