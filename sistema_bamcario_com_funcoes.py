def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > saldo:
        print("Saldo Insuficiente!")
    elif valor > limite:
        print("o valor excende o limite de saque!")
    elif numero_saques >= limite_saques:
        print(" numero maximo de saque atingido!")
    elif valor < 0:
        print("Valor Invalido")
    else:
        saldo -= valor
        extrato.append(f"Saque: -R$ {valor:.2f}")
        numero_saques += 1

        print("Saque reaLizado com sucesso!")
    return saldo, extrato, numero_saques


def depositar(saldo, valor, extrato):
    if valor < 0:
        print("Valor invalido para o deposito!")
    else:
        saldo += valor
        extrato.append(f"Deposito: +R$ {valor:.2f}")
        print("Deposito Realizado com Sucesso!")
    return saldo, extrato


def exibir_Extrato(saldo, *, extrato):
    print("==========EXTRATO==========")
    if not extrato:
        print("\nNenhuma Movimentacoes Resalizada")
    else:
        for mov in extrato:
            print(mov)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================")


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (Somente numeros): ")
    if any(usuario['cpf'] == cpf for usuario in usuarios):
        print("Usuario ja cadastrado!")
        return usuarios

    nome = input("Digite o Nome Completo: ")

    data_nasc = input("digite a sua data de  nascimento(dd/mm/aaaa): ")
    
    endereco = input("digite o endereco (lougradouro, numero-bairro-cidade/Estado): ")

    usuarios.append({'nome':nome, 'data_nac':data_nasc, 'cpf':cpf, 'endereco': endereco})

    print("\nUsuario Cadastrado com Sucesso!\n")
    return usuarios


def criar_conta(agencia, numero_conta, usuarios, contas):
    cpf = input("digite o CPF do usuario: ")
    usuario = next((usuario for usuario in usuarios if usuario['cpf'] == cpf),None)

    if usuario:
        contas.append({'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario})
        print("conta Criada com Sucesso")
    
    else:
        print("\nusuario nao encontrado! Cadestre o usuario Primeiro\n")

    return contas


def listar_contas(contas):
    for conta in contas:
        linha = f"Agencia: {conta["agencia"]} | Conta: {conta['numero_conta']} | Titular: {conta['usuario']['nome']}"
        print(linha)


def menu():
    opcao = input("""
==========MENU==========
[1] Depositar
[2] Sacar
[3] Extrato
[4] Nova Conta
[5] Listar Usuario
[6] Novo usuario
[0] Sair
ESCOLHA O OPCAP=> """)
    return opcao


def main():
    saldo = 0
    limite = 500
    extrato = []
    numero_saques = 0
    limite_saques = 3
    usuarios = []
    contas = []
    AGENCIA = "0001"

    while True:
        opcao = menu()

        if opcao == "1":
            valor = float(input("\nDigite o valor do Deposito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "2":
            valor = float(input("Digitr o valor sacar: "))

            saldo, extrato, numero_saques = sacar(
                                                saldo=saldo,
                                                valor=valor,
                                                extrato=extrato,
                                                limite=limite,
                                                numero_saques=numero_saques,
                                                limite_saques=limite_saques
                                                 )
        
        elif opcao == "3":
            exibir_Extrato(saldo, extrato=extrato)

        elif opcao =="4":
            numero_conta = len(contas) + 1
            contas = criar_conta(AGENCIA, numero_conta, usuarios, contas)

        elif opcao == "5":
            listar_contas(contas)

        elif opcao == "6":
            usuarios = criar_usuario(usuarios)

        elif opcao =="0":
            print("Saindo...")
            print("Obrigado por usar o Sistema!\n")
            break
        
        else:
            print("Opcoa invalida. Escolha siga o munu")

main()