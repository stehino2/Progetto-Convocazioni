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

# Funzione per gestire la connessione TCP di un singolo client
def handle_tcp_client(clientTCP, server_socket_vid, addrUDP):
    try:
        while True:
            message = clientTCP.recv(1024).decode('utf-8')
            
            # Ricezione del flusso video tramite UDP
            data, _ = server_socket_vid.recvfrom(65536)
            frame = cv2.imdecode(np.frombuffer(data, dtype=np.uint8), cv2.IMREAD_COLOR)
            
            if not message:
                break

            if message.lower() == 'exit':
                break

            room_name = None
            # Trova la stanza del client
            for room, clients in rooms.items():
                if clientTCP in clients:
                    room_name = room
                    break

            if room_name:
                # Invia il messaggio a tutti gli altri client nella stessa stanza
                for other_client in rooms[room_name]:
                    if other_client != clientTCP:
                        try:
                            server_socket_vid.sendto(data, addrUDP)
                            other_client.send(message.encode('utf-8'))
                        except:
                            continue
            else:
                print("Errore: client non trovato nella stanza.")

    except Exception as e:
        print(f"An error occurred in handle_tcp_client: {e}")
    finally:
        clientTCP.close()

# Funzione per gestire la connessione TCP e UDP di un client
def handle_client_connections(server_socket_msg, server_socket_vid):
    while True:
        clientTCP, addrTCP = server_socket_msg.accept()
        print(f"Connessione accettata da {addrTCP}")
        clientUDP, addrUDP = server_socket_vid.recvfrom(65536)
        print(f"Packet received from {addrUDP}")

        choice = clientTCP.recv(1024).decode('utf-8')

        if choice == 'create':
            room_name = create_room()
            rooms[room_name] = [clientTCP]
            clientTCP.send(f"Sei nella stanza '{room_name}'".encode('utf-8'))
        elif choice == 'join':
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
        thread = threading.Thread(target=handle_tcp_client, args=(clientTCP, server_socket_vid, addrUDP))
        thread.start()

# Funzione principale
def main():
    server_socket_msg = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket_vid = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    host = '127.0.0.1'
    port_msg = 12345
    port_vid = 8080

    server_socket_msg.bind(('localhost', port_msg))
    server_socket_msg.listen()
    print(f"TCP server listening on {'localhost'}:{port_msg}...")
    
    server_socket_vid.bind((host, port_vid))
    print(f"UDP server listening on {host}:{port_vid}...")

    # Avvia un thread per gestire le connessioni TCP e UDP dei client
    thread = threading.Thread(target=handle_client_connections, args=(server_socket_msg, server_socket_vid))
    thread.start()

    thread.join()

    # Chiusura dei socket e uscita dal programma
    server_socket_msg.close()
    server_socket_vid.close()

if __name__ == '__main__':
    main()
