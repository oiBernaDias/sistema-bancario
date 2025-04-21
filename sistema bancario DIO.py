menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Ajuda
[0] Sair

=> """

ajuda = """

[1] Problemas com deposito
[2] Problemas com saque
[3] Problemas em nosso aplicativo
[4] Falar com um atendente
[0] Sair

=> """


saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "3":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "4":
           escolha = input(ajuda)
           
           if escolha == "1":
                print("\n Para ajuda com depósito entre em contato através do nosso número 0800...'.")
           
           elif escolha == "2":
                print("\n Em caso de problemas com saque vá até a agência mais próxima e fale com um de nossos atendentes .")

           elif escolha == "3":
               print("\n Caso esteja com algum bug ou erro relacionado ao nosso aplicativo, aguarde ou ligue para nosso 0800 para informar o erro..")

           elif escolha == "4":
               print("\n Um de nossos atendentes entrará em contato em instantes. Aguarde...")
               break
           
           elif escolha == "5":
               print("\n✅ Obrigado por entrar em contato. Tenha um ótimo dia!")
               break
           
           else:
               print("\n⚠️ Opção inválida. Tente novamente.")
     
    elif opcao == "0":
        print("\n✅ Obrigado pela preferencia. Tenha um ótimo dia!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
