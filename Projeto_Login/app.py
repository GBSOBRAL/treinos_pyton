import customtkinter as ctk

#Criação das funcionalidades
def validar_login():
    usuario = campo_usuario.get()
    senha = campo_senha.get()
    
    if usuario == "Gustavo" and senha == "123":
        resultado_login.configure(text="Login feito com sucesso!",
                                  text_color="green")
    else:
        resultado_login.configure(text="Credenciais incorretas!",
                                  text_color="red")

#Criação da aparencia
ctk.set_appearance_mode("dark")

#Criação da Janela principal
app = ctk.CTk()
app.title("Sistema de Login")
app.geometry("300x300")

#Criação dos campos
#login
label_usuario = ctk.CTkLabel(app, text="Usuário:")
label_usuario.pack(pady=10)

campo_usuario = ctk.CTkEntry(app, placeholder_text="Digite seu usuário")
campo_usuario.pack(pady=10)

#senha
label_senha = ctk.CTkLabel(app, text="Senha:")
label_senha.pack(pady=10)

campo_senha = ctk.CTkEntry(app, placeholder_text="Digite sua senha")
campo_senha.pack(pady=10)

#botão
botao_login = ctk.CTkButton(app, text="Login", command=validar_login)
botao_login.pack(pady=10)

#texto feedback
resultado_login = ctk.CTkLabel(app, text="")
resultado_login.pack(pady=10)

#Iniciar a aplicação
app.mainloop()