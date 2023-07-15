# menu = """

# [1] Depositar
# [2] Sacar
# [3] Extrato
# [4] Sair

# => """

saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    print("\n[1] Depositar")
    print("[2] Sacar")
    print("[3] Extrato")
    print("[4] Sair")

    opcao = input("\nQual operação deseja realizar? Digite o número correspondente: ")

    if opcao == "1":
        valor_deposito = float(input("\nDigite o valor a ser depositado: "))
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato.append(("Depósito", valor_deposito))
            
            print("\n================================================")
            print(f"\nDepósito de R${valor_deposito:.2f} realizado com sucesso!")
            print("\n================================================")
        else:
            
            print("\n================================================")
            print("Valor inválido. O valor do depósito deve ser maior que zero.")
            print("\n================================================")

    elif opcao == "2":
        if numero_saques < LIMITE_SAQUES:
            
            valor_saque = float(input("\nDigite o valor a ser sacado: "))
            
            if valor_saque > 0 and valor_saque <= saldo and valor_saque <= limite:
                
                saldo -= valor_saque
                extrato.append(("Saque", valor_saque))
                
                numero_saques += 1
                ("\n================================================")
                print(f"Saque de R${valor_saque:.2f} realizado com sucesso!")
                ("\n================================================")
                
            elif valor_saque <= 0:
                print("\nValor inválido. O valor do saque deve ser maior que zero.")
                
            elif valor_saque > saldo:
                print("\nSaldo insuficiente para realizar o saque.")
                
            elif valor_saque > limite:
                print("\nO valor do saque excede o limite diário.")
                
        else:
            print("\nLimite máximo de saques diários atingido.")

    elif opcao == "3":
        print("\n================== Extrato ===================")
        for operacao, valor in extrato:
            print(f"{operacao}: R${valor:.2f}")
        print(f"Saldo atual: R${saldo:.2f}")
        print("\n================================================")

    elif opcao == "4":
        print("\n================================================")
        print("\nSaindo...")
        ("\n================================================")
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")