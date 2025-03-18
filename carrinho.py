import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

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

    frame1 = tk.Frame(root)
    frame1.place(x=200, y=73, width=180, height=120)
    texto1 = tk.Label(frame1, text="Canetas BIC", font=("Arial", 16))
    texto1.pack()
    preco1 = tk.Label(frame1, text="Preço - R$ 19,99", font=("Arial", 14))
    preco1.pack()

    frame1_botao = tk.Frame(frame1)
    frame1_botao.pack(pady=(18, 0))
    botao_menos1 = tk.Button(frame1_botao, text="-", command=lambda: atualizar_quantidade(quantidade1, -1), width=3, height=1, font=("Arial", 12), bg="#CCCCCC", fg="#000000", relief="ridge", borderwidth=2)
    botao_menos1.pack(side=tk.LEFT, padx=2)
    quantidade1 = tk.Label(frame1_botao, text="0", font=("Arial", 12))
    quantidade1.pack(side=tk.LEFT, padx=2)
    botao_mais1 = tk.Button(frame1_botao, text="+", command=lambda: atualizar_quantidade(quantidade1, 1), width=3, height=1, font=("Arial", 12), bg="#CCCCCC", fg="#000000", relief="ridge", borderwidth=2)
    botao_mais1.pack(side=tk.LEFT, padx=2)

    frame2 = tk.Frame(root)
    frame2.place(x=200, y=270, width=180, height=120)
    texto2 = tk.Label(frame2, text="Mochila Kipling", font=("Arial", 16))
    texto2.pack()
    preco2 = tk.Label(frame2, text="Preço - R$ 999,99", font=("Arial", 14))
    preco2.pack()

    frame2_botao = tk.Frame(frame2)
    frame2_botao.pack(pady=(18, 0))
    botao_menos2 = tk.Button(frame2_botao, text="-", command=lambda: atualizar_quantidade(quantidade2, -1), width=3, height=1, font=("Arial", 12), bg="#CCCCCC", fg="#000000", relief="ridge", borderwidth=2)
    botao_menos2.pack(side=tk.LEFT, padx=2)
    quantidade2 = tk.Label(frame2_botao, text="0", font=("Arial", 12))
    quantidade2.pack(side=tk.LEFT, padx=2)
    botao_mais2 = tk.Button(frame2_botao, text="+", command=lambda: atualizar_quantidade(quantidade2, 1), width=3, height=1, font=("Arial", 12), bg="#CCCCCC", fg="#000000", relief="ridge", borderwidth=2)
    botao_mais2.pack(side=tk.LEFT, padx=2)

    frame3 = tk.Frame(root)
    frame3.place(x=200, y=475, width=180, height=120)
    texto3 = tk.Label(frame3, text="Caderno Tilibra", font=("Arial", 16))
    texto3.pack()
    preco3 = tk.Label(frame3, text="Preço - R$ 39,99", font=("Arial", 14))
    preco3.pack()

    frame3_botao = tk.Frame(frame3)
    frame3_botao.pack(pady=(18, 0))
    botao_menos3 = tk.Button(frame3_botao, text="-", command=lambda: atualizar_quantidade(quantidade3, -1), width=3, height=1, font=("Arial", 12), bg="#CCCCCC", fg="#000000", relief="ridge", borderwidth=2)
    botao_menos3.pack(side=tk.LEFT, padx=2)
    quantidade3 = tk.Label(frame3_botao, text="0", font=("Arial", 12))
    quantidade3.pack(side=tk.LEFT, padx=2)
    botao_mais3 = tk.Button(frame3_botao, text="+", command=lambda: atualizar_quantidade(quantidade3, 1), width=3, height=1, font=("Arial", 12), bg="#CCCCCC", fg="#000000", relief="ridge", borderwidth=2)
    botao_mais3.pack(side=tk.LEFT, padx=2)

    frame4 = tk.Frame(root)
    frame4.place(x=650, y=73, width=180, height=120)  # Mudou de 420 para 650
    texto4 = tk.Label(frame4, text="Estojo Kipling", font=("Arial", 16))
    texto4.pack()
    preco4 = tk.Label(frame4, text="Preço - R$ 99,99", font=("Arial", 14))
    preco4.pack()

    frame4_botao = tk.Frame(frame4)
    frame4_botao.pack(pady=(18, 0))
    botao_menos4 = tk.Button(frame4_botao, text="-", command=lambda: atualizar_quantidade(quantidade4, -1), width=3, height=1, font=("Arial", 12), bg="#CCCCCC", fg="#000000", relief="ridge", borderwidth=2)
    botao_menos4.pack(side=tk.LEFT, padx=2)
    quantidade4 = tk.Label(frame4_botao, text="0", font=("Arial", 12))
    quantidade4.pack(side=tk.LEFT, padx=2)
    botao_mais4 = tk.Button(frame4_botao, text="+", command=lambda: atualizar_quantidade(quantidade4, 1), width=3, height=1, font=("Arial", 12), bg="#CCCCCC", fg="#000000", relief="ridge", borderwidth=2)
    botao_mais4.pack(side=tk.LEFT, padx=2)

    frame5 = tk.Frame(root)
    frame5.place(x=650, y=270, width=180, height=120)  # Mudou de 420 para 650
    texto5 = tk.Label(frame5, text="Kit de Lapis", font=("Arial", 16))
    texto5.pack()
    preco5 = tk.Label(frame5, text="Preço - R$ 249,99", font=("Arial", 14))
    preco5.pack()

    frame5_botao = tk.Frame(frame5)
    frame5_botao.pack(pady=(18, 0))
    botao_menos5 = tk.Button(frame5_botao, text="-", command=lambda: atualizar_quantidade(quantidade5, -1), width=3, height=1, font=("Arial", 12), bg="#CCCCCC", fg="#000000", relief="ridge", borderwidth=2)
    botao_menos5.pack(side=tk.LEFT, padx=2)
    quantidade5 = tk.Label(frame5_botao, text="0", font=("Arial", 12))
    quantidade5.pack(side=tk.LEFT, padx=2)
    botao_mais5 = tk.Button(frame5_botao, text="+", command=lambda: atualizar_quantidade(quantidade5, 1), width=3, height=1, font=("Arial", 12), bg="#CCCCCC", fg="#000000", relief="ridge", borderwidth=2)
    botao_mais5.pack(side=tk.LEFT, padx=2)

    botao_comprar = tk.Button(root, text="Finalizar Compra", command=lambda: abrir_janela_carrinho(), width=15, height=1, font=("Arial", 12), bg="#CCCCCC", fg="#000000", relief="ridge", borderwidth=2)
    botao_comprar.place(x=600, y=500)

    def atualizar_quantidade(label, valor):
        quantidade = int(label.cget("text"))
        quantidade += valor
        if quantidade < 0:
            quantidade = 0
        label.config(text=str(quantidade))

    def abrir_janela_carrinho():
        janela_carrinho = tk.Toplevel(root)
        janela_carrinho.title("Carrinho de Compras")

        # Crie a tabela para mostrar os produtos
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
        produtos = [
            ("Canetas BIC", quantidade1, 19.99),
            ("Mochila Kipling", quantidade2, 999.99),
            ("Caderno Tilibra", quantidade3, 39.99),
            ("Estojo Kipling", quantidade4, 99.99),
            ("Kit de Lapis", quantidade5, 249.99)
        ]

        for produto, label_quantidade, preco in produtos:
            quantidade = int(label_quantidade.cget("text"))
            if quantidade > 0:
                valor_total = preco * quantidade
                tabela_produtos.insert("", "end", values=(produto, quantidade, f"R$ {preco:.2f}", f"R$ {valor_total:.2f}"))

        # Calcular o total
        total = sum(int(label_quantidade.cget("text")) * preco for _, label_quantidade, preco in produtos)
        label_total = tk.Label(janela_carrinho, text=f"Total: R$ {total:.2f}", font=("Arial", 14))
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
            messagebox.showinfo("Compra Finalizada", f"Compra finalizada com sucesso! Forma de pagamento: {pagamento_selecionado}")
            janela_carrinho.destroy()

        botao_finalizar = tk.Button(janela_carrinho, text="Finalizar Compra", command=finalizar_compra, font=("Arial", 12), bg="#4CAF50", fg="white")
        botao_finalizar.grid(row=4, column=0, pady=10)

        janela_carrinho.mainloop()

    root.mainloop()

# Tela de login
root_login = tk.Tk()
root_login.title("Tela de Login")

# Tamanho da janela
root_login.geometry("400x300")

# Adicionando o campo de Email
label_email = tk.Label(root_login, text="Email:")
label_email.pack(pady=5)
entry_email = tk.Entry(root_login, font=("Arial", 14))
entry_email.pack(pady=5)

# Adicionando o campo de Senha
label_senha = tk.Label(root_login, text="Senha:")
label_senha.pack(pady=5)
entry_senha = tk.Entry(root_login, show="*", font=("Arial", 14))
entry_senha.pack(pady=5)

# Adicionando o botão de login
botao_login = tk.Button(root_login, text="Login", command=verificar_login, font=("Arial", 12), bg="#4CAF50", fg="white")
botao_login.pack(pady=20)

root_login.mainloop()
