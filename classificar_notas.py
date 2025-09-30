import tkinter as tk
from tkinter import messagebox

def verificar_nota():
    nota_texto = entry_nota.get()
    
    if nota_texto.replace(".", "", 1).isdigit():  # verifica se é número (aceita decimal)
        nota = float(nota_texto)
        
        if nota == 10:
            resultado = "Parabéns, nota máxima!"
        elif 9 <= nota < 10:
            resultado = "Quase perfeito!"
        elif 0 <= nota <= 4.9:
            resultado = "Reprovado com baixa nota."
        elif nota >= 7:
            resultado = "Aprovado!!"
        elif nota >= 5:
            resultado = "Recuperação!!"
        else:
            resultado = "Nota inválida."
            
        messagebox.showinfo("Resultado", f"Situação: {resultado}")
    else:
        messagebox.showerror("Erro", "Digite um número válido.")

# Janela principal
root = tk.Tk()
root.title("Verificador de Nota")
root.geometry("300x200")
root.configure(bg="#8CB9F0")  # fundo amarelo claro

# Widgets
tk.Label(root, text="Digite a nota do aluno:", bg="#A58CF0", fg="black", font=("Arial", 11, "bold")).pack(pady=10)
entry_nota = tk.Entry(root)
entry_nota.pack(pady=5)
tk.Button(root, text="Verificar", command=verificar_nota, bg="blue", fg="white", font=("Arial", 11, "bold")).pack(pady=15)

root.mainloop()