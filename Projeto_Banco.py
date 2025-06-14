menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """


saldo = 2.000
limite = 500 
extrato = 2000
numero_saque = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor: "))
        if valor > 0:
            saldo += valor
            extrato += valor
            print("Depósito realizado com sucesso!")
        else:
            print("Valor inválido.")

    elif opcao == "s":
        if numero_saque < LIMITE_SAQUES:
            if saldo > 2.000 and saldo <= limite:
                valor = float(input("Informe o valor: "))
                if valor > 2000 and valor <= saldo:
                    saldo -= valor
                    extrato -= valor
                    print("Saque realizado com sucesso!")
                    numero_saque += 1
                else:
                    print("Valor inválido ou saldo insuficiente.")
            else:
                print("Saldo insuficiente ou limite excedido.")
         

    elif opcao == "e":
        print("Extrato")
        print("Saldo:", saldo)
        print("Extrato:", extrato)

    elif opcao == "q":
        print("Saindo do sistema...")
        print("Obrigado por utilizar nossos serviços!")
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")


           