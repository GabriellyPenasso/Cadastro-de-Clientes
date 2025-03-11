import json  # Importa a biblioteca JSON para manipulação de arquivos JSON
import tkinter as tk # Importa sys para possíveis manipulações do sistema
from tkinter import messagebox, simpledialog

clientes = []  # Lista para armazenar os clientes
# Nome do arquivo onde os dados dos clientes serão armazenados
arquivo_dados = "clientes.json"

def salvar_dados():
    """Salva os dados dos clientes no arquivo JSON."""
    with open(arquivo_dados, "w") as arquivo:
        json.dump(clientes, arquivo, indent=4)  # Salva a lista de clientes em formato JSON, com indentação de 4 espaços

def carregar_dados():
    """Carrega os dados dos clientes do arquivo JSON."""
    global clientes # Permite modificar a variável global clientes
    try:
        with open(arquivo_dados, "r") as arquivo:
            clientes = json.load(arquivo) # Carrega os dados do arquivo JSON para a lista de clientes
    except (FileNotFoundError, json.JSONDecodeError):  # Se o arquivo não existir ou estiver corrompido
        clientes = []  # Inicializa a lista como vazia, drrr!

def cadastrar_cliente():
    """Função para cadastrar um cliente."""
    nome = simpledialog.askstring("Cadastro", "Nome do cliente:")
    email = simpledialog.askstring("Cadastro", "Email do cliente:")
    telefone = simpledialog.askstring("Cadastro", "Telefone do cliente:")
    
    if nome and email and telefone: # Verifica se os campos 'nome', 'email' e 'telefone' foram preenchidos#
        cliente = {
            "nome": nome,
            "email": email,
            "telefone": telefone,
            "compras": [],
            "carrinho": []
        }
        clientes.append(cliente)
        salvar_dados()
        messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")

def listar_clientes():
    """Função para listar os clientes cadastrados."""
    if not clientes: # Verifica se a lista de clientes está vazia
        messagebox.showinfo("Clientes", "Nenhum cliente cadastrado ainda.")
    else:
        lista = "\n".join([f"{i+1}. {c['nome']} - {c['email']} - {c['telefone']}" for i, c in enumerate(clientes)])  # Percorre a lista de clientes
        messagebox.showinfo("Lista de Clientes", lista)

def adicionar_ao_carrinho():
    #Função para adicionar um item ao carrinho do cliente.
    email = simpledialog.askstring("Carrinho", "Digite o email do cliente:")
    for cliente in clientes:
        if cliente['email'] == email: # Percorre a lista de clientes
            produto = simpledialog.askstring("Carrinho", "Nome do produto:")
            quantidade = simpledialog.askinteger("Carrinho", "Quantidade:")
            cliente['carrinho'].append({"produto": produto, "quantidade": quantidade}) # Adiciona o item ao carrinho
            salvar_dados()
            messagebox.showinfo("Sucesso", "Produto adicionado ao carrinho!")
            return
    messagebox.showerror("Erro", "Cliente não encontrado.") # Mensagem de erro se o cliente não for encontrado

def visualizar_carrinho():
    #Função para visualizar o carrinho do cliente.
    email = simpledialog.askstring("Carrinho", "Digite o email do cliente:")
    for cliente in clientes:
        if cliente['email'] == email:
            if not cliente['carrinho']:
                messagebox.showinfo("Carrinho", "O carrinho está vazio.")
                return
            lista = "\n".join([f"{item['produto']} - {item['quantidade']}" for item in cliente['carrinho']])
            messagebox.showinfo("Carrinho", lista)
            return
    messagebox.showerror("Erro", "Cliente não encontrado.")

def finalizar_compra():
    #Função para finalizar a compra do carrinho.
    email = simpledialog.askstring("Compra", "Digite o email do cliente:")
    for cliente in clientes:
        if cliente['email'] == email:
            if not cliente['carrinho']:
                messagebox.showinfo("Compra", "O carrinho está vazio.")
                return
            cliente['compras'].extend(cliente['carrinho'])
            cliente['carrinho'].clear()
            salvar_dados()
            messagebox.showinfo("Sucesso", "Compra finalizada com sucesso!")
            return
    messagebox.showerror("Erro", "Cliente não encontrado.")

def sair():
    #Fecha a aplicação.
    janela.quit()

# Interface gráfica
carregar_dados()
janela = tk.Tk()
janela.title("Sistema de Carrinho")
janela.geometry("300x300")

btn_cadastrar = tk.Button(janela, text="Cadastrar Cliente", command=cadastrar_cliente)
btn_listar = tk.Button(janela, text="Listar Clientes", command=listar_clientes)
btn_adicionar = tk.Button(janela, text="Adicionar ao Carrinho", command=adicionar_ao_carrinho)
btn_visualizar = tk.Button(janela, text="Visualizar Carrinho", command=visualizar_carrinho)
btn_finalizar = tk.Button(janela, text="Finalizar Compra", command=finalizar_compra)
btn_sair = tk.Button(janela, text="Sair", command=sair) 

btn_cadastrar.pack(pady=5)
btn_listar.pack(pady=5)
btn_adicionar.pack(pady=5)
btn_visualizar.pack(pady=5)
btn_finalizar.pack(pady=5)
btn_sair.pack(pady=5)

janela.mainloop()
