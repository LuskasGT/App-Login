import customtkinter

customtkinter.set_appearance_mode("dark")  
customtkinter.set_default_color_theme("dark-blue")  

# Função para mostrar a tela inicial
def mostrar_tela_inicial():
    esconder_todos_widgets()
    texto_bem_vindo.pack(padx=5, pady=5)
    botao_fazer_login.pack(padx=5, pady=5)
    botao_criar_conta.pack(padx=5, pady=5)
    botao_esqueci_senha.pack(padx=5, pady=5)

# Função para mostrar o formulário de login
def mostrar_formulario_login():
    esconder_todos_widgets()
    botao_voltar.place(x=10, y=10)  # Posiciona o botão de voltar no canto superior esquerdo
    texto_login.pack(padx=5, pady=5)
    texto_digite_email.pack(padx=5, pady=2.5)
    campo_email_login.pack(padx=5, pady=2.5)
    texto_digite_senha.pack(padx=5, pady=2.5)
    campo_senha_login.pack(padx=5, pady=2.5)
    botao_entrar.pack(padx=5, pady=5)

# Função para mostrar o formulário de criação de conta
def mostrar_formulario_criacao_conta():
    esconder_todos_widgets()
    botao_voltar.place(x=10, y=10)  # Posiciona o botão de voltar no canto superior esquerdo
    texto_criar_conta.pack(padx=5, pady=5)
    texto_digite_email.pack(padx=5, pady=2.5)
    campo_email_criar.pack(padx=5, pady=2.5)
    texto_digite_email_novamente.pack(padx=5, pady=2.5)
    campo_email_novamente_criar.pack(padx=5, pady=2.5)
    texto_digite_senha.pack(padx=5, pady=2.5)
    campo_senha_criar.pack(padx=5, pady=2.5)
    texto_digite_senha_novamente.pack(padx=5, pady=2.5)
    campo_senha_novamente_criar.pack(padx=5, pady=2.5)
    botao_criar_conta_final.pack(padx=5, pady=5)

# Função para mostrar o formulário de esqueci a senha
def mostrar_formulario_esqueci_senha():
    esconder_todos_widgets()
    botao_voltar.place(x=10, y=10)  # Posiciona o botão de voltar no canto superior esquerdo
    texto_esqueci_senha.pack(padx=5, pady=5)
    texto_digite_email.pack(padx=5, pady=2.5)
    campo_email_esqueci.pack(padx=5, pady=2.5)
    botao_enviar.pack(padx=5, pady=5)

# Função para esconder todos os widgets
def esconder_todos_widgets():
    for widget in janela.winfo_children():
        widget.pack_forget()
        widget.place_forget()

# Criação da janela principal
janela = customtkinter.CTk()
janela.geometry("900x400")
janela.iconbitmap('GT.ico')
janela.title("Aplicativo GT")

# Botão de voltar
botao_voltar = customtkinter.CTkButton(janela, text="Voltar", width=70, command=mostrar_tela_inicial)  # Botão menor

# Rótulo de texto de boas-vindas
texto_bem_vindo = customtkinter.CTkLabel(janela, text="Bem-vindo! Escolha uma opção:")

# Botão para fazer login
botao_fazer_login = customtkinter.CTkButton(janela, text="Fazer Login", command=mostrar_formulario_login)

# Botão para criar uma conta
botao_criar_conta = customtkinter.CTkButton(janela, text="Criar Nova Conta", command=mostrar_formulario_criacao_conta)

# Botão para esqueci a senha
botao_esqueci_senha = customtkinter.CTkButton(janela, text="Esqueci a Senha", command=mostrar_formulario_esqueci_senha)

# Widgets do formulário de login
texto_login = customtkinter.CTkLabel(janela, text="Fazer Login", font=("Helvetica", 19, "bold"))
texto_digite_email = customtkinter.CTkLabel(janela, text="Digite seu email")
campo_email_login = customtkinter.CTkEntry(janela, placeholder_text="Seu email")
texto_digite_senha = customtkinter.CTkLabel(janela, text="Digite sua senha")
campo_senha_login = customtkinter.CTkEntry(janela, placeholder_text="Sua senha", show="*")
botao_entrar = customtkinter.CTkButton(janela, text="Entrar", command=lambda: print("Login"))

# Widgets do formulário de criação de conta
texto_criar_conta = customtkinter.CTkLabel(janela, text="Criar Nova Conta", font=("Helvetica", 19, "bold"))
campo_email_criar = customtkinter.CTkEntry(janela, placeholder_text="Digite seu email")
texto_digite_email_novamente = customtkinter.CTkLabel(janela, text="Digite seu email novamente")
campo_email_novamente_criar = customtkinter.CTkEntry(janela, placeholder_text="Digite seu email novamente")
texto_digite_senha = customtkinter.CTkLabel(janela, text="Digite sua senha")
campo_senha_criar = customtkinter.CTkEntry(janela, placeholder_text="Digite sua senha", show="*")
texto_digite_senha_novamente = customtkinter.CTkLabel(janela, text="Digite sua senha novamente")
campo_senha_novamente_criar = customtkinter.CTkEntry(janela, placeholder_text="Digite sua senha novamente", show="*")
botao_criar_conta_final = customtkinter.CTkButton(janela, text="Criar Conta", command=lambda: print("Criar conta"))

# Widgets do formulário de esqueci a senha
texto_esqueci_senha = customtkinter.CTkLabel(janela, text="Esqueci a Senha", font=("Helvetica", 19, "bold"))
campo_email_esqueci = customtkinter.CTkEntry(janela, placeholder_text="Digite seu email")
botao_enviar = customtkinter.CTkButton(janela, text="Enviar", command=lambda: print("Enviar"))

# Mostra a tela inicial ao iniciar o programa
mostrar_tela_inicial()

# Execução da janela principal
janela.mainloop()
