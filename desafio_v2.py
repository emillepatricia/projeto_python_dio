
def criar_usuario(usuarios):
    cpf = input("Informe o CPF do usuário (somente números): ")
    if len(cpf) != 11 or not cpf.isdigit():
        print("CPF inválido.")
        return None

    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            print("Usuário já cadastrado.")
            return None

    nome = input("Informe o nome completo do usuário: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")

    usuario = {
        "cpf": cpf,
        "nome": nome,
        "data_nascimento": data_nascimento,
        "contas": []
    }

    usuarios.append(usuario)

    return usuario


def criar_conta(usuario, proxima_conta):
    agencia = "0001"
    conta = {
        "agencia": agencia,
        "numero": proxima_conta,
        "saldo": 0,
        "extrato": [],
        "numero_saques": 0
    }

    usuario["contas"].append(conta)

    return conta


def deposito(conta, valor):
    if valor > 0:
        conta["saldo"] += valor
        conta["extrato"].append(f"Depósito: R$ {valor:.2f}")
    else:
        print("Operação falhou! O valor informado é inválido.")


def saque(conta, valor, limite, limite_saques):
    excedeu_saldo = valor > conta["saldo"]
    excedeu_limite = valor > limite
    excedeu_saques = conta["numero_saques"] >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        conta["saldo"] -= valor
        conta["extrato"].append(f"Saque: R$ {valor:.2f}")
        conta["numero_saques"] += 1
    else:
        print("Operação falhou! O valor informado é inválido.")


def extrato(conta):
    print("\n================ EXTRATO ================")
    if not conta["extrato"]:
        print("Não foram realizadas movimentações.")
    else:
        for movimento in conta["extrato"]:
            print(movimento)
    print(f"\nSaldo: R$ {conta['saldo']:.2f}")
    print("==========================================")


def listar_contas(usuarios):
    if not usuarios:
        print("Nenhum usuário cadastrado.")
        return

    print("\n================ LISTA DE CONTAS ================")
    print("Agência   |   C/C   |   Titular")
    print("-----------------------------------------------")

    for usuario in usuarios:
        cpf = usuario["cpf"]
        nome = usuario["nome"]
        for conta in usuario["contas"]:
            agencia = conta["agencia"]
            numero = conta["numero"]
            print(f"{agencia:<9} | {numero:<7} | {nome}")

    print("==================================================")


usuarios = []
proxima_conta = 1
limite = 500
limite_saques = 3

while True:
    opcao = input(
        """
    [c] Criar usuário
    [a] Criar conta
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [l] Listar contas
    [q] Sair

    => """
    )

    if opcao == "c":
        usuario = criar_usuario(usuarios)
        if usuario:
            print("Usuário criado com sucesso!")
    elif opcao == "a":
        cpf = input("Informe o CPF do usuário vinculado à conta (somente números): ")
        for usuario in usuarios:
            if usuario["cpf"] == cpf:
                conta = criar_conta(usuario, proxima_conta)
                proxima_conta += 1
                print("Conta criada com sucesso!")
                break
        else:
            print("Usuário não encontrado. Não é possível criar conta.")
    elif opcao == "d":
        agencia = input("Informe o número da agência: ")
        numero = int(input("Informe o número da conta: "))
        valor = float(input("Informe o valor do depósito: "))
        for usuario in usuarios:
            for conta in usuario["contas"]:
                if conta["agencia"] == agencia and conta["numero"] == numero:
                    deposito(conta, valor)
                    print("Depósito realizado com sucesso!")
                    break
            else:
                continue
            break
        else:
            print("Conta não encontrada. Não é possível realizar depósito.")
    elif opcao == "s":
        agencia = input("Informe o número da agência: ")
        numero = int(input("Informe o número da conta: "))
        valor = float(input("Informe o valor do saque: "))
        for usuario in usuarios:
            for conta in usuario["contas"]:
                if conta["agencia"] == agencia and conta["numero"] == numero:
                    saque(conta, valor, limite, limite_saques)
                    print("Saque realizado com sucesso!")
                    break
            else:
                continue
            break
        else:
            print("Conta não encontrada. Não é possível realizar saque.")
    elif opcao == "e":
        agencia = input("Informe o número da agência: ")
        numero = int(input("Informe o número da conta: "))
        for usuario in usuarios:
            for conta in usuario["contas"]:
                if conta["agencia"] == agencia and conta["numero"] == numero:
                    extrato(conta)
                    break
            else:
                continue
            break
        else:
            print("Conta não encontrada. Não é possível exibir extrato.")
    elif opcao == "l":
        listar_contas(usuarios)
    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
