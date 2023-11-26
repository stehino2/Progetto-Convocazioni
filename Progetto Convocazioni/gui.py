'''
Stetco Andrei Grumezescu Ricardo
07/11/2023
Progetto Convocazioni

Scrivere un programma in python il quale, attraverso l'uso di un server, permetterà la gestione delle convocazioni dei giocatori di una squadra.

Il programma dovrà permettere le seguenti funzionalità:

1 Un utente (allenatore) si registra al sito attraverso il suo nome e il nome della squadra che allena. Tutti i futuri acessi avverrano attraverso questi due parametri.

2 L'allenatore potrà attraverso una schermata aggiungere giocatori alla sua squadra, inserendo: Nome, Cognome, Anno di nascita. (L'aggiunta di giocatori dovrà essere possibile in qualsiasi momento).

3 L'allenatore dovrà poter rimuovere un giocatore dalla lista o poter modificare uno dei dati di quelli inseriti in precedenza.

4 L'allenatore potrà premere il tasto "fine stagione", il quale mantiene la lista dei giocatori, ma svuota i dati relativi alle convocazioni

L'allenatore potrà fare le convocazioni e quindi inserire una lista di giocatori da convocare alla prossima partita (minino 10 massimo 12). Nella schermata di scelta giocatori dovrà poter vedere:
- (5) Per ogni giocatore, a che data risale l'ultima partita giocata
- (6) Per ogni giocatore, il numero di partite giocate in quella stagione
(7) Nella convocazione dovrà inserire l'ora, la data e l'indirizzo della palestra dove si giocherà la partita. Confermata la convocazione il server fornirà una stringa di testo che l'allenatore potrà copiare e incollare nell'ipotetico gruppo whatsapp della squadra.
(Esempio del messaggio: Ciao a tutti! La partita sarà il 12/11/2023 in Via dell'Usignolo 4. I convocati sono i seguenti: Carlo, Mario, ... Buona giornata a tutti!).

8 Tutto il lato client del programma dovrà essere utilizzabile attraverso un'interfaccia grafica (TKinter)

9 Il codice deve essere commentato per rendere comprensibile ogni sua parte importante a livello logico. 

10 Deve essere poi presente un file (doc o pdf) che documenta il programma e presenta le sue varie funzionalità

11 Il programma poi dovrà essere presentato al resto della classe (Lascio a voi scegliere se preparare un ppt oppure no, in ogni caso va mostrato il programma in esecuzione). La documentazione può essere usata nella presentazione.

Extra:
- Una convocazione dopo la conferma potrà essere modificata (sia indirizzo che data che giocatori)
- Un giocatore potrà accedere attraverso il suo nome, cognome e la sua squadra e vedere le partite che ha giocato in questa stagione.
'''

import PySimpleGUI as sg
import requests
import json

ip_address = "127.0.0.1"
port = "8080"

def registerTrainer(item):
    url = "http://" + ip_address + ":" + port + "/register_trainer"
    headers = {'Content-type' : 'application/json'} #tipo di dato che mando
    response = requests.post(url, data = item, headers = headers)
    return response

def loginTrainer(item):
    url = "http://" + ip_address + ":" + port + "/login_trainer"
    headers = {"Content-type": "application/json"}
    response = requests.post(url, data = item, headers = headers)
    return response

def addPlayer(item):
    url = "http://" + ip_address + ":" + port + "/players"
    headers = {'Content-type' : 'application/json'} #tipo di dato che mando
    response = requests.post(url, data = item, headers = headers)
    return response

def login_screen():
    layout = [
        [sg.Text("Accesso Allenatore")],
        [sg.Text("Nome Allenatore"), sg.InputText(key = "trainer_name")],
        [sg.Text("Nome Squadra"), sg.InputText(key = "team_name")],
        [sg.Button("Accedi"), sg.Button("Registrati")]
    ]

    window = sg.Window("Accesso", layout)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED:
            break
        elif event == "Accedi":
            trainer_name = values["trainer_name"]
            team_name = values["team_name"]

            trainer = {"trainer_name" : trainer_name, "team_name" : team_name} 
            trainer = (json.dumps(trainer))

            if loginTrainer(trainer).status_code == 200:
                window.hide()
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

    window = sg.Window("Registrazione", layout)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED:
            break
        elif event == "Annulla":
            window.close()
        elif event == "Registra":
            trainer_name = values["trainer_name"]
            team_name = values["team_name"]

            trainer = {"trainer_name" : trainer_name, "team_name" : team_name} 
            trainer = (json.dumps(trainer))

            if registerTrainer(trainer).status_code == 200:
                '''
                https://developer.mozilla.org/en-US/docs/Web/HTTP/Status#client_error_responses
                '''
                #se non esiste già l'allenatore e la squadra ricevo il codice 200
                #e quindi l'operazione di registrazione è andata a buon fine
                sg.PopupOK("Registrazione effettuata col nome " + trainer_name + " e con la squadra " + team_name, title = "Registrazione effettuata!")
                window.close()
            else:
                #se invece l'allenatore e la squadra esistono già riceverò un altro
                #codice, quindi l'operazione di registrazione non è andata a buon fine
                sg.PopupOK("Errore durante la registrazione, il nome dell'allenatore e la squadra eistono già")  

    window.close()

def main_screen(trainer_name):
    layout = [
        [sg.Text("Benvenuto allenatore " + trainer_name)],
        [sg.Button("Aggiungi giocatore"), sg.Button("Logout")]
    ]
    window = sg.Window("Selezione", layout)

    while True:
        event = window.read()

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
        [sg.Text("Anno di nascita"), sg.InputText(key = "player_birth_year")],
        [sg.Button("Aggiungi"), sg.Button("PULSANTE")]
    ]

    window = sg.Window("Aggiunta Giocatori", layout)

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

    window.close()    

if __name__ == "__main__":
    login_screen()