# CONSEGNA

Scrivere in python dei client che permettano a dei diversi utenti di effettuare una videochiamata tra loro.
Oltre alla videochiamata il client deve promettere ai due utenti di usare una chat testuale tra di loro

La videochiamata deve permette di inserire 3 filtri (Open CV e Numpy):
- Reds, rendere l'immagine rossa
- Upside down, girare a testa in giù l'immagine
- Blurr, sfuochi l'immagine

Obbligatorio: 2 Client che interagiscono tra loro con la videochiamata e con la chat + 3 filtri scritti sopra.

Extra: Più client che videochiamano e chattano + Aggiunta di uno o più filtri a piacere. 

# TODO LIST

link utile: https://www.youtube.com/watch?v=4DfPQdC8L80
altro link utile: https://www.youtube.com/watch?v=jGYNFssXiAQ
video gui: https://www.youtube.com/watch?v=oLxFqpUbaAE #TkinterDesigner
https://github.com/ParthJadhav/Tkinter-Designer/blob/master/docs/instructions.md

Usiamo di sicuro le socket, va sicuramente cryptata (se abbiamo tempo e voglia)
Fare due connessioni diverse, tcp invio i messaggi mentre udp invio i dati della fotocamera
teoricamente 5 threads
    2 per inviare e ricevere il video
    2 per inviare e ricere i messaggi
    1 per far accedere più client contemporaneamente (extra teoricamente)

[] videochiamata:
    [] client:
        invia i dati della fotocamera e i messaggi al server e riceve la risposta sempre dal server
    [] server: 
        quando il client invia un messaggio o i dati della fotocamera, passa prima per il server e poi passa per il client
        
[] chat:
    [] client:

    [] server:
        [] magari tiene conto della cronologia dei messaggi, solo nella sessione però, quando viene eliminata la sessione
           la chat viene eliminata

[] filtri:
    [] reds:

    [] upside down:

    [] blurr:
