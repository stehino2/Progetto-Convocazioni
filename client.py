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

#Grumezescu Ricardo 5^CI
import requests
import json 
#import os #libreria che mi serve per eliminare il file

#file = open("Utonto.json", "w")
#file.close
#file = open("Utonto.json", "a")

IPADDRESS = "127.0.0.1"
PORTADDRESS = "8080"

ip_address = "127.0.0.1"
port = "8080"


def ArchivioUtenti():
    url = "http://"+IPADDRESS+":"+PORTADDRESS+ "/team" #specifico l'URL dove verra inviata la richiesta GET
    response = requests.get(url) #utilizzo la libreria requests per effetuare la richiesta GET all'URL specificato. risposta memorizzata nella variabile response
    return response.json()  #restituisce i dati della risposta sotto forma di JSON

def addPlayer(item):
    url = "http://"+IPADDRESS+":"+PORTADDRESS+ "/newplayers"
    headers = {'Content-type': 'application/json'}
    response = requests.post(url, data=json.dumps(item), headers=headers)
    return response.text

def addAllenatore(item): #poi cambia nome se vuoi
    url = "http://" + ip_address + ":" + port + "/archivio_allenatori"
    headers = {'Content-type' : 'application/json'} #tipo di dato che mando
    response = requests.post(url, data=item, headers=headers)
    return response


#continua = True

#while continua:
        


nome_utente = input("Inserisci il tuo nome utente: ")
team_utente = input("Inserisci nome della tua squadra: ")

allenatore = {"name":nome_utente,"team":team_utente}
            #people.append(persona.copy()) 
jsallenatore = (json.dumps(allenatore))
print (allenatore)
addAllenatore(jsallenatore)

#file.write(json.dumps(allenatore, indent=4))

#file.close()



#print("File Aperto")
#file = open("Utonto.json", "r")
#contenuto = json.load(file)
#addAllenatore(contenuto)
#file.close
#print("Contenuto del file:", contenuto)
#print("Elimino il file")
#os.remove("Utonto.json") 



continua = True
richieste_utente = 0

'''
Scrivere un programma in python il quale, attraverso l'uso di un server, permetterà la gestione delle convocazioni dei giocatori di una squadra.

Il programma dovrà permettere le seguenti funzionalità:

1 Un utente (allenatore) si registra al sito attraverso il suo nome e il nome della squadra che allena. Tutti i futuri acessi avverrano attraverso questi due parametri.
'''
#nome_utente = input("Inserisci il tuo nome utente: ")
#nome_squadra = input("Inserisci il nome della tua squadra: ")

