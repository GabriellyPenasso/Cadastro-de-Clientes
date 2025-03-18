import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

# Função de Login
class Login:
    def _init_(self, root):
        self.root = root
        self.root.title("Login")

        # Campos de entrada para o login
        self.label_email = tk.Label(self.root, text="Email:")
        self.label_email.pack(pady=5)
        self.entry_email = tk.Entry(self.root)
        self.entry_email.pack(pady=5)

        self.label_senha = tk.Label(self.root, text="Senha:")
        self.label_senha.pack(pady=5)
        self.entry_senha = tk.Entry(self.root, show="*")
        self.entry_senha.pack(pady=5)

        # Botão para realizar login
        self.botao_login = tk.Button(self.root, text="Login", command=self.realizar_login, width=15, height=2)
        self.botao_login.pack(pady=10)

    def realizar_login(self):
        email = self.entry_email.get()
        senha = self.entry_senha.get()

        # Verifica as credenciais
        if email == "gabrielly" and senha == "123Mudar":
            self.root.destroy()  # Fecha a janela de login
            abrir_janela_produtos()  # Abre a janela de produtos
        else:
            messagebox.showerror("Erro", "Email ou senha incorretos!")


def abrir_janela_produtos():
    root_produtos = tk.Tk()
    root_produtos.title("Produtos")

    canvas = tk.Canvas(root_produtos, width=900, height=600)
    canvas.pack()

    canvas.create_rectangle(400, 50, 20, 200)
    canvas.create_rectangle(400, 250, 20, 400)
    canvas.create_rectangle(400, 453, 20, 600)
    canvas.create_rectangle(450, 50, 840, 200)
    canvas.create_rectangle(450, 250, 840, 400)

    frame1 = tk.Frame(root_produtos)
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

    frame2 = tk.Frame(root_produtos)
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

    frame3 = tk.Frame(root_produtos)
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

    frame4 = tk.Frame(root_produtos)
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

    frame5 = tk.Frame(root_produtos)
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

    botao_comprar = tk.Button(root_produtos, text="Finalizar Compra", command=lambda: abrir_janela_carrinho(), width=15, height=1, font=("Arial", 12), bg="#CCCCCC", fg="#000000", relief="ridge", borderwidth=2)
    botao_comprar.place(x=600, y=500)

    def atualizar_quantidade(label, valor):
        quantidade = int(label.cget("text"))
        quantidade += valor
        if quantidade < 0:
            quantidade = 0
        label.config(text=str(quantidade))

    def abrir_janela_carrinho():
        janela_carrinho = tk.Toplevel(root_produtos)
        janela_carrinho.title("Carrinho de Compras")

        # Crie a tabela para mostrar os produtos
        tabela_produtos = ttk.Treeview(janela_carrinho)
        tabela_produtos["columns"] = ("Produto", "Quantidade", "Valor Unitário", "Valor Total")
        tabela_produtos.column("#0", width=0, stretch=tk.NO)
        tabela_produtos.column("Produto", anchor=tk.W, width=200)
        tabela_produtos.column("Quantidade", anchor=tk.W, width=100)
        tabela_produtos.column("Valor Unitário", anchor=tk.W, width=100)
        tabela_produtos.column("Valor Total", anchor=tk.W, width=100)
        tabela_produtos.heading("#0", text="", anchor=tk.W)
        tabela_produtos.heading("Produto", text="Produto", anchor=tk.W)
        tabela_produtos.heading("Quantidade", text="Quantidade", anchor=tk.W)
        tabela_produtos.heading("Valor Unitário", text="Valor Unitário", anchor=tk.W)
        tabela_produtos.heading("Valor Total", text="Valor Total", anchor=tk.W)

        tabela_produtos.pack()

        # Adicionar itens na tabela
        produtos = [
            ("Canetas BIC", quantidade1.cget("text"), "R$ 19,99", float(quantidade1.cget("text")) * 19.99),
            ("Mochila Kipling", quantidade2.cget("text"), "R$ 999,99", float(quantidade2.cget("text")) * 999.99),
            ("Caderno Tilibra", quantidade3.cget("text"), "R$ 39,99", float(quantidade3.cget("text")) * 39.99),
            ("Estojo Kipling", quantidade4.cget("text"), "R$ 99,99", float(quantidade4.cget("text")) * 99.99),
            ("Kit de Lapis", quantidade5.cget("text"), "R$ 249,99", float(quantidade5.cget("text")) * 249.99)
        ]

        for produto in produtos:
            tabela_produtos.insert("", tk.END, values=(produto[0], produto[1], produto[2], f"R$ {produto[3]:.2f}"))

        # Exibir valor total da compra
        valor_total = sum([float(quantidade1.cget("text")) * 19.99, float(quantidade2.cget("text")) * 999.99,
                           float(quantidade3.cget("text")) * 39.99, float(quantidade4.cget("text")) * 99.99,
                           float(quantidade5.cget("text")) * 249.99])

        label_total = tk.Label(janela_carrinho, text=f"Total: R$ {valor_total:.2f}", font=("Arial", 14))
        label_total.pack(pady=10)

    root_produtos.mainloop()

# Inicia a janela de login
root_login = tk.Tk()
login = Login(root_login)
root_login.mainloop()
