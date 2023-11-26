# TODO LIST

- [] Un utente (allenatore) si registra al sito attraverso il suo nome e il nome della squadra che allena. Tutti i futuri acessi avverrano attraverso questi due parametri.
    - [x] Fare il controllo dell'inserimento dei dati nell'accesso 
    - [x] controllo nella registrazione 
    # controllo da rivedere, se voglio che avvenga solo se c'è sia nome che squadra uguali, oppure nome diverso, ma squadra uguale, perché
    # non ha troppo senso che esistano due allenatori diversi per la stessa squadra (non sempre non ha senso, e non sempre ha senso)
    - [x] sistema pulsante annulla
    - [] sistema logout
    - [] sistema crash della gui.py
    - [x] sistema vari titoli etc..
    - [x] evitare che quando non si inserisce nulla faccia registrazione/accesso
    - [] potresti mettere i send_error al posto dei send_response quando invio dati al client
    - [] cambiare alcuni nomi variabili
    - # potremmo modificare la schermata di accesso, quando premo registrati invece di mandarmi a una nuova scheda, mi registra direttamente

- [] L'allenatore potrà attraverso una schermata aggiungere giocatori alla sua squadra, inserendo: Nome, Cognome, Anno di nascita. (L'aggiunta di giocatori dovrà essere possibile in qualsiasi momento).
    - [x] layout della pagina
    # layout da completare/migliorare
    - [] aggiunta player nel server
    # non funziona aggiunta player

- [] L'allenatore dovrà poter rimuovere un giocatore dalla lista o poter modificare uno dei dati di quelli inseriti in precedenza.

- [] L'allenatore potrà premere il tasto "fine stagione", il quale mantiene la lista dei giocatori, ma svuota i dati relativi alle convocazioni

- [] L'allenatore potrà fare le convocazioni e quindi inserire una lista di giocatori da convocare alla prossima partita (minino 10 massimo 12). Nella schermata di scelta giocatori dovrà poter vedere:
- [] Per ogni giocatore, a che data risale l'ultima partita giocata
- [] Per ogni giocatore, il numero di partite giocate in quella stagione
- [] Nella convocazione dovrà inserire l'ora, la data e l'indirizzo della palestra dove si giocherà la partita. Confermata la convocazione il server fornirà una stringa di testo che l'allenatore potrà copiare e incollare nell'ipotetico gruppo whatsapp della squadra.
(Esempio del messaggio: Ciao a tutti! La partita sarà il 12/11/2023 in Via dell'Usignolo 4. I convocati sono i seguenti: Carlo, Mario, ... Buona giornata a tutti!).

- [] Tutto il lato client del programma dovrà essere utilizzabile attraverso un'interfaccia grafica (TKinter)

- [] Il codice deve essere commentato per rendere comprensibile ogni sua parte importante a livello logico. 

- [] Deve essere poi presente un file (doc o pdf) che documenta il programma e presenta le sue varie funzionalità

- [] Il programma poi dovrà essere presentato al resto della classe (Lascio a voi scegliere se preparare un ppt oppure no, in ogni caso va mostrato il programma in esecuzione). La documentazione può essere usata nella presentazione.