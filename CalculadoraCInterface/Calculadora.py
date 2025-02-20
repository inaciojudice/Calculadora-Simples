import tkinter as tk


# Funções para manipulação do campo de entrada e cálculos
def click_button(valor):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + valor)


def clear_entry():
    entry.delete(0, tk.END)


def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Erro")


# Configuração da janela principal
root = tk.Tk()
root.title("Calculadora")

# Campo de entrada para exibir números e resultados
entry = tk.Entry(root, width=20, font=('Arial', 20), borderwidth=5)
entry.grid(row=0, column=0, columnspan=4)

# Lista de botões da calculadora
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '+', '='
]

# Posicionamento dos botões na interface
row = 1
col = 0

for button in buttons:
    if button == '=':
        tk.Button(root, text=button, padx=40, pady=20, font=('Arial', 16), command=calculate).grid(row=row, column=col)
    else:
        tk.Button(root, text=button, padx=40, pady=20, font=('Arial', 16),
                  command=lambda b=button: click_button(b)).grid(row=row, column=col)

    col += 1
    if col > 3:
        col = 0
        row += 1

# Botão para limpar o campo de entrada
tk.Button(root, text="C", padx=40, pady=20, font=('Arial', 16), command=clear_entry).grid(row=row, column=col)

# Inicia o loop principal da interface gráfica
root.mainloop()