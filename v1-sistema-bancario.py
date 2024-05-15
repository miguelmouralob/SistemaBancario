menu = """
------------------------
----------MENU----------
------------------------
[1] Depósito
[2] Saque
[3] Extrato
[0] Sair
------------------------
R:. """

saldo = 0
extrato = ""
qtd_saque = 0
qtd_max_saque = 3
limite_saque = 500

kp = -1

while kp != 0:
    opcao = int(input(menu))

    if opcao == 0:
        kp = 0
        break

    elif opcao == 1:
        deposito = float(input('Quanto em R$ deseja depositar: '))
        if deposito > 0:
            saldo += deposito
            extrato += f'Depósito: R$ {deposito:.2f}\n'
        else:
            print('Valor não aceito')

    elif opcao == 2:
        saque = float(input('Quanto em R$ deseja sacar: '))

        excedeu_saldo = saque > saldo
        excedeu_limite = saque > limite_saque
        excedeu_saques = qtd_saque >= qtd_max_saque

        if excedeu_saldo:
            print('Saldo Insuficiente! ')
            break
        elif excedeu_limite:
            print('Ultrapassa o valor máximo de saque! ')
        elif excedeu_saques:
            print('Quantidade máxima de saques diários atingida! ')
        elif saque > 0:
            saldo -= saque
            extrato += f'Saque: R$ {saque:.2f}\n'
            qtd_saque += 1
        else:
            print('Valor Inválido! ')

    elif opcao == 3:
        print('\n-----------EXTRATO-----------')
        print('Não houve movimentação.' if not extrato else extrato)
        print(f'O saldo é de R${saldo:.2f}')
        print('\n------------------------------')
    else:
        print('Digite uma opção válida')
