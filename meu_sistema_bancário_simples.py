menu = """
SELECIONE A OPERAÇÃO DESEJADA:

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"\033[32mDepósito: R$ {valor: .2f}\n\033[0m"

        else:
            print(
                "Operação Inválida!\nValor inválido, lembre-se de informar um valor positivo.")

    elif opcao == "s":
        valor = float(input("Informe  valor do saque: "))

        if valor > saldo:
            print(f"Operação negada por saldo insuficiente!\nSeu saldo atual é: R$ {
                  saldo: .2f} ")

        elif valor > limite:
            print(
                f"Operação negada por exceder o limite!\nLembre-se: você tem um limite de R$ {limite: .2f}")

        elif numero_saques >= LIMITE_SAQUES:
            print("Operação negada por exceder o limite de saques diários!\nLembre-se: você tem um limite de 3 saques diários.")

        elif valor > 0:
            saldo -= valor
            extrato += f"\033[31mSaque: R$ {valor:.2f}\n\033[0m"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n\033[1m================ EXTRATO ================\033[0m")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("\033[1m==========================================\033[0m")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
