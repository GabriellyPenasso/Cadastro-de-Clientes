import tkinter as tk
from tkinter import ttk, messagebox
import json

class Cliente:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

class FormaDePagamento:
    def __init__(self, tipo):
        self.tipo = tipo

class ItemPedido:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def valor_total(self):
        return self.preco * self.quantidade

class Pedido:
    def __init__(self, cliente, forma_pagamento):
        self.cliente = cliente
        self.forma_pagamento = forma_pagamento
        self.itens = []
        self.subtotal = 0.0
        self.total = 0.0

    def adicionar_item(self, item):
        self.itens.append(item)
        self.subtotal += item.valor_total()

    def calcular_total(self):
        self.total = self.subtotal

    def salvar_pedido(self):
        pedido_dict = {
            "cliente": {"nome": self.cliente.nome, "email": self.cliente.email},
            "forma_pagamento": self.forma_pagamento.tipo,
            "itens": [{"nome": item.nome, "preco": item.preco, "quantidade": item.quantidade, "valor_total": item.valor_total()} for item in self.itens],
            "subtotal": self.subtotal,
            "total": self.total
        }
        with open("pedido.json", "w") as f:
            json.dump(pedido_dict, f, indent=4)

# Função de login
def verificar_login():
    email = entry_email.get()
    senha = entry_senha.get()
    
    # Verificando se o login está correto
    if email == "teste@gmail.com" and senha == "123Mudar":
        messagebox.showinfo("Sucesso", "Login bem-sucedido!")
        root_login.quit()  # Fecha a tela de login
        abrir_interface_principal()  # Abre a interface principal
    else:
        messagebox.showerror("Erro", "Email ou senha incorretos. Tente novamente.")

