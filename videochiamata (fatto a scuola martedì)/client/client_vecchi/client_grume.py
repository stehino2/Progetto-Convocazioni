import cv2
import socket
import os
import numpy as np
import threading

def sender(socket,host,port):

    cap = cv2.VideoCapture(0)  #  #0 = video camera ; path_to_video
    #cap = capture
    #cv2 = library to handle images
    
    while cap.isOpened():
        #ret = boolean value; frame is the image
        ret, frame = cap.read()

        #The frame can be bigger than the buffer size. To avoid that we resize it. 
        frame = cv2.resize(frame, (640, 480))
        #encoded is a bool
        encoded, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 50])
        if len(buffer) > 65536:#max dim of the buffer
            print("The frame is too large to be sent over UDP")
        else:
            socket.sendto(buffer, (host, port))#send the data

    cap.release()#end the capture
    socket.close()

def receiver(socket,host,port):

    #(CONNESSIONE) parte dove gestisco la connessione tra il server e il client
   
    buffer_size = 65536 #max datagram dimension

    #socket.bind((host, port)) #mi serve per fare il binding 
    print(f"UDP server listening on {host}:{port}...")
    cv2.namedWindow("Streaming Video", cv2.WINDOW_NORMAL) #apro la finestra

    while True:
        try:
            packet, _ = socket.recvfrom(buffer_size)
            print("Packet received")
            #np = numpy = library to handle multidimensional array
            data = np.frombuffer(packet, dtype=np.uint8) #datatype of the buffer = 8bytes integer (unsigned long integer)
            frame = cv2.imdecode(data, cv2.IMREAD_COLOR) #convert bytes to image
            if frame is not None:
                cv2.imshow("Streaming Video", frame)#show image, Streaming Video window name
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        except Exception as e:
            print(f"An error occurred: {e}")
            break

    socket.close()
    cv2.destroyAllWindows()

def main():

    #(CONNESSIONE) parte dove gestisco la connessione tra il server e il client
    video_socket= socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #creo la socket per ricevere un informazione
    host = '127.0.0.1'  
    port = 12345 #porta per inviare un informazione
    video_socket.connect((host, port)) ## !

    #video_socket.bind((host, port)) #mi serve per fare il binding

# Crea il thread per ricevere il video dal server
    receive_thread = threading.Thread(target=receiver, args=(video_socket,host,port))
    receive_thread.start()

    # Crea il thread per inviare il video al server
    send_thread = threading.Thread(target=sender, args=(video_socket,host,port))
    send_thread.start()

    # Attendi la fine dei thread
    receive_thread.join()
    send_thread.join()
     

if __name__ == '__main__':
    main()