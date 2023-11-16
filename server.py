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

#Grumezescu Ricardo 5^CI e stehino the best
from http.server import BaseHTTPRequestHandler, HTTPServer #importo due classi per gestire richieste HTTP e per implementare un server HTTP 
import json 

FILENAME = 'allenatori.json' 

'''

def registra_allenatore(self, nome_allenatore, nome_squadra):
        try:
            with open("allenatori.json", "r") as file:
                allenatori = json.load(file)
        except FileNotFoundError:
            allenatori = []

        nuovo_allenatore = {"nome_allenatore": nome_allenatore, "nome_squadra": nome_squadra}
        allenatori.append(nuovo_allenatore)

        with open("allenatori.json", "w") as file:
            json.dump(allenatori, file)

COSA DEVO FARE:
1. quando l'utente si registra, devo fare una richiesta post e inserire l'utente nel file json allenatori.json, se c'è un errore nella registrazione
o nell'accesso devo inviare un errore 403/altro errore

'''

HOSTNAME = "127.0.0.1"
SERVERPORT = 8080

f = "utente.json"
allenatori = []

#Dizionario per la gestione degli utenti(allenatore)
ArchivioAllenatori  = "allenatori.json"

#Definisco una nuova classe  che eredita i metodi e le proprieta di BaseHttpRequestHandler(GET,POST)
class ServerHandler(BaseHTTPRequestHandler):

    #impostiamo un header di risposta
    def set_headers(self,ctype):
        self.send_response(200) #richiesta elaborata con successo
        self.send_header('Content-type', ctype) #aggiungo un header indicando il tipo di contenuto che il server sta inviando al cliente con ctype intendo un parametro che deve essere fornito quando la funzione viene chiamata
        self.end_headers() #fine header ora il server puo inviare il corpo effettivo della risposta

    #funzione utilizzata per scrivere il contenuto di una risposta HTTP nel corpo della risposta
    def write_response(self, content):
        self.wfile.write(bytes(content,"utf-8")) #metodo scrive dati nel corpom della risposta HTTP, (self.wfile) associato di solito ai client , bytes(cont, "utf-8") questa parte converte la stringa 'content' in una sequenza di byte utilizzando l'encoding UTF-8

    def do_POST(self):
        if self.path == "/archivio_allenatori":
            content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
            post_data = self.rfile.read(content_length) # <--- Gets the data itself

            js = post_data.decode("utf-8")
            js = json.loads(js)
            print(js)
            #js = str(js)
            #stampa file in json
            with open("utente.json", "w") as file:
                json.dump(allenatori, file)

            #file_uno = open("esempio_uno.txt", "w")
            #file_uno.write(js)
            #file_uno.close()    # ricordate sempre di chiudere i file!
                        




            #print(post_data)
            #item = json.loads(post_data.decode('utf-8'))




            self.send_response(200)
            #nome_allenatore = self.rfile.read(content_length)

            #allenatori.append(item)
            #print(allenatori)
            #f.write(json.dumps(st, indent = 4))
            #allenatori.append(item)
'''
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write("Elemento aggiunto alla lista della alllenatore.".encode())
            
            nome_squadra_json = {"name" : "", "team" : ""}
            name = item["name"]
            team = item["team"]
            dict_allenatore = {"name" : name,
                               "team" : team}
            st = str(dict_allenatore)
            f.write(json.dumps(st, indent = 4))
            print(dict_allenatore)
            #print(item)
            '''


'''
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])  # lunghezza della richiesta
        payload = self.rfile.read(content_length)
        data = json.loads(payload.decode('utf-8'))

        # Verifica se la richiesta è per la registrazione di un nuovo allenatore
        if self.path == "/registra_allenatore":
            """content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            item = json.loads(post_data.decode('utf-8'))
            lista_spesa.append(item)"""
            nome_allenatore = self.rfile.read(content_length)#linea di codice è responsabile di estrarre i dati inviati dal client nel corpo del messaggio della richiesta HTTP.
            
            nome_allenatore = data.get('nome_allenatore', '')
            squadra = data.get('squadra', '')
            

            # Verifica se l'allenatore esiste già
            #if nome_allenatore in allenatori:
            #    self.invia_errore(400, 'L\'allenatore esiste già. Scegli un altro nome.')
            #    return

            if nome_allenatore and squadra:
                # Carica il vecchio archivio degli allenatori
                with open(ArchivioAllenatori, 'r') as file:
                    allenatori = json.load(file)

                # Aggiungi il nuovo allenatore
                allenatori[nome_allenatore] = squadra

                # Salva l'archivio aggiornato
                with open(ArchivioAllenatori, 'w') as file:
                    json.dump(allenatori, file)

                # Invia una risposta di successo al client
                self.send_response(200)
                self.send_header('Content-type', 'application/json') #?
                self.end_headers()                                  #?
                #response = {'messaggio': 'Allenatore registrato con successo'}
                #self.wfile.write(json.dumps(response).encode('utf-8'))
                self.set_headers("text/html") #invio la risposta
                self.write_response("tutto ok")
            else:
                # Invia una risposta di errore al client
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                response = {'errore': 'Parametri mancanti per la registrazione dell\'allenatore'}
                self.wfile.write(json.dumps(response).encode('utf-8'))
'''
#verifico se lo script è stato eseguito direttamente 
if __name__ == "__main__":
    #Eseguo il server e verifico se è in ascolto
    webServer = HTTPServer((HOSTNAME,SERVERPORT),ServerHandler)
    print("Server Started")

    try:
        #Serve per fermare il server quando è necessario (obbligare l'arresto forzato)
        webServer.serve_forever() #avvio il server e lo mantengo in ascolto per tutte le richieste HTTP
    except KeyboardInterrupt:
        pass

    webServer.server_close() #chiudo il server dopo che è stato interrotto
    print("\nServer stopped")    