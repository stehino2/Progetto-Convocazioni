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
  
import requests
import json 

ip_address = "127.0.0.1"
port = "8080"

def ArchivioUtenti():
    url = "http://"+ip_address+":"+port+ "/team" #specifico l'URL dove verra inviata la richiesta GET
    response = requests.get(url) #utilizzo la libreria requests per effetuare la richiesta GET all'URL specificato. risposta memorizzata nella variabile response
    return response.json()  #restituisce i dati della risposta sotto forma di JSON

def addPlayers(item):
    url = "http://" + ip_address + ":" + port + "/archivio_allenatori/players"
    headers = {'Content-type' : 'application/json'} #tipo di dato che mando
    response = requests.post(url, data=item, headers=headers)
    return response
    """url = "http://"+IPADDRESS+":"+PORTADDRESS+ "/newplayers"
    headers = {'Content-type': 'application/json'}
    response = requests.post(url, data=json.dumps(item), headers=headers)
    return response.text"""

def addAllenatore(item): #poi cambia nome se vuoi
    url = "http://" + ip_address + ":" + port + "/archivio_allenatori"
    headers = {'Content-type' : 'application/json'} #tipo di dato che mando
    response = requests.post(url, data=item, headers=headers)
    return response

#Mi permette di inserire un nuovo Utente

nome_utente = input("Inserisci il tuo nome utente: ")
team_utente = input("Inserisci nome della tua squadra: ")
allenatore = {"name":nome_utente,"team":team_utente} 
jsallenatore = (json.dumps(allenatore))
print (jsallenatore)
addAllenatore(jsallenatore)

#Andiamo ad inserire giocatori all interno di un team
players = {"Allenatore( "+ nome_utente +" ) e Squadra( "+ team_utente +" ) Players:":[]}
RispRichiestaTeam = input("Hai intezione di inserire dei giocatori all'interno del tuo team [y/n]: \n")
if RispRichiestaTeam == "y":
    player_number = 0
    while RispRichiestaTeam == "y":
        player_name = input("Inserisci il nome del player: \n")
        player_surname = input("Inserisci il cognome del player: \n")
        player_year = input("Inserisci l'anno di nascita del player del player: \n")

        player = {"name":player_name,"surname":player_surname, "birth_year": player_year}
        player_number += 1
        #players["Player"+ str(player_number)]= player
        players["Allenatore( "+ nome_utente +" ) e Squadra( "+ team_utente +" ) Players:"].append(player)
        RispRichiestaTeam = input("Hai intezione di inserire altri giocatori all'interno del tuo team [y/n] \n")

    jsplayers = (json.dumps(players))#trasformo il dizionario in json
    print(jsplayers) 
    addPlayers(jsplayers)
   

elif RispRichiestaTeam == "n":
    print("Richiesta di inserire utente rifiutata")

else:
    print("Valore inserito non coretto")
