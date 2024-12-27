# Criar um programa de interface gráfica que deve fazer:
# Armazenar o site/software para qual a senha será gerada
# Armazenar a senha
# Possibilidade de configurar o tamanho da senha

import random
import tkinter as tk
from tkinter import messagebox
import os

class PassGen:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Password Generator")
        
        # Labels and Entry widgets
        tk.Label(self.window, text="Site/Software:").grid(row=0, column=0, padx=10, pady=10)
        self.site_entry = tk.Entry(self.window)
        self.site_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self.window, text="E-mail/Usuário:").grid(row=1, column=0, padx=10, pady=10)
        self.usuario_entry = tk.Entry(self.window)
        self.usuario_entry.grid(row=1, column=1, padx=10, pady=10)
        
        tk.Label(self.window, text="Quantidade de caracteres:").grid(row=2, column=0, padx=10, pady=10)
        self.total_chars = tk.IntVar(value=8)
        tk.Spinbox(self.window, from_=1, to=30, textvariable=self.total_chars).grid(row=2, column=1, padx=10, pady=10)
        
        # Output area
        self.output_text = tk.Text(self.window, height=5, width=32)
        self.output_text.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
        
        # Generate button
        tk.Button(self.window, text="Gerar Senha", command=self.generate_password).grid(row=4, column=0, columnspan=2, pady=10)

        # View passwords button
        tk.Button(self.window, text="Ver Senhas", command=self.view_passwords).grid(row=5, column=0, columnspan=2, pady=10)
        
    def generate_password(self):
        try:
            nova_senha = self.gerar_senha()
            self.output_text.insert(tk.END, f"Nova senha gerada: {nova_senha}\n")
            self.salvar_senha(nova_senha)
            messagebox.showinfo("Senha Gerada", "Senha gerada e salva com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao gerar senha: {e}")

    def gerar_senha(self):
        char_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%&*'
        chars = random.choices(char_list, k=self.total_chars.get())
        new_pass = ''.join(chars)
        return new_pass

    def salvar_senha(self, nova_senha):
        with open('senhas.txt', 'a', newline='') as arquivo:
            arquivo.write(f"Site: {self.site_entry.get()}, Usuário: {self.usuario_entry.get()}, Senha: {nova_senha}\n")

    def view_passwords(self):
        if not os.path.exists('senhas.txt'):
            messagebox.showwarning("Aviso", "Nenhuma senha salva.")
            return

        with open('senhas.txt', 'r') as arquivo:
            senhas = arquivo.readlines()
        
        if senhas:
            top = tk.Toplevel(self.window)
            top.title("Senhas Salvas")
            text_area = tk.Text(top, height=15, width=50)
            text_area.pack(padx=10, pady=10)
            
            for linha in senhas:
                parts = linha.strip().split(", ")
                site = parts[0].split(": ")[1]
                usuario = parts[1].split(": ")[1]
                senha = parts[2].split(": ")[1]
                text_area.insert(tk.END, f"Site/Software: {site}\n")
                text_area.insert(tk.END, f"E-mail/Usuário: {usuario}\n")
                text_area.insert(tk.END, f"Senha: {senha}\n")
                text_area.insert(tk.END, "-"*40 + "\n")
                
            text_area.config(state=tk.DISABLED)
        else:
            messagebox.showwarning("Aviso", "Nenhuma senha salva.")
        
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    gen = PassGen()
    gen.run()

