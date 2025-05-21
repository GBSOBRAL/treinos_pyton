import openpyxl
import customtkinter as ctk
from cryptography.fernet import Fernet

secret_key = b'a0LGI7KuOdJ7EvmFYubDT2_Mc6QYW0vK8JezMTL4l6U='
fernet = Fernet(secret_key)

def encrypt_pw(pw):
     return fernet.encrypt(pw.encode()).decode()

def decrypt_pw(pw_encrypted):
     return fernet.decrypt(pw_encrypted.encode()).decode()

#Planilha
book = openpyxl.load_workbook("Dados.xlsx")
page = book["Dados"]

app = ctk.CTk()
app.title("Login")
app.geometry("300x400")

field_user_signin=""
field_pw_signin=""
    
def check_login():
    user = field_user.get()
    pw = field_pw.get()
    for row in page.iter_rows(min_row=2):
        user_check = row[0].value
        pw_check = decrypt_pw(row[1].value)
        if user_check == user and pw_check == pw:
             result_login.configure(text = "Login efetuado com sucesso")
             break
        else:
             result_login.configure(text = "Credenciais incorretas")

def send_signin():
        user_signin = field_user_signin.get()
        pw_signin = encrypt_pw(field_pw_signin.get())
        page.append([user_signin, pw_signin])
        
        book.save("Dados.xlsx")

def hide_pw():
    button_showpw.configure(text="Mostrar senha", command=show_pw)
    field_pw.configure(show="*")

def show_pw():
    button_showpw.configure(text="Esconder senha", command=hide_pw)
    field_pw.configure(show="")


#Janela de Cadastro       
def screen_signin():
    global field_user_signin, field_pw_signin
    
    win_signin = ctk.CTkToplevel(app)
    win_signin.geometry("300x320")
    win_signin.title("Signin")

    label_user_signin = ctk.CTkLabel(win_signin, text="Usuário:")
    label_user_signin.pack(pady=5)
    field_user_signin = ctk.CTkEntry(win_signin, placeholder_text="Digite seu usuário")
    field_user_signin.pack(pady=10)

    label_pw_signin = ctk.CTkLabel(win_signin, text="Senha:")
    label_pw_signin.pack(pady=5)
    field_pw_signin = ctk.CTkEntry(win_signin, placeholder_text="Digite sua senha")
    field_pw_signin.pack(pady=10)

    button_back = ctk.CTkButton(master=win_signin, text="Voltar", command=win_signin.destroy)
    button_back.pack(pady=10)

    button_send = ctk.CTkButton(master=win_signin, text="Enviar", command=send_signin)
    button_send.pack(pady=10)

    result_signin = ctk.CTkLabel(win_signin, text="")
    result_signin.pack(pady=10)

#Login
ctk.set_appearance_mode("dark")

label_user = ctk.CTkLabel(app, text="Usuário:")
label_user.pack(pady=5)
field_user = ctk.CTkEntry(app, placeholder_text="Digite seu usuário")
field_user.pack(pady=10)

label_pw = ctk.CTkLabel(app, text="Senha:")
label_pw.pack(pady=5)
field_pw = ctk.CTkEntry(app, placeholder_text="Digite sua senha", show = "*")
field_pw.pack(pady=10)

button_login = ctk.CTkButton(master=app, text="Login", command=check_login)
button_login.pack(pady=10)

button_signin = ctk.CTkButton(master=app, text="Signin", command=screen_signin)
button_signin.pack(pady=10)

button_showpw = ctk.CTkButton(master=app, text="Mostrar senha", command=show_pw)
button_showpw.pack(pady=10)

result_login = ctk.CTkLabel(app, text="")
result_login.pack(pady=10)

app.mainloop()