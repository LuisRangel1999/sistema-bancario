saldo = 1000
while True:
    opcao = int(input("1 - Ver saldo\n2 - Depositar\n3 - Sacar\n4 - Sair\n"))
    if opcao == 1:
        print(f"Seu saldo é: R${saldo:.2f}\n")

    elif opcao == 2:
        deposito = float(input("Quanto deseja depositar?\n"))
        if deposito < 0:
                print("Depósito inválido")
        else:
            saldo += deposito
            print(f"Seu saldo é: {saldo:.2f}\n")

    elif opcao == 3:
        sacar = float(input(f"Quanto deseja sacar?\n"))
        if sacar > saldo:
            print("Saldo insuficiente")
        else:
            saldo -= sacar
        print(f"Seu saldo é: {saldo:.2f}\n")
    elif opcao == 4:
        print("Sistema encerrado")
        break
    else:
        print("Opção inválida")