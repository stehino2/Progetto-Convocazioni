'''
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


import requests
import json

def lista_spesa():
    url = "http://127.0.0.1:8080/lista"
    response = requests.get(url)
    return response.json()

def aggiungi_in_lista(item):
    url = "http://127.0.0.1:8080/aggiungi"
    headers = {'Content-type': 'application/json'}
    response = requests.post(url, data=json.dumps(item), headers=headers)
    return response.text

def n_richieste():
    url = "http://127.0.0.1:8080/richieste"
    response = requests.get(url)
    return response.json()

continua = True
richieste_utente = 0

nome_utente = input("Inserisci il tuo nome utente: ")
nome_squadra = input("Inserisci il nome della tua squadra: ")

while continua:
    print("\nScegli un'azione:")
    print("1. Visualizza la lista della spesa")
    print("2. Aggiungi un elemento alla lista della spesa")
    print("3. Visualizza il conteggio delle richieste")
    print("4. Esci")
    scelta = input("Scelta: ")

    if scelta == "1":
        try:
            lista = lista_spesa()
            print("Lista della spesa:", lista)
        except Exception as e:
            print("Lista della spesa vuota")
    elif scelta == "2":
        try:
            item = input("Inserisci un elemento: ")
            aggiungi_in_lista(item)
            richieste_utente += 1  # Incrementa il conteggio delle richieste dell'utente
            print("Elemento aggiunto alla lista della spesa.")
        except Exception as e:
            print("Errore durante la connettività con il server")
    elif scelta == "3":
        try:
            conteggio_richieste = n_richieste()
            print("Totale richieste:", conteggio_richieste["richieste totali"])
            print(f"Le tue richieste totali: {richieste_utente}")
        except Exception as e:
            print("Errore durante il conteggio delle richieste")
    elif scelta == "4":
        continua = False