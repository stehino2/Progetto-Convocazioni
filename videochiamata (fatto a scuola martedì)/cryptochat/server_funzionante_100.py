import socket #libreria per l'interfaccia socket
import threading #libbreria per permettere il thread
import random #libreria per generare un numero casuale

# Dizionario per memorizzare le stanze e i relativi client
rooms = {}

###################################################################
#L'uso di f-string è particolarmente utile quando si lavora con stringhe che incorporano variabili o espressioni Python all'interno di esse.
###################################################################

# Funzione per creare il codice della stanza
def create_room():
    room_code = str(random.randint(1, 100))
    return f"Room-{room_code}"

# Funzione per accettare messaggi e inviarli all'altro client
# Funzione per accettare messaggi e inviarli agli altri client nella stessa stanza
def handle_client(client, room_name):
    try:
        # loop per ricevere messaggi dal client nella stanza
        while True:
            message = client.recv(1024).decode('utf-8')
            if not message:
                break

            # Se il messaggio è 'exit', termina il loop
            if message.lower() == 'exit':
                break

            # Invia il messaggio a tutti gli altri client nella stessa stanza
            for other_client in rooms[room_name]:
                if other_client != client:
                    try:
                        other_client.send(message.encode('utf-8'))
                    except:
                        continue

    except:
        # Gestione delle eccezioni in caso di disconnessione del client
        pass
    finally:
        # Rimuove il client dalla stanza
        rooms[room_name].remove(client)
        client.close()

# Funzione principale
def main():

    # Crea il server con la socket TCP
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    #fa il bindingo della porta 8080 e si mette in ascolto di connessioni
    server.bind(('localhost', 8080)) #da modificare in caso non funzioni
    server.listen()

    print("Server in ascolto...")

    # Inizializzo il dizionario delle stanze
    while True:
        client, addr = server.accept() #riceve il client e l'indirizzo del client
        print(f"Connessione accettata da {addr}")

        # Riceve la scelta del client (creare o entrare in una stanza)
        choice = client.recv(1024).decode('utf-8')

        #in base alla scelta crea una nuova stanza o entra in una stanza gia esistente
        if choice == 'create':
            #mi crea la stanza prendone il suo numero
            room_name = create_room()
            rooms[room_name] = [client] #lo aggiunmge al dizionario 
            client.send(f"Sei nella stanza '{room_name}'".encode('utf-8')) #manda al client il nome della stanza
        elif choice == 'join':
            #ti mostra le stanze disponibili
            client.send("Stanze disponibili:".encode('utf-8'))
            for room_name in rooms:
                if len(rooms[room_name]) < 2:
                    client.send(f" - {room_name}".encode('utf-8'))

            client.send("Inserisci il nome della stanza a cui vuoi unirti:".encode('utf-8'))
            room_name = client.recv(1024).decode('utf-8')

            if room_name in rooms and len(rooms[room_name]) < 2:
                rooms[room_name].append(client)
                client.send(f"Sei nella stanza '{room_name}'".encode('utf-8'))
            else:
                client.send("La stanza è piena o non esiste. Creane una nuova.".encode('utf-8'))
        else:
            client.send("Scelta non valida.".encode('utf-8'))

        # Avvia un thread per gestire il client nella sua stanza
        thread = threading.Thread(target=handle_client, args=(client, room_name))
        thread.start()

if __name__ == "__main__":
    main()
