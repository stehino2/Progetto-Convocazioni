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

from http.server import BaseHTTPRequestHandler, HTTPServer
import json

hostName = "127.0.0.1"
serverPort = 8080

# Dizionario per la lista della spesa
lista_spesa = []
# Dizionario per tenere traccia delle richieste di ciascun utente
user_requests = {}

class ServerHandler(BaseHTTPRequestHandler):

    def set_headers(self, ctype):
        self.send_response(200)
        self.send_header('Content-type', ctype)
        self.end_headers()

    def write_response(self, content):
        self.wfile.write(bytes(content, "utf-8"))

    def do_GET(self):
        if self.path == "/lista":
            # Gestisci la richiesta per visualizzare la lista della spesa
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(lista_spesa).encode())
        elif self.path == "/richieste":
            # Gestisci la richiesta per visualizzare il conteggio delle richieste
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            richieste_totali = sum(user_requests.values())
            username = self.headers.get('Username')
            richieste_utente = user_requests.get(username, 0)
            response = {
                "richieste totali": richieste_totali,
                "mie richieste": richieste_utente
            }
            self.wfile.write(json.dumps(response).encode())

    def do_POST(self):
        if self.path == "/aggiungi":
            # Gestisci la richiesta per aggiungere un elemento alla lista della spesa
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            item = json.loads(post_data.decode('utf-8'))
            lista_spesa.append(item)

            # Registra la richiesta dell'utente
            username = self.headers.get('Username')
            if username:
                user_requests[username] = user_requests.get(username, 0) + 1

            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write("Elemento aggiunto alla lista della spesa.".encode())

if __name__ == "__main__": 
    # Esegui il server e mantienilo in ascolto
    webServer = HTTPServer((hostName, serverPort), ServerHandler)
    print("Server started")

    try:
        # Serve per fermare il server quando necessario
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("\nServer stopped")
