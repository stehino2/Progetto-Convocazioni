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
