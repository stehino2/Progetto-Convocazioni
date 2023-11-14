'''
import PySimpleGUI as sg

allenatori = {}  # Dizionario per memorizzare gli allenatori registrati

#in questo mi momento mi appre la schermata per registrarmi 
def registrazione_layout():
    layout = [
        [sg.Text('Registrazione Allenatore')],
        [sg.Text('Nome Allenatore:'), sg.InputText(key='nome_allenatore')],
        [sg.Text('Nome Squadra:'), sg.InputText(key='squadra')],
        [sg.Button('Registra'), sg.Button('Annulla')]
    ]
    return layout

def accesso_layout():
    layout = [
        [sg.Text('Accesso Allenatore')],
        [sg.Text('Nome Allenatore:'), sg.InputText(key='nome_allenatore')],
        [sg.Text('Nome Squadra:'), sg.InputText(key='squadra')],
        [sg.Button('Accedi'), sg.Button('Annulla')]
        #[sg.Button('Reg'), sg.Button('Annulla')] #modifica di andrei
    ]
    return layout

def main():
    sg.theme('DefaultNoMoreNagging')

    registrazione_window = sg.Window('Registrazione Allenatore', registrazione_layout())
    accesso_window = sg.Window('Accesso Allenatore', accesso_layout())

    while True:
        event_reg, values_reg = registrazione_window.read()
        if event_reg in (sg.WIN_CLOSED, 'Annulla'):
            break
        elif event_reg == 'Registra':
            nome_allenatore = values_reg['nome_allenatore']
            squadra = values_reg['squadra']

            if nome_allenatore and squadra:
                allenatori[nome_allenatore] = squadra
                sg.popup(f'Benvenuto, {nome_allenatore}! Ora sei registrato con la squadra {squadra}.')
            else:
                sg.popup('Errore nella registrazione. Assicurati di inserire nome allenatore e nome squadra.')

        event_acc, values_acc = accesso_window.read()
        if event_acc in (sg.WIN_CLOSED, 'Annulla'):
            break
        elif event_acc == 'Accedi':
            nome_allenatore = values_acc['nome_allenatore']
            squadra = values_acc['squadra']

            if nome_allenatore in allenatori and allenatori[nome_allenatore] == squadra:
                sg.popup(f'Accesso riuscito per {nome_allenatore} della squadra {squadra}.')
            else:
                sg.popup('Accesso non autorizzato. Assicurati di essere registrato come allenatore della squadra.')

    registrazione_window.close()
    accesso_window.close()

if __name__ == '__main__':
    main()
'''
'''
import PySimpleGUI as sg

allenatori = {}  # Dizionario per memorizzare gli allenatori registrati

def accesso_layout():
    layout = [
        [sg.Text('Accesso Allenatore')],
        [sg.Text('Nome Allenatore:'), sg.InputText(key='nome_allenatore')],
        [sg.Text('Nome Squadra:'), sg.InputText(key='squadra')],
        [sg.Button('Accedi'), sg.Button('Registrati')]
    ]
    return layout

def registrazione_layout():
    layout = [
        [sg.Text('Registrazione Allenatore')],
        [sg.Text('Nome Allenatore:'), sg.InputText(key='nome_allenatore_reg')],
        [sg.Text('Nome Squadra:'), sg.InputText(key='squadra_reg')],
        [sg.Button('Registra'), sg.Button('Annulla')]
    ]
    return layout

def main():
    sg.theme('DefaultNoMoreNagging')

    accesso_window = sg.Window('Accesso Allenatore', accesso_layout())
    registrazione_window = None

    while True:
        event_acc, values_acc = accesso_window.read()

        if event_acc == sg.WIN_CLOSED:
            break
        elif event_acc == 'Accedi':
            nome_allenatore = values_acc['nome_allenatore']
            squadra = values_acc['squadra']

            if nome_allenatore in allenatori and allenatori[nome_allenatore] == squadra:
                sg.popup(f'Accesso riuscito per {nome_allenatore} della squadra {squadra}.')
            else:
                sg.popup('Accesso non autorizzato. Assicurati di essere registrato come allenatore della squadra.')

        elif event_acc == 'Registrati':
            accesso_window.hide()
            registrazione_window = sg.Window('Registrazione Allenatore', registrazione_layout())

        if registrazione_window:
            event_reg, values_reg = registrazione_window.read()

            if event_reg in (sg.WIN_CLOSED, 'Annulla'):
                accesso_window.un_hide()
                registrazione_window.close()
                registrazione_window = None

            elif event_reg == 'Registra':
                nome_allenatore = values_reg['nome_allenatore_reg']
                squadra = values_reg['squadra_reg']

                if nome_allenatore and squadra:
                    allenatori[nome_allenatore] = squadra
                    sg.popup(f'Benvenuto, {nome_allenatore}! Ora sei registrato con la squadra {squadra}.')
                    accesso_window.un_hide()
                    registrazione_window.close()
                    registrazione_window = None
                else:
                    sg.popup('Errore nella registrazione. Assicurati di inserire nome allenatore e nome squadra.')

    accesso_window.close()

if __name__ == '__main__':
    main()
'''

