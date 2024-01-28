import cv2
import socket
import os
import threading
import numpy as np

global filter 

# Dimensione massima del buffer
global buffer_size 
buffer_size = 65336

def user_experience(client_socket_vid, client_socket_msg):
    
    # Scelta del client (creare o entrare in una stanza)
    choice = input("Vuoi creare una stanza o unirti a una stanza? (create/join): \n")
    client_socket_msg.send(choice.encode('utf-8'))

    # Mostra il messaggio di connessione al server
    response = client_socket_msg.recv(1024).decode('utf-8')
    print(response)

    # Nel caso la risposta dal server sia "Sei nella stanza" o "Stanze disponibili"
    if "Sei nella stanza" in response or "Stanze disponibili" in response:
        # Crea il thread per ricevere i messaggi dal server
        receive_msg_thread = threading.Thread(target=receive_messages, args=(client_socket_msg,))
        receive_msg_thread.start()

        # Crea il thread per ricevere il video dal server
        receive_vid_thread = threading.Thread(target=receive_video, args=(client_socket_vid,))
        receive_vid_thread.start()

        # Crea il thread per inviare i messaggi al server
        input_msg_thread = threading.Thread(target=send_messages, args=(client_socket_msg,))
        input_msg_thread.start()

        # Crea il thread per inviare il video al server
        input_vid_thread = threading.Thread(target=send_video, args=(client_socket_msg,))
        input_vid_thread.start()

        # Attendi la fine dei thread
        receive_msg_thread.join()
        receive_vid_thread.join()
        input_msg_thread.join()
        input_msg_thread.join()

    # Nel caso la risposta dal server sia "Non sei nella stanza"
    else:
        print("Errore nella scelta.")

def send_messages(client_socket):
    try:
        while True:
            message = input() #inserisci il messaggio
            client_socket.send(message.encode()) #te lo codifica e lo manda al server
    except EOFError:
        pass


def receive_messages(client_socket):
    try:
        while True:
            message = client_socket.recv(1024).decode() #riceve il messaggio lo decodifica 
            print(message) #stampa succesivamente il messaggio
    except:
        pass

# Funzione per inviare il frame della videocamera al server
def send_video(client_socket_video, cap, host, port):
    while cap.isOpened():
        ret, frame = cap.read()

        frame = cv2.resize(frame, (640, 480))
        encoded, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 50])

        # Controllo se il buffer supera il valore massimo prestabilito
        if len(buffer) > buffer_size:
            print("The frame is too large to be sent over UDP")
        else:
            # Invio il frame al server
            client_socket_video.sendto(buffer, (host, port))

# Funzione per ricevere il frame della videocamera dal server
def receive_video(client_socket_video, cap):
    while True:
        try:
            # Ricevo il frame dal server
            packet, _ = client_socket_video.recvfrom(buffer_size)
            data = np.frombuffer(packet, dtype=np.uint8)
            received_frame = cv2.imdecode(data, cv2.IMREAD_COLOR)

            """
            if (filter == 1): #gray scale
                recived_frame = cv2.cvtColor(recived_frame, cv2.COLOR_BGR2GRAY) 
            if (filter == 2): 
                ksize = (15, 15)
                recived_frame = cv2.blur(recived_frame, ksize)  
            if (filter == 3):
                recived_frame = cv2.flip(recived_frame, 0)
            """

            # Visualizzo il frame ricevuto dal server
            if received_frame is not None:
                cv2.imshow("Streaming Video - Client", received_frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        except Exception as e:
            print(f"An error occured: {e}")
            break

def main():
    """
    Inizializziamo una socket UDP per il video,
    questo perché non ci interessa se durante l'invio
    dei dati perdiamo dei pacchetti, mentre d'altra parte
    inizializiamo una socket TCP per i messaggi perché
    non vogliamo perdere pacchetti per strada
    """
    client_socket_video = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket_chat = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'  
    port = 12345

    #PARTE USER EXPERIENCE CIÒ CHE APPARE NEL TERMINALE
    ####################################
    client_socket_video.connect((host, port))

    # Catturiamo il video della videocamera
    cap = cv2.VideoCapture(0)

    """
    Avviamo i threads per permettere al client di inviare
    il frame della videocamera al server, per poi successivamente
    reinviarli al client
    """
    send_thread = threading.Thread(target = send_video, args = (client_socket_video, cap, host, port))
    receive_thread = threading.Thread(target = receive_video, args = (client_socket_video, cap))

    # Avviamo i due threads
    send_thread.start()
    receive_thread.start()

    # Aspettiamo che i due threads terminino
    send_thread.join()
    receive_video.join()
        
    # Rilasciamo la videocamera e chiudiamo la socket del client
    cap.release()
    client_socket_video.close()

if __name__ == '__main__':
    main()