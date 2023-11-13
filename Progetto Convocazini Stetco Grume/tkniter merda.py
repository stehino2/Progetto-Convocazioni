import tkinter as tk
from tkinter import simpledialog, messagebox
import os
import json

FILENAME = 'allenatori.json'

def save_allenatori(allenatori_data):
    with open(FILENAME, 'w') as file:
        json.dump(allenatori_data, file)

def load_allenatori():
    if os.path.exists(FILENAME):
        with open(FILENAME, 'r') as file:
            return json.load(file)
    else:
        return {}

allenatori = load_allenatori()

def accesso_callback():
    nome_allenatore = nome_allenatore_entry.get()
    squadra = squadra_entry.get()

    if nome_allenatore in allenatori and allenatori[nome_allenatore] == squadra:
        messagebox.showinfo('Accesso Riuscito', f'Accesso riuscito per {nome_allenatore} della squadra {squadra}.')
    else:
        messagebox.showwarning('Accesso Non Autorizzato', 'Accesso non autorizzato. Assicurati di essere registrato come allenatore della squadra.')

def registrazione_callback():
    global registrazione_window
    nome_allenatore_reg = nome_allenatore_reg_entry.get()
    squadra_reg = squadra_reg_entry.get()

    if nome_allenatore_reg and squadra_reg:
        allenatori[nome_allenatore_reg] = squadra_reg
        save_allenatori(allenatori)
        messagebox.showinfo('Registrazione Riuscita', f'Benvenuto, {nome_allenatore_reg}! Ora sei registrato con la squadra {squadra_reg}.')
        registrazione_window.destroy()
    else:
        messagebox.showwarning('Errore nella Registrazione', 'Assicurati di inserire nome allenatore e nome squadra.')

def registrazione_window_close():
    global registrazione_window
    accesso_window.deiconify()
    registrazione_window.destroy()

def registrazione_window_callback():
    global registrazione_window
    registrazione_window = tk.Toplevel(accesso_window)
    registrazione_window.title('Registrazione Allenatore')

    nome_allenatore_reg_label = tk.Label(registrazione_window, text='Nome Allenatore:')
    nome_allenatore_reg_label.grid(row=0, column=0, sticky='E', padx=5, pady=5)
    squadra_reg_label = tk.Label(registrazione_window, text='Nome Squadra:')
    squadra_reg_label.grid(row=1, column=0, sticky='E', padx=5, pady=5)

    global nome_allenatore_reg_entry, squadra_reg_entry
    nome_allenatore_reg_entry = tk.Entry(registrazione_window)
    nome_allenatore_reg_entry.grid(row=0, column=1, padx=5, pady=5)
    squadra_reg_entry = tk.Entry(registrazione_window)
    squadra_reg_entry.grid(row=1, column=1, padx=5, pady=5)

    registra_button = tk.Button(registrazione_window, text='Registra', command=registrazione_callback)
    registra_button.grid(row=2, column=0, columnspan=2, pady=10)

    annulla_button = tk.Button(registrazione_window, text='Annulla', command=registrazione_window_close)
    annulla_button.grid(row=3, column=0, columnspan=2, pady=5)

# Main window
accesso_window = tk.Tk()
accesso_window.title('Accesso Allenatore')

nome_allenatore_label = tk.Label(accesso_window, text='Nome Allenatore:')
nome_allenatore_label.grid(row=0, column=0, sticky='E', padx=5, pady=5)
squadra_label = tk.Label(accesso_window, text='Nome Squadra:')
squadra_label.grid(row=1, column=0, sticky='E', padx=5, pady=5)

nome_allenatore_entry = tk.Entry(accesso_window)
nome_allenatore_entry.grid(row=0, column=1, padx=5, pady=5)
squadra_entry = tk.Entry(accesso_window)
squadra_entry.grid(row=1, column=1, padx=5, pady=5)

accedi_button = tk.Button(accesso_window, text='Accedi', command=accesso_callback)
accedi_button.grid(row=2, column=0, columnspan=2, pady=10)

registrati_button = tk.Button(accesso_window, text='Registrati', command=registrazione_window_callback)
registrati_button.grid(row=3, column=0, columnspan=2, pady=5)

accesso_window.mainloop()
