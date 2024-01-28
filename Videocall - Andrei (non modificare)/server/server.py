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

def main():
    #udp socket
    server_socket_vid = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket_msg = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 12345
    buffer_size = 65536 #max datagram dimension

    server_socket_vid.bind((host, port))
    print(f"UDP server listening on {host}:{port}...")
    #Like tkinter
    #cv2.namedWindow("Streaming Video", cv2.WINDOW_NORMAL)

    while True:
        try:
            packet, client_address = server_socket_vid.recvfrom(buffer_size) # Ricevo i dati dalla videocamera dei clients
            print(f"Packet received from {client_address}")
            #np = numpy = library to handle multidimensional array
            data = np.frombuffer(packet, dtype=np.uint8) #datatype of the buffer = 8bytes integer (unsigned long integer)
            frame = cv2.imdecode(data, cv2.IMREAD_COLOR) #convert bytes to image

            
            if frame is not None:
                server_socket_vid.sendto(packet, client_address) # Invio il dato al client
                print("Messaggio inviato al client")
        except Exception as e:
            print(f"An error occurred: {e}")
            break

    server_socket_vid.close()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()