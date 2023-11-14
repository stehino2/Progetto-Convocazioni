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

HOSTNAME = "127.0.0.1"
SERVERPORT = 8080

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

    def do_GET(self):
        if self.path == "/archivio_allenatori":
            self.set_headers("application/json")
            f = open("allenatori.json", "rb") #read byte
            old_json = json.loads(f.read())
            out = json.dumps(old_json) #converto il dizionario in stringa
            f = open("allenatori.json", "w") #apro il file json
            self.write_response(out) #scrivo il dizionario nuovo modificato
            self.set_headers("text/html") #invio la risposta
            self.write_response("tutto ok")

            '''
            content_length = int(self.headers['Content-Length']) #lunghezza della richiesta
            print(self.headers)
            post_data = self.rfile.read(content_length)
            new_json = post_data.decode('utf-8') #leggo il file json che mi arriva dalla richiest
            new_json = (json.loads(new_json)) # lo converto in json
            f = open("allenatori.json", "rb") #read byte
            old_json = json.loads(f.read())
            out = json.dumps(old_json) #converto il dizionario in stringa
            f = open("allenatori.json", "w") #apro il file json
            f.write(out) #scrivo il dizionario nuovo modificato
            self.set_headers("text/html") #invio la risposta
            self.write_response("tutto ok")
            f
            '''
        
        #if self.path =="/autentification":

    
    #def do_POST(self):

        #if self.path =="/registration":


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