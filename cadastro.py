clientes = []  # Lista para armazenar os clientes

def cadastrar_cliente():
    """Função para cadastrar um cliente."""
    nome = input("Nome do cliente: ")  # Solicita o nome do cliente
    email = input("Email do cliente: ")  # Solicita o email do cliente
    telefone = input("Telefone do cliente: ")  # Solicita o telefone do cliente
    
    # Cria um dicionário com os dados do cliente
    cliente = {
        "nome": nome,
        "email": email,
        "telefone": telefone,
        "compras": []  # Lista para armazenar as compras do cliente
    }
    
    clientes.append(cliente)  # Adiciona o cliente à lista de clientes
    print("Cliente cadastrado com sucesso!\n")  # Confirmação do cadastro

def listar_clientes():
    """Função para listar os clientes cadastrados."""
    if not clientes:  # Verifica se a lista de clientes está vazia
        print("Nenhum cliente cadastrado ainda.\n")  # Exibe mensagem se não houver clientes
    else:
        print("Lista de Clientes:")  # Título da listagem
        for i, cliente in enumerate(clientes, 1):  # Percorre a lista numerando os clientes
            print(f"{i}. Nome: {cliente['nome']}, Email: {cliente['email']}, Telefone: {cliente['telefone']}")  # Exibe os dados do cliente
        print("\n")  # Adiciona uma linha em branco ao final

def cliente_fez_compra(email):
    """Função para verificar se um cliente já fez alguma compra."""
    for cliente in clientes:
        if cliente['email'] == email:  # Verifica se o email corresponde a um cliente
            if cliente['compras']:  # Verifica se a lista de compras não está vazia
                return True  # Cliente já fez compras
            else:
                return False  # Cliente ainda não fez compras
    return None  # Retorna None se o cliente não for encontrado

# Menu principal
enquanto = True  # Variável de controle para manter o loop rodando
while enquanto:
    print("1 - Cadastrar Cliente")  # Opção para cadastrar um cliente
    print("2 - Listar Clientes")  # Opção para listar clientes
    print("3 - Verificar se um cliente fez compras")  # Opção para verificar compras
    print("4 - Sair")  # Opção para sair do programa
    opcao = input("Escolha uma opção: ")  # Solicita uma escolha do usuário
    
    if opcao == "1":  # Se o usuário escolher 1, chama a função de cadastro
        cadastrar_cliente()
    elif opcao == "2":  # Se o usuário escolher 2, chama a função de listagem
        listar_clientes()
    elif opcao == "3":  # Se o usuário escolher 3, verifica se o cliente já fez compras
        email = input("Digite o email do cliente: ")
        resultado = cliente_fez_compra(email)
        if resultado is True:
            print("O cliente já fez compras.\n")
        elif resultado is False:
            print("O cliente ainda não fez compras.\n")
        else:
            print("Cliente não encontrado.\n")
    elif opcao == "4":  # Se o usuário escolher 4, encerra o loop
        print("Saindo...")  # Mensagem de saída
        enquanto = False  # Define a variável para encerrar o loop
    else:
        print("Opção inválida!\n")  # Mensagem de erro para entrada inválida
