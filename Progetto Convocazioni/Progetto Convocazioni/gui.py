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
'''
import PySimpleGUI as sg
import os
import json
import requests
from client import funzioni

FILENAME = 'allenatori.json'
url = "http://127.0.0.1:8080"

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
        [sg.Text("Accesso Allenatore")],
        [sg.Text("Nome Allenatore"), sg.InputText(key = "nome_allenatore")],
        [sg.Text("Nome Squadra"), sg.InputText(key='squadra')],
        [sg.Button("Accedi"), sg.Button('Registrati')]
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

def aggiungiGiocatore_layout():
    layout = [
        [sg.Text("Registrazione Giocatore")],
        [sg.Text("Nome Giocatore:"), sg.InputText(key = "nome_giocatore_reg")],
        [sg.Text("Cognome Giocatore:"), sg.InputText(key = "cognome_giocatore_reg")],
        [sg.Text()]
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
                #da mettere richiesta post

                #response = requests.post(url, data=json.dumps(nome_allenatore))

                sg.popup(f'Accesso riuscito per {nome_allenatore} della squadra {squadra}.')
            else:
                #anche qui
                sg.popup('Accesso non autorizzato. Assicurati di essere registrato come allenatore della squadra.') #da mettere errore 403

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
                    # Effettua una richiesta POST al server per registrare l'allenatore
                    response = requests.post(f"{url}/registra_allenatore", data=json.dumps({'nome_allenatore': nome_allenatore, 'squadra': squadra}))

                    # Controlla la risposta del server

                    #probema con accesso

                    if response.status_code == 200:
                        sg.popup(f'Benvenuto, {nome_allenatore}! Ora sei registrato con la squadra {squadra}.')
                        accesso_window.un_hide()
                        registrazione_window.close()
                        registrazione_window = None
                    else:
                        sg.popup(f'Errore nella registrazione: {response.json().get("errore", "Errore sconosciuto")}')
                else:
                    sg.popup('Errore nella registrazione. Assicurati di inserire nome allenatore e nome squadra.')

    accesso_window.close()

if __name__ == '__main__':
    main()

'''    
import PySimpleGUI as sg
import requests
import json

ip_address = "127.0.0.1"
port = "8080"

def addTrainer(item):
    url = "http://" + ip_address + ":" + port + "/archivio_allenatori"
    headers = {'Content-type' : 'application/json'} #tipo di dato che mando
    response = requests.post(url, data = item, headers = headers)
    return response

def addPlayer(item):
    url = "http://" + ip_address + ":" + port + "/giocatori"
    headers = {'Content-type' : 'application/json'} #tipo di dato che mando
    response = requests.post(url, data = item, headers = headers)
    return response

'''
def access_layout():
    layout = [
        [sg.Text("Accesso Allenatore")],
        [sg.Text("Nome Allenatore"), sg.InputText(key = "trainer_name")],
        [sg.Text("Nome Squadra"), sg.InputText(key = "team_name")],
        [sg.Button("Accedi"), sg.Button("Registrati")]
    ]
    return layout

def register_layout():
    layout = [
        [sg.Text("Registrazione Allenatore")],
        [sg.Text("Nome allenatore"), sg.InputText(key = "trainer_name")],
        [sg.Text("Nome Squadra"), sg.InputText(key = "team_name")],
        [sg.Button("Registra"), sg.Button("Annulla")]
    ]
    return layout

def addPlayers_layout():
    layout = [
        [sg.Text("Registrazione Giocatore")],
        [sg.Text("Nome"), sg.InputText(key = "player_name")],
        [sg.Text("Cognome"), sg.InputText(key = "player_surname")],
        [sg.Text("Anno di nascita"), sg.InputText(key = "player_year")],
        [sg.Button("Aggiungi")]
    ]
    return layout
'''

def login_screen():
    layout = [
        [sg.Text("Accesso Allenatore")],
        [sg.Text("Nome Allenatore"), sg.InputText(key = "trainer_name")],
        [sg.Text("Nome Squadra"), sg.InputText(key = "team_name")],
        [sg.Button("Accedi"), sg.Button("Registrati")]
    ]

    window = sg.Window("TITOLO", layout)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED:
            break
        elif event == "Accedi":
            trainer_name = values["trainer_name"]
            team_name = values["team_name"]

            #sg.PopupOK("Accesso effettuato col nome " + trainer_name + " e con la squadra " + team_name, title = "Accesso effettuato!")

            trainer = {"name" : trainer_name, "team" : team_name} 
            trainer = (json.dumps(trainer))
            addTrainer(trainer)

            window.hide()
            #window.close()
            main_screen(trainer_name)
        elif event == "Registrati":
            #window.close()
            register_screen()

    window.close()

