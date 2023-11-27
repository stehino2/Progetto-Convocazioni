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

from http.server import BaseHTTPRequestHandler, HTTPServer #importo due classi per gestire richieste HTTP e per implementare un server HTTP 
import json 

ip_address = "127.0.0.1"
port = 8080

fArchivio = "archivio.json"

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
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        decoded_data = post_data.decode("utf-8")
        dict_data = json.loads(decoded_data) #cambiare nomi variabili
        print("Recived data: ")
        print(decoded_data) #stampo il dizionario, che contiene le informazioni che mi sono arrivate dal client    
            
        if self.path == "/register_trainer":
            self.register_trainer(dict_data)
        elif self.path == "/login_trainer":
            self.login_trainer(dict_data)
        elif self.path == "/players":
            self.add_player(dict_data)

    def register_trainer(self, datad): #da cambiare nome variabile
        with open(fArchivio, "r") as file:
            try:
            #carico i dati già esistenti nel file json
                data = json.load(file)
            except json.JSONDecodeError:
                #se il file json è vuoto inizializzo una struttura valida, 
                #così da poter scriverci all'interno senza che mi dia errori
                data = {"Trainers": []}
                
        #controllo se esiste "Trainers" all'interno del file json (probabilmente posso eliminare questa riga di codice)
        if "Trainers" not in data or not isinstance(data["Trainers"], list):
            data["Trainers"] = []

        #cerco il nome dell'allenatore e il nome della squadra nel file json
        trainer_name = datad["trainer_name"]
        team_name = datad["team_name"]

        #creo il dizionario contentenente il nome dell'allenatore e il nome della squadra
        trainer = {"trainer_name": trainer_name, "team_name": team_name}

        if trainer in data.get("Trainers", []):
            self.send_error(403, "Elemento già esistente, effettua l'accesso") #errore più opportuno
            self.end_headers()
            return
        else:
            # Aggiungi il nuovo elemento alla lista
            data["Trainers"].append(trainer)

            # Ora apri il file in modalità scrittura
            with open(fArchivio, "w") as file:
                # Scrivi la nuova struttura dati JSON nel file
                json.dump(data, file, indent = 4)
            
            self.send_response(200)
            self.end_headers()

    def login_trainer(self, datad):
        with open(fArchivio, "r") as file:
            try:
            #carico i dati già esistenti nel file json
                data = json.load(file)
            except json.JSONDecodeError:
                #se il file json è vuoto inizializzo una struttura valida, 
                #così da poter scriverci all'interno senza che mi dia errori
                data = {"Trainers": []}
                
        #controllo se esiste "Trainers" all'interno del file json (probabilmente posso eliminare questa riga di codice)
        if "Trainers" not in data or not isinstance(data["Trainers"], list):
            data["Trainers"] = []

        #cerco il nome dell'allenatore e il nome della squadra nel file json
        trainer_name = datad["trainer_name"]
        team_name = datad["team_name"]

        #creo il dizionario contentenente il nome dell'allenatore e il nome della squadra
        global global_trainer 
        global_trainer = {"trainer_name": trainer_name, "team_name": team_name}

        if global_trainer in data.get("Trainers", []):
            self.send_response(200)
            self.end_headers()
            return
        else:
            self.send_error(401, "Elemento non esistente, registrati") #errore più opporturno
            self.end_headers()
            return
        
    '''
    LOGICA DI FUNZIONAMENTO DI ADD_PLAYER:
    CHIEDO IL NOME DEL TRAINER E LA SQUADRA, CERCO NEL FILE JSON QUESTI DUE, QUANDO LO TROVO, CREO UNA NUOVA SEZIONE, CHIAMATA
    PLAYERS E INSERISCO IO NOME, COGNOME, DATA
    '''

    def add_player(self, recived_data):
        with open(fArchivio, "r") as file:
            try:
            #carico i dati già esistenti nel file json
                data = json.load(file)
            except json.JSONDecodeError:
                #se il file json è vuoto inizializzo una struttura valida, 
                #così da poter scriverci all'interno senza che mi dia errori
                data = {"Trainers": []}

        '''
        POTREI ANCHE TOGLIERE LA PARTE DI CONTROLLO TRY CATCH E ANCHE IF TRAINERS NOT IN DATA ETCC..
        '''
                
        #controllo se esiste "Trainers" all'interno del file json (probabilmente posso eliminare questa riga di codice)
        if "Trainers" not in data or not isinstance(data["Trainers"], list):
            data["Trainers"] = []
        
        player_name = recived_data["player_name"]
        player_surname = recived_data["player_surname"]
        player_birth = recived_data["player_birth"]
        player = {"player_name": player_name, "player_surname": player_surname, "player_birth": player_birth}

        print(global_trainer)

        for global_trainer in data["Trainers"]:
            if "players" not in global_trainer:
                global_trainer["players"] = []
            global_trainer["players"].append(player)

        # Salva i dati aggiornati nel file JSON
            with open(fArchivio, "w") as file:
                json.dump(data, file, indent=4)

            # Invia una risposta di successo
            self.send_response(200)
            self.end_headers()
        else:
            # L'allenatore non esiste
            self.send_error(401, "Allenatore non trovato")
            self.end_headers()

        '''
        if trainer in data.get("Trainers", []):
             # Trovato l'allenatore, ora aggiungi il giocatore
            trainer_data = next((item for item in data["Trainers"] if item["trainer_name"] == trainer_name and item["team_name"] == team_name), None)
            if len(trainer_data["players"]) < 12:
                #aggiungo i dati del player in un dizionario
                player = {"player_name": player_name, "player_surname": player_surname, "player_birth": player_birth}
                trainer_data["players"].append(player)

                #invio la risposta di successo dell'operazione
                self.send_response(200)
                self.end_headers()
                return
            else:
                # Il numero massimo di giocatori è stato raggiunto
                self.send_response(402)  # Codice di errore per indicare che il numero massimo di giocatori è stato raggiunto
                self.end_headers()
                return
        else:
            # Allenatore non trovato, invia una risposta di errore
            self.send_response(401) #errore più opporturno
            self.end_headers()
            return
        '''
            
#verifico se lo script è stato eseguito direttamente 
if __name__ == "__main__":
    #Eseguo il server e verifico se è in ascolto
    webServer = HTTPServer((ip_address,port),ServerHandler)
    print("Server Started")

    try:
        #Serve per fermare il server quando è necessario (obbligare l'arresto forzato)
        webServer.serve_forever() #avvio il server e lo mantengo in ascolto per tutte le richieste HTTP
    except KeyboardInterrupt:
        pass

    webServer.server_close() #chiudo il server dopo che è stato interrotto
    print("\nServer stopped")    

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
