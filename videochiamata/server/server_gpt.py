import cv2
import threading
import random
import numpy as np
import socket

# Dizionario per memorizzare le stanze e i relativi client
rooms = {}

# Funzione per creare il codice della stanza
def create_room():
    room_code = str(random.randint(1, 100))
    return f"Room-{room_code}"

# Funzione per accettare messaggi e inviarli agli altri client nella stessa stanza
def handle_client(clientTCP, clientUDP, room_name, server_socket_vid, addrUDP):
    try:
        # loop per ricevere messaggi dal client nella stanza
        while True:
            message = clientTCP.recv(1024).decode('utf-8')
            
            # Ricezione del flusso video tramite UDP
            data, _ = server_socket_vid.recvfrom(65536)
            frame = cv2.imdecode(np.frombuffer(data, dtype=np.uint8), cv2.IMREAD_COLOR)
            
            if not message:
                break

            # Se il messaggio è 'exit', termina il loop
            if message.lower() == 'exit':
                break

            # Invia il messaggio a tutti gli altri client nella stessa stanza
            for other_client in rooms[room_name]:
                if other_client != clientTCP:
                    try:
                        server_socket_vid.sendto(data, addrUDP)  # Invio il dato al client
                        other_client.send(message.encode('utf-8'))
                    except:
                        continue

    except Exception as e:
        # Gestione delle eccezioni in caso di disconnessione del client
        print(f"An error occurred in handle_client: {e}")
    finally:
        # Rimuove il client dalla stanza
        rooms[room_name].remove(clientTCP)
        clientTCP.close()

def main():
    # UDP socket
    server_socket_vid = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket_msg = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 12345
    port2 = 8080
    buffer_size = 65536  # max datagram dimension

    server_socket_msg.bind((host, port2))  # faccio il binding per i messaggi
    server_socket_msg.listen()
    print(f"TCP server listening on {host}:{port2}...")
    server_socket_vid.bind((host, port))
    print(f"UDP server listening on {host}:{port}...")

    while True:
        clientTCP, addrTCP = server_socket_msg.accept()  # riceve il client e l'indirizzo del client
        print(f"Connessione accettata da {addrTCP}")
        clientUDP, addrUDP = server_socket_vid.recvfrom(buffer_size)  # Ricevo i dati dalla videocamera dei clients
        print(f"Packet received from {addrUDP}")

        # Riceve la scelta del client (creare o entrare in una stanza)
        choice = clientTCP.recv(1024).decode('utf-8')

        # in base alla scelta crea una nuova stanza o entra in una stanza gia esistente
        if choice == 'create':
            # mi crea la stanza prendone il suo numero
            room_name = create_room()
            rooms[room_name] = [clientTCP]  # lo aggiunge al dizionario
            clientTCP.send(f"Sei nella stanza '{room_name}'".encode('utf-8'))  # manda al client il nome della stanza
        elif choice == 'join':
            # ti mostra le stanze disponibili
            clientTCP.send("Stanze disponibili:".encode('utf-8'))
            for room_name in rooms:
                if len(rooms[room_name]) < 2:
                    clientTCP.send(f" - {room_name}".encode('utf-8'))

            clientTCP.send("\n \nInserisci il nome della stanza a cui vuoi unirti:".encode('utf-8'))
            room_name = clientTCP.recv(1024).decode('utf-8')

            if room_name in rooms and len(rooms[room_name]) < 2:
                rooms[room_name].append(clientTCP)
                clientTCP.send(f"\nSei nella stanza '{room_name}'".encode('utf-8'))
            else:
                clientTCP.send("\nLa stanza è piena o non esiste. Creane una nuova.".encode('utf-8'))
        else:
            clientTCP.send("\nScelta non valida.".encode('utf-8'))

        # Avvia un thread per gestire il client nella sua stanza
        thread = threading.Thread(target=handle_client, args=(clientTCP, clientUDP, room_name, server_socket_vid, addrUDP))
        thread.start()

    # Chiusura dei socket e uscita dal programma
    server_socket_msg.close()
    server_socket_vid.close()

if __name__ == '__main__':
    main()