import PySimpleGUI as sg
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

def accesso_layout():
    layout = [
        [sg.Text('Accesso Allenatore')],
        [sg.Text('Nome Allenatore:'), sg.InputText(key='nome_allenatore')],
        [sg.Text('Nome Squadra:'), sg.InputText(key='squadra')],
        [sg.Button('Accedi'), sg.Button('Registrati')]
    ]
    return layout

def registrazione_layout():
    layout = [
        [sg.Text('Registrazione Allenatore')],
        [sg.Text('Nome Allenatore:'), sg.InputText(key='nome_allenatore_reg')],
        [sg.Text('Nome Squadra:'), sg.InputText(key='squadra_reg')],
        [sg.Button('Registra'), sg.Button('Annulla')]
    ]
    return layout
'''
def aggiungiGiocatore_layout():
    layout = [
        [sg.Text("Registrazione Giocatore")],
        [sg.Text("Nome Giocatore:"), sg.InputText(key = "nome_giocatore_reg")],
        [sg.Text("Cognome Giocatore:"), sg.InputText(key = "cognome_giocatore_reg")],
        [sg.Text()]
    ]
    return layout
'''
def main():
    sg.theme('DefaultNoMoreNagging')

    accesso_window = sg.Window('Accesso Allenatore', accesso_layout())
    registrazione_window = None

    while True:
        event_acc, values_acc = accesso_window.read()

        if event_acc == sg.WIN_CLOSED:
            break
        elif event_acc == 'Accedi':
            nome_allenatore = values_acc['nome_allenatore']
            squadra = values_acc['squadra']

            if nome_allenatore in allenatori and allenatori[nome_allenatore] == squadra:
                sg.popup(f'Accesso riuscito per {nome_allenatore} della squadra {squadra}.')
            else:
                sg.popup('Accesso non autorizzato. Assicurati di essere registrato come allenatore della squadra.')

        elif event_acc == 'Registrati':
            accesso_window.hide()
            registrazione_window = sg.Window('Registrazione Allenatore', registrazione_layout())

        if registrazione_window:
            event_reg, values_reg = registrazione_window.read()

            if event_reg in (sg.WIN_CLOSED, 'Annulla'):
                accesso_window.un_hide()
                registrazione_window.close()
                registrazione_window = None

            elif event_reg == 'Registra':
                nome_allenatore = values_reg['nome_allenatore_reg']
                squadra = values_reg['squadra_reg']

                if nome_allenatore and squadra:
                    allenatori[nome_allenatore] = squadra
                    save_allenatori(allenatori)
                    sg.popup(f'Benvenuto, {nome_allenatore}! Ora sei registrato con la squadra {squadra}.')
                    accesso_window.un_hide()
                    registrazione_window.close()
                    registrazione_window = None
                else:
                    sg.popup('Errore nella registrazione. Assicurati di inserire nome allenatore e nome squadra.')

    accesso_window.close()

if __name__ == '__main__':
    main()