def register_screen():
    layout = [
        [sg.Text("Registrazione Allenatore")],
        [sg.Text("Nome allenatore"), sg.InputText(key = "trainer_name")],
        [sg.Text("Nome Squadra"), sg.InputText(key = "team_name")],
        [sg.Button("Registra"), sg.Button("Annulla")]
    ]

    window = sg.Window("TITOLO", layout)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED:
            break
        elif event == "Registra":
            trainer_name = values["trainer_name"]
            team_name = values["team_name"]

            sg.PopupOK("Registrazione effettuata col nome " + trainer_name + " e con la squadra " + team_name, title = "Registrazione effettuata!")

            trainer = {"name" : trainer_name, "team" : team_name} 
            trainer = (json.dumps(trainer))
            addTrainer(trainer)

    window.close()

def main_screen(trainer_name):
    layout = [
        [sg.Text("Benvenuto allenatore " + trainer_name)],
        [sg.Button("Aggiungi giocatore"), sg.Button("Logout")]
    ]
    window = sg.Window("TILOTO", layout)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == "Logout":
            break
        elif event == "Aggiungi giocatore":
            add_players_screen(trainer_name)

    window.close()

def add_players_screen(trainer_name):
    layout = [
        [sg.Text("Registrazione Giocatore")],
        [sg.Text("Nome"), sg.InputText(key = "player_name")],
        [sg.Text("Cognome"), sg.InputText(key = "player_surname")],
        [sg.Text("Anno di nascita"), sg.InputText(key = "player_year")],
        [sg.Button("Aggiungi")]
    ]

    window = sg.Window('Add Players', layout)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED: #agigungi tasto
            break
        elif event == "Aggiungi":
            player_name = values["player_name"]
            player_surname = values["player_surname"]
            player_birth_year = values["player_birth_year"]
            player = {"name": player_name, "surname": player_surname, "birth_year": player_birth_year}
            player = (json.dumps(player))
            addPlayer(player)
            print(player)

    window.close()    

if __name__ == '__main__':
    login_screen()

'''
def main():
    sg.theme("DefaultNoMoreNagging") #tema della finestra

    access_window = sg.Window("Accesso Allenatore", access_layout())

    while True:
        event_access, values_access = access_window.read()

        if event_access == sg.WIN_CLOSED: #chiudo la finestra
            break
        elif event_access == "Accedi": #se premo accedi
            trainer_name = values_access["trainer_name"]
            team_name = values_access["team_name"]

            #sg.PopupOK("Accesso effettuato col nome " + trainer_name + " e con la squadra " + team_name, title = "Accesso effettuato!")

            trainer = {"name" : trainer_name, "team" : team_name} 
            trainer = (json.dumps(trainer))
            addTrainer(trainer)
            #response = requests.post(url, data = trainer)

            yes_no = sg.popup_yes_no("Accesso effetuato con successo, vuoi aggiungere giocatori alla tua squadra?", title = "TITOLO ANCORA DA DARE") 
            if yes_no == "Yes":
                access_window.hide()
                addplayers_window = sg.Window("Aggiungi Giocatori", addPlayers_layout())
                

                if addplayers_window:
                    event_players, values_players = addplayers_window.read()

                if event_access == sg.WIN_CLOSED: #chiudo la finestra
                    break
            else:
                print("hai premuto no")

        #dopo aver inserito i dati, devo chiudere la finestra e aprirne un'altra per inserire i giocatori

        elif event_access == "Registrati":
            access_window.hide()
            register_window = sg.Window("Registrazione Allenatore", register_layout())

        if register_window:
            event_reg, values_reg = register_window.read()

            if event_reg in (sg.WIN_CLOSED, "Annulla"):
                access_window.un_hide()
                register_window.close()
                #da aggiungere che quando premo il bottone Annulla torno indietro alla pagina di accesso

            elif event_reg == "Registra":
                trainer_name = values_reg["trainer_name"]
                team_name = values_reg["team_name"]

                sg.PopupOK("Registrazione effettuata col nome " + trainer_name + " e con la squadra " + team_name, title = "Registrazione effettuata!")

                trainer = {"name" : trainer_name, "team" : team_name} 
                trainer = (json.dumps(trainer))
                addTrainer(trainer) 

        access_window.close()

if __name__ == "__main__":
    main()
'''
