import cv2
import socket
import os
import threading
import numpy as np

#global filter 
#global buffer_size 
#buffer_size = 65336

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

def send_video(client_socket_video, cap, host, port,buffer_size):
    #ret = boolean value; frame is the image
    while cap.isOpened():
        ret, frame = cap.read()

        #The frame can be bigger than the buffer size. To avoid that we resize it. 
        frame = cv2.resize(frame, (640, 480))
        #encoded is a bool
        encoded, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 50])

        if len(buffer) > buffer_size:#max dim of the buffer
            print("The frame is too large to be sent over UDP")
        else:
            # Invio il frame al server
            client_socket_video.sendto(buffer, (host, port))

def receive_video(client_socket_video, cap, buffer_size):
    #cv2.namedWindow("Streaming Video", cv2.WINDOW_NORMAL) #apro la finestra
    while True:
        try:
            # Ricevo il frame dal server
            packet, _ = client_socket_video.recvfrom(buffer_size)
            data = np.frombuffer(packet, dtype=np.uint8)
            received_frame = cv2.imdecode(data, cv2.IMREAD_COLOR)

            # Visualizzo il frame ricevuto dal server
            if received_frame is not None:
                cv2.imshow("Streaming Video - Client", received_frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break #break
        except Exception as e:
            print(f"An error occured: {e}")
            break #break

def main():
    #socket e indirizzi
    client_socket_vid = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #soc
    client_socket_msg = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'  
    port = 12345
    buffer_size = 65536 #max datagram dimension

    client_socket_msg.connect(('localhost', 8080)) ##!
    client_socket_vid.connect((host, port)) ## !

    cap = cv2.VideoCapture(0)  #  #0 = video camera ; path_to_video

    #PARTE USER EXPERIENCE CIÒ CHE APPARE NEL TERMINALE
    ####################################
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

        # Crea il thread per inviare il video al server
        input_vid_thread = threading.Thread(target=send_video, args=(client_socket_vid, cap, host, port,buffer_size))
        input_vid_thread.start()

        # Crea il thread per ricevere il video dal server
        receive_vid_thread = threading.Thread(target=receive_video, args=(client_socket_vid, cap, buffer_size))
        receive_vid_thread.start()

        # Crea il thread per inviare i messaggi al server
        input_msg_thread = threading.Thread(target=send_messages, args=(client_socket_msg,))
        input_msg_thread.start()



        # Attendi la fine dei thread
        receive_msg_thread.join()
        receive_vid_thread.join()
        input_msg_thread.join()
        input_vid_thread.join()

        cap.release()#end the capture
        

    # Nel caso la risposta dal server sia "Non sei nella stanza"
    else:
        print("Errore nella scelta.")

    client_socket_vid.close()
    client_socket_msg.close()



if __name__ == '__main__':
    main()