# Função para abrir a interface principal
def abrir_interface_principal():
    root = tk.Tk()
    root.title("Produtos")

    canvas = tk.Canvas(root, width=900, height=600)
    canvas.pack()

    canvas.create_rectangle(400, 50, 20, 200)
    canvas.create_rectangle(400, 250, 20, 400)
    canvas.create_rectangle(400, 453, 20, 600)
    canvas.create_rectangle(450, 50, 840, 200)
    canvas.create_rectangle(450, 250, 840, 400)

    # Produtos
    produtos = [
        ("Canetas BIC", 19.99, 0),
        ("Mochila Kipling", 999.99, 0),
        ("Caderno Tilibra", 39.99, 0),
        ("Estojo Kipling", 99.99, 0),
        ("Kit de Lapis", 249.99, 0)
    ]

    quantidade_labels = []
    for i, (produto, preco, _) in enumerate(produtos):
        frame = tk.Frame(root)
        frame.place(x=200 + (i % 2) * 450, y=73 + (i // 2) * 200, width=180, height=120)
        texto = tk.Label(frame, text=produto, font=("Arial", 16))
        texto.pack()
        preco_label = tk.Label(frame, text=f"Preço - R$ {preco:.2f}", font=("Arial", 14))
        preco_label.pack()

        frame_botao = tk.Frame(frame)
        frame_botao.pack(pady=(18, 0))
        botao_menos = tk.Button(frame_botao, text="-", command=lambda i=i: atualizar_quantidade(i, -1), width=3, height=1, font=("Arial", 12), bg="#CCCCCC", fg="#000000", relief="ridge", borderwidth=2)
        botao_menos.pack(side=tk.LEFT, padx=2)
        quantidade_label = tk.Label(frame_botao, text="0", font=("Arial", 12))
        quantidade_label.pack(side=tk.LEFT, padx=2)
        quantidade_labels.append(quantidade_label)
        botao_mais = tk.Button(frame_botao, text="+", command=lambda i=i: atualizar_quantidade(i, 1), width=3, height=1, font=("Arial", 12), bg="#CCCCCC", fg="#000000", relief="ridge", borderwidth=2)
        botao_mais.pack(side=tk.LEFT, padx=2)

    def atualizar_quantidade(i, valor):
        quantidade = int(quantidade_labels[i].cget("text"))
        quantidade += valor
        if quantidade < 0:
            quantidade = 0
        quantidade_labels[i].config(text=str(quantidade))

    def abrir_janela_carrinho():
        janela_carrinho = tk.Toplevel(root)
        janela_carrinho.title("Carrinho de Compras")

        tabela_produtos = ttk.Treeview(janela_carrinho)
        tabela_produtos["columns"] = ("Produto", "Quantidade", "Valor Unitário", "Valor Total")
        tabela_produtos.column("#0", width=0, stretch=tk.NO)
        tabela_produtos.column("Produto", anchor=tk.W, width=200)
        tabela_produtos.column("Quantidade", anchor=tk.W, width=100)
        tabela_produtos.column("Valor Unitário", anchor=tk.W, width=100)
        tabela_produtos.column("Valor Total", anchor=tk.W, width=100)
        tabela_produtos.grid(row=0, column=0, padx=10, pady=10)

        tabela_produtos.heading("#0", text="", anchor=tk.W)
        tabela_produtos.heading("Produto", text="Produto", anchor=tk.W)
        tabela_produtos.heading("Quantidade", text="Quantidade", anchor=tk.W)
        tabela_produtos.heading("Valor Unitário", text="Valor Unitário", anchor=tk.W)
        tabela_produtos.heading("Valor Total", text="Valor Total", anchor=tk.W)

        # Adicionar produtos no carrinho
        itens = [
            ("Canetas BIC", 19.99),
            ("Mochila Kipling", 999.99),
            ("Caderno Tilibra", 39.99),
            ("Estojo Kipling", 99.99),
            ("Kit de Lapis", 249.99)
        ]
        pedido = Pedido(Cliente("Cliente", "cliente@example.com"), FormaDePagamento("Cartão de Crédito"))

        for i, (produto, preco) in enumerate(itens):
            quantidade = int(quantidade_labels[i].cget("text"))
            if quantidade > 0:
                item = ItemPedido(produto, preco, quantidade)
                pedido.adicionar_item(item)
                tabela_produtos.insert("", "end", values=(produto, quantidade, f"R$ {preco:.2f}", f"R$ {item.valor_total():.2f}"))

        pedido.calcular_total()
        label_total = tk.Label(janela_carrinho, text=f"Total: R$ {pedido.total:.2f}", font=("Arial", 14))
        label_total.grid(row=1, column=0, pady=10)

        # Opções de pagamento
        label_pagamento = tk.Label(janela_carrinho, text="Escolha a forma de pagamento:", font=("Arial", 12))
        label_pagamento.grid(row=2, column=0, pady=10)

        opcoes_pagamento = ["Cartão de Crédito", "Boleto Bancário", "Pix"]
        combo_pagamento = ttk.Combobox(janela_carrinho, values=opcoes_pagamento, state="readonly", width=20, font=("Arial", 12))
        combo_pagamento.grid(row=3, column=0, pady=10)
        combo_pagamento.set(opcoes_pagamento[0])  # Definir a opção padrão

        def finalizar_compra():
            pagamento_selecionado = combo_pagamento.get()
            pedido.forma_pagamento = FormaDePagamento(pagamento_selecionado)
            pedido.salvar_pedido()
            messagebox.showinfo("Compra Finalizada", f"Compra finalizada com sucesso! Forma de pagamento: {pagamento_selecionado}")
            janela_carrinho.destroy()

        botao_finalizar = tk.Button(janela_carrinho, text="Finalizar Compra", command=finalizar_compra, font=("Arial", 12), bg="#4CAF50", fg="white")
        botao_finalizar.grid(row=4, column=0, pady=10)

        janela_carrinho.mainloop()

    botao_comprar = tk.Button(root, text="Finalizar Compra", command=abrir_janela_carrinho, width=15, height=1, font=("Arial", 12), bg="#CCCCCC", fg="#000000", relief="ridge", borderwidth=2)
    botao_comprar.place(x=600, y=500)

    root.mainloop()

# Tela de login
root_login = tk.Tk()
root_login.title("Login")

label_email = tk.Label(root_login, text="Email:", font=("Arial", 12))
label_email.pack(pady=10)
entry_email = tk.Entry(root_login, font=("Arial", 12))
entry_email.pack(pady=5)

label_senha = tk.Label(root_login, text="Senha:", font=("Arial", 12))
label_senha.pack(pady=10)
entry_senha = tk.Entry(root_login, show="*", font=("Arial", 12))
entry_senha.pack(pady=5)

botao_login = tk.Button(root_login, text="Login", command=verificar_login, font=("Arial", 12), bg="#4CAF50", fg="white")
botao_login.pack(pady=20)

root_login.mainloop()
