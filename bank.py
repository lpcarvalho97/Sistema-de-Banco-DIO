
saldo = 0
deposito = 0
quantidade_saque = 0
valor_saque_dia = 0
tela_login = -1
opcao = -1
lista_saques = list()
lista_debitos = list()
i = 0
j = 0
cadastro_cliente = {}
cadastros_cpf = set() #conjunto para armazenar os CPFs já cadastrados
cadastro_cliente = set()
numero_conta = set()
dados_conta = {}
numero_agencia = '0001'
numero_conta = 0
contador_conta = 0
senha_da_conta = set()




def depositar(conta_logada):
    global i

    deposito = float(input("Quanto deseja depositar? "))
    if deposito > 0:
        
        conta_logada['saldo'] += deposito
        print(f"Seu saldo atual é de {conta_logada['saldo']}")

        i = i + 1
        conta_logada['lista_debitos'].append(f"{i}º depósito no valor de: R$ {deposito: .2f}")

    else:
        print("Não é possível depositar valores inferiores a 'R$ 00,00'. Favor informe um valor maior que 'R$ 00,00'")


def sacar(conta_logada):
    global j

    saque = float(input("Informe quanto deseja sacar: "))
    if conta_logada['quantidade_saque'] < 3:
        if saque <= conta_logada['saldo']:
            if saque <= 500:
                print("Saque realizado com sucesso!")
                conta_logada['saldo'] -= saque
                conta_logada['quantidade_saque'] += 1
                conta_logada['valor_saque_dia'] += saque

                print(f"Total dos saques de hoje {conta_logada['valor_saque_dia']}.\n Quantidade de saques realizados hoje: {quantidade_saque}.\n Saldo restante: {conta_logada['saldo']}\n")
                j = j + 1
                conta_logada['lista_saques'].append(f"{j}º saque no valor de: R$ {saque: .2f}")

            else:
                print("O saque não poderá ultrapassar R$ 500,00")
                
        else:
            print(f"O valor do saque não pode ser superior ao valor do saldo! O seu saldo atualmente é {conta_logada['saldo']}")
    else:
        print("Limite diário de quantidade de saques (3) ultrapassado!")
        

def ver_extrato(conta_logada):

    if not conta_logada['lista_debitos'] and not conta_logada['lista_saques']:
        print("Não foram realizadas movimentações na sua conta.\n")

    if conta_logada['lista_debitos']:
        print("Débitos:")
        print(conta_logada['lista_debitos'])
        print(f"O saldo atual da conta é R${conta_logada['saldo']: .2f}")

    if conta_logada['lista_saques']:
        print("Saques")
        print(conta_logada['lista_saques'])
    
    print(f"O saldo atual da conta é R${conta_logada['saldo']: .2f}")


def cadastrar_cliente():
    global cadastro_cliente  # cria um dicionário vazio para armazenar os dados do cliente

    nome = input("Vamos fazer o cadastro! Digite o seu nome: ")
    cpf = input("Digite o CPF, apenas os números: ")

    #Verifica se o CPF já foi cadastrado
    if cpf in cadastros_cpf:
        print("CPF já cadastrado. Por favor, insira um CPF válido!")
        return None

    if not cpf.isdigit():
        print("O CPF deve conter apenas números!")
        return None
    
    email = input("Digite o seu e-mail: ")
    telefone = input("Digite o seu telefone: ")

    endereco_cliente = {}
    endereco_cliente['logradouro'] = input("Digite o nome da sua rua: ")
    endereco_cliente['numero'] = input("Digite o número de rua da sua residência: ")
    endereco_cliente['complemento'] = input("Digite o complemento: ")
    endereco_cliente['bairro'] = input("Digite o bairro: ")
    endereco_cliente['cidade'] = input("Digite a cidade: ")
    endereco_cliente['estado'] = input("Digite a sigla do seu estado: ")

    #adiciona o CPF ao conjunto de CPFs cadastrados
    cadastros_cpf.add(cpf)

    cadastro_cliente = {
        'nome': nome,
        'cpf': cpf,
        'email': email,
        'telefone': telefone,
        'endereco_cliente': endereco_cliente
    }

    print("Cliente cadastrado com sucesso!")
    return cadastro_cliente




def criar_conta():
    global cadastro_cliente
    global numero_conta
    global contador_conta
    global cadastros_cpf
    global dados_conta
    global numero_agencia
    global senha_da_conta

    validar_cpf_cadastro = input("Informe o seu CPF (somente números): ")

    if validar_cpf_cadastro in cadastros_cpf:
        
        print("Você já está cadastrado no banco. Validando se você já tem uma conta...")

        if validar_cpf_cadastro in dados_conta:

            for conta in dados_conta[validar_cpf_cadastro]:
                print(f"Agência: {conta['numero_agencia']}, Conta: {conta['numero_conta']}")

            print("Vamos criar mais uma conta para você!")

        else:
            print("Você não possui nenhuma conta no banco.")
            dados_conta[validar_cpf_cadastro] = []
            print("Vamos criar sua primeira conta!")
            
        contador_conta += 1
        numero_conta_atual = numero_conta + contador_conta

        senha_da_conta = input("Informe a senha da sua nova conta: ")

        nova_conta = {
            'numero_agencia': numero_agencia,
            'numero_conta': numero_conta_atual,
            'usuario': validar_cpf_cadastro,
            'senha': senha_da_conta,
            'saldo': 0,
            'quantidade_saque': 0,
            'valor_saque_dia': 0,
            'lista_saques': [],
            'lista_debitos': []
        }

        dados_conta[validar_cpf_cadastro].append(nova_conta)

        print(f"""
        Agência: {nova_conta['numero_agencia']}
        Conta: {nova_conta['numero_conta']}
        CPF: {nova_conta['usuario']}
        Senha:{nova_conta['senha']}
        """)

    else:
        print("Você ainda não tem cadastro no banco! É necessário cadastrar-se no banco antes de abrir uma conta!")



def logar():

    login = int(input("Informe o numero da sua conta: "))
    senha = input("Informe a sua senha: ")

    for cpf, contas in dados_conta.items():
        for conta in contas:
            if conta['numero_conta'] == login and conta['senha'] == senha:
                print("Login realizado com sucesso!")
                return conta

    print("Número da conta ou senha estão incorretos!")
    return None





    

while tela_login != 5:

    tela_login = float(input("""Escolha uma opção:
          1 - Para Logar na sua conta
          2 - Para Cadastrar-se no banco
          3 - Para Criar uma conta
          5 - Para sair do sistema."""))
    
    if tela_login == 1:

        conta_logada = logar()
        if conta_logada:
            opcao = -1


            while opcao != 5:
            
                opcao = int(input(""" Escolha uma opção:
                    1 - Para depositar
                    2 - Para sacar
                    3 - Para ver o Extrato
                    5 - Para sair da conta. /n
                    """))
            
                if opcao == 1:

                    depositar(conta_logada)        

                elif opcao == 2:                    
                        
                    sacar(conta_logada)

                elif opcao == 3:
                    ver_extrato(conta_logada)

                elif opcao == 5:
                    print("Saindo da conta...")

                        
                else:
                    print("Favor digitar um número válido!")

    elif tela_login == 2:
        cadastrar_cliente()

    elif tela_login == 3:

        criar_conta()

    elif tela_login == 5:
        print("Encerrando o sistema!")

    else:
        print("Escolha um número válido!")