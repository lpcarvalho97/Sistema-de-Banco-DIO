
saldo = 0
deposito = 0
quantidade_saque = 0
valor_saque_dia = 0
opcao = -1
lista_saques = list()
lista_debitos = list()
i = 0
j = 0


def depositar():
    global saldo
    global lista_debitos
    global i

    deposito = float(input("Quanto deseja depositar? "))
    if deposito > 0:
        
        saldo = saldo + deposito
        print(f"Seu saldo atual é de {saldo}")

        i = i + 1
        lista_debitos.append(f"{i}º depósito no valor de: R$ {deposito: .2f}")

    else:
        print("Não é possível depositar valores inferiores a 'R$ 00,00'. Favor informe um valor maior que 'R$ 00,00'")


def sacar():
        
    global quantidade_saque
    global valor_saque_dia
    global saldo
    global lista_saques
    global j

    saque = float(input("Informe quanto deseja sacar: "))
    if quantidade_saque < 3:
        if saque <= saldo:
            if saque <= 500:
                print("Saque realizado com sucesso!")
                saldo = saldo - saque
                quantidade_saque += 1
                valor_saque_dia += saque
                print(f"Total dos saques de hoje {valor_saque_dia}.\n Quantidade de saques realizados hoje: {quantidade_saque}.\n Saldo restante: {saldo}\n")
                j = j + 1
                lista_saques.append(f"{j}º saque no valor de: R$ {saque: .2f}")

            else:
                print("O saque não poderá ultrapassar R$ 500,00")
                
        else:
            print(f"O valor do saque não pode ser superior ao valor do saldo! O seu saldo atualmente é {saldo}")
    else:
        print("Limite diário de quantidade de saques (3) ultrapassado!")
        

def ver_extrato():
    global saldo

    if i == 0 and j == 0:
        print("Não foram realizadas movimentações na sua conta.\n")
        print(f"O saldo atual da conta é R${saldo: .2f}")

    elif i == 0 and j > 0:
        print("Não foram realizados débitos na sua conta.\n")
        print(lista_saques)
        print(f"O saldo atual da conta é R${saldo: .2f}")

    elif i > 0 and j == 0:
        print(lista_debitos)
        print("Não foram realizados saques na sua conta.\n")
        print(f"O saldo atual da conta é R${saldo: .2f}")

    else:
        print(lista_debitos)
        print(lista_saques)
        print(f"O saldo atual da conta é R${saldo: .2f}")



    




while opcao != 5:
    
    opcao = int(input(""" Escolha uma opção:
          1 - Para depositar
          2 - Para sacar
          3 - Para ver o Extrato
          5 - Para sair.
           """))
    
    if opcao == 1:

        depositar()        

    elif opcao == 2:                    
       
        sacar()

    elif opcao == 3:
        ver_extrato()

    elif opcao == 5:
        print("Saindo do sistema...")
    
    else:
        print("Favor digitar um número válido!")