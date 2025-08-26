import tkinter as tk
from tkinter import messagebox
senhat = str(input("Insira a senha para ser válidada: "))
def login_user():
    senha_user = entry_senha.get()
    senha = str(senha_user)
    if len(senha) ==8:
        if senha == senhat:
            resultado = "Senha correta!"
        else:
            resultado = "Senha incorreta"
        messagebox.showinfo("Resultado: ",resultado)
    else:
        messagebox.showerror("Valor inválido!","Valor Inválido!")
root = tk.Tk()
root.geometry("300x150")
root.title("Cavalo advinho das senhas!")
root.configure(bg="#F3F168")
tk.Label(root, text = "Senha: ", bg = "green", fg= "Black", font=("Arial", 12, "bold")).pack(pady=10)
entry_senha= tk.Entry(root)
entry_senha.pack(pady=15)
tk.Button(root, text = "Verificar", command = login_user, bg = "Purple", fg = "Black", font=("Arial", 12, "bold")).pack(pady=15)
root.mainloop()   