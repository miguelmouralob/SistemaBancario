def menu():
    menu = """
    ========== MENU ==========
    ==========================
    [1] Depósito
    [2] Saque
    [3] Extrato
    [4] Nova Conta
    [5] Listar Contas
    [6] Novo Usuário
    [0] Sair
    
    >> """
    return int(input(menu))

def depositar(saldo, deposito, extrato, /):
    if deposito > 0:
        saldo += deposito
        extrato += f'Depósito:\t\tR$ {deposito:.2f}\n'
    else:
        print('Valor não aceito')
    
    return saldo, extrato

def sacar(*, saldo, saque, extrato, limite_saque, qtd_saque, qtd_max_saque):
    excedeu_limite = saque > limite_saque
    excedeu_saldo = saque > saldo
    excedeu_saques = qtd_saque >= qtd_max_saque

    if excedeu_saldo:
        print('Saldo Insuficiente! ')
    elif excedeu_limite:
        print('Ultrapassa o valor máximo de saque! ')
    elif excedeu_saques:
        print('Quantidade máxima de saques diários atingida! ')
    elif saque > 0:
        saldo -= saque
        extrato += f'Saque:\t\tR$ {saque:.2f}\n'
        qtd_saque += 1
        print(f'Saque de R${saque:.2f} realizado com sucesso')
    else:
        print('Valor Inválido! ')
    
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print('\n-----------EXTRATO-----------')
    print('Não houve movimentação.' if not extrato else extrato)
    print(f'O saldo é de R${saldo:.2f}')
    print('\n------------------------------')

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('Informe o CPF do usuário: ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('Conta criada com SUCESSO! ')
        return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}
    
    print('Usuário NÃO encontrado - Fluxo encerrado! ')

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
        Agência:\t{conta['agencia']}
        C/C:\t{conta['numero_conta']}
        Titular:\t{conta['usuario']['nome']}
        """
        print(linha)

def criar_usuario(usuarios):
    cpf = input('Informe o CPF (somente número): ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('Essse CPF já está cadastrado! ')
        return
    
    nome = input('Informe seu nome completo: ')
    data_nascimento = input('Informe a data de nascimento (dd-mm-aaaa): ')
    endereco = input('Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ')

    usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco})
    print('Usuário criado com sucesso! ')

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def main():
    qtd_max_saque = 3
    n_agencia = '0001'

    saldo = 0
    limite_saque = 500
    extrato = ""
    qtd_saque = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == 0:
            break

        elif opcao == 1:
            deposito = float(input('Quanto em R$ deseja depositar: '))

            saldo, extrato = depositar(saldo, deposito, extrato)

        elif opcao == 2:
            saque = float(input('Quanto em R$ deseja sacar: '))

            saldo, extrato = sacar(
                saldo = saldo,
                saque = saque,
                extrato = extrato,
                limite_saque = limite_saque,
                qtd_saque = qtd_saque,
                qtd_max_saque = qtd_max_saque,
            )

        elif opcao == 3:
            exibir_extrato(saldo, extrato = extrato)
        
        elif opcao == 4:
            numero_conta = len(contas) + 1
            
            conta = criar_conta(n_agencia, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == 5:
            listar_contas(contas)

        elif opcao == 6:
            criar_usuario(usuarios)

        else:
            print('Digite uma opção válida')

main()
