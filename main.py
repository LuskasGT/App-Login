import customtkinter
from PIL import Image, ImageTk

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

def mostrar_tela_inicial():
    esconder_todos_widgets()
    texto_bem_vindo.pack(padx=5, pady=20)
    frame_botoes.place(relx=0.5, rely=0.5, anchor="center")
    botao_fazer_login.pack(padx=5, pady=5)
    botao_criar_conta.pack(padx=5, pady=5)
    botao_esqueci_senha.pack(padx=5, pady=5)

def mostrar_formulario_login():
    esconder_todos_widgets()
    botao_voltar.place(x=10, y=10)
    frame_login.place(relx=0.5, rely=0.5, anchor="center")
    texto_login.pack(padx=5, pady=5)
    texto_digite_email_login.pack(padx=5, pady=2.5)
    campo_email_login.pack(padx=5, pady=2.5)
    texto_digite_senha_login.pack(padx=5, pady=2.5)
    campo_senha_login.pack(padx=5, pady=2.5)
    botao_entrar.pack(padx=5, pady=5)

def mostrar_formulario_criacao_conta():
    esconder_todos_widgets()
    botao_voltar.place(x=10, y=10)
    frame_criacao_conta.place(relx=0.5, rely=0.5, anchor="center")
    texto_criar_conta.pack(padx=5, pady=5)
    texto_digite_email_criar.pack(padx=5, pady=2.5)
    campo_email_criar.pack(padx=5, pady=2.5)
    texto_digite_email_novamente.pack(padx=5, pady=2.5)
    campo_email_novamente_criar.pack(padx=5, pady=2.5)
    texto_digite_senha_criar.pack(padx=5, pady=2.5)
    campo_senha_criar.pack(padx=5, pady=2.5)
    texto_digite_senha_novamente_criar.pack(padx=5, pady=2.5)
    campo_senha_novamente_criar.pack(padx=5, pady=2.5)
    botao_criar_conta_final.pack(padx=5, pady=5)

def mostrar_formulario_esqueci_senha():
    esconder_todos_widgets()
    botao_voltar.place(x=10, y=10)
    frame_esqueci_senha.place(relx=0.5, rely=0.5, anchor="center")
    texto_esqueci_senha.pack(padx=5, pady=5)
    texto_digite_email_esqueci.pack(padx=5, pady=2.5)
    campo_email_esqueci.pack(padx=5, pady=2.5)
    botao_enviar.pack(padx=5, pady=5)

def esconder_todos_widgets():
    for widget in frame_direita.winfo_children():
        widget.pack_forget()
        widget.place_forget()
    frame_login.place_forget()
    frame_criacao_conta.place_forget()
    frame_esqueci_senha.place_forget()
    frame_botoes.place_forget()

janela = customtkinter.CTk()
janela.geometry("750x600")
janela.iconbitmap('GT.ico')
janela.title("Aplicativo GT")

background_image_path = "bg.jpg"
background_image = Image.open(background_image_path)
background_image = background_image.resize((900, 600), Image.ANTIALIAS)
background_photo = ImageTk.PhotoImage(background_image)

canvas = customtkinter.CTkCanvas(janela, width=900, height=400)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=background_photo, anchor="nw")

frame_esquerda = customtkinter.CTkFrame(janela)
frame_esquerda.place(x=0, y=0, relwidth=0.5, relheight=1)

frame_direita = customtkinter.CTkFrame(janela)
frame_direita.place(x=0.5, y=0, relwidth=0.5, relheight=1)

botao_voltar = customtkinter.CTkButton(frame_direita, text="Voltar", corner_radius=28, width=70, command=mostrar_tela_inicial)

texto_bem_vindo = customtkinter.CTkLabel(frame_direita, text="Bem-vindo! Escolha uma opção:", font=("Helvetica", 19, "bold"))

frame_botoes = customtkinter.CTkFrame(frame_direita, fg_color="transparent")

botao_fazer_login = customtkinter.CTkButton(frame_botoes, text="Fazer Login", corner_radius=28, command=mostrar_formulario_login)

botao_criar_conta = customtkinter.CTkButton(frame_botoes, text="Criar Nova Conta", corner_radius=28, command=mostrar_formulario_criacao_conta)

botao_esqueci_senha = customtkinter.CTkButton(frame_botoes, text="Esqueci a Senha", corner_radius=28, command=mostrar_formulario_esqueci_senha)

frame_login = customtkinter.CTkFrame(frame_direita, fg_color="transparent")
texto_login = customtkinter.CTkLabel(frame_login, text="Fazer Login", font=("Helvetica", 19, "bold"))
texto_digite_email_login = customtkinter.CTkLabel(frame_login, text="Digite seu email")
campo_email_login = customtkinter.CTkEntry(frame_login, placeholder_text="Seu email", width=200)
texto_digite_senha_login = customtkinter.CTkLabel(frame_login, text="Digite sua senha")
campo_senha_login = customtkinter.CTkEntry(frame_login, placeholder_text="Sua senha", show="*", width=200)
botao_entrar = customtkinter.CTkButton(frame_login, text="Entrar", corner_radius=28, command=lambda: print("Login"))

frame_criacao_conta = customtkinter.CTkFrame(frame_direita, fg_color="transparent")
texto_criar_conta = customtkinter.CTkLabel(frame_criacao_conta, text="Criar Nova Conta", font=("Helvetica", 19, "bold"))
texto_digite_email_criar = customtkinter.CTkLabel(frame_criacao_conta, text="Digite seu email")
campo_email_criar = customtkinter.CTkEntry(frame_criacao_conta, placeholder_text="Digite seu email", width=200)
texto_digite_email_novamente = customtkinter.CTkLabel(frame_criacao_conta, text="Digite seu email novamente")
campo_email_novamente_criar = customtkinter.CTkEntry(frame_criacao_conta, placeholder_text="Digite seu email novamente", width=200)
texto_digite_senha_criar = customtkinter.CTkLabel(frame_criacao_conta, text="Digite sua senha")
campo_senha_criar = customtkinter.CTkEntry(frame_criacao_conta, placeholder_text="Sua senha", show="*", width=200)
texto_digite_senha_novamente_criar = customtkinter.CTkLabel(frame_criacao_conta, text="Digite sua senha novamente")
campo_senha_novamente_criar = customtkinter.CTkEntry(frame_criacao_conta, placeholder_text="Sua senha novamente", show="*", width=200)
botao_criar_conta_final = customtkinter.CTkButton(frame_criacao_conta, text="Criar Conta", corner_radius=28, command=lambda: print("Criar Conta"))

frame_esqueci_senha = customtkinter.CTkFrame(frame_direita, fg_color="transparent")
texto_esqueci_senha = customtkinter.CTkLabel(frame_esqueci_senha, text="Esqueci a Senha", font=("Helvetica", 19, "bold"))
texto_digite_email_esqueci = customtkinter.CTkLabel(frame_esqueci_senha, text="Digite seu email")
campo_email_esqueci = customtkinter.CTkEntry(frame_esqueci_senha, placeholder_text="Seu email", width=200)
botao_enviar = customtkinter.CTkButton(frame_esqueci_senha, text="Enviar", corner_radius=28, command=lambda: print("Enviar"))

mostrar_tela_inicial()
janela.mainloop()

