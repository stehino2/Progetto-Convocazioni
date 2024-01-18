import cv2
import socket
import os
import numpy as np
import threading

######################## json 
info_messaggio = {
    "nome": "",
    "messaggio": ""
}

def codeice():
    pass



def main():
    #Family address IPV4   //UDP Protocol, send different datagrams, limited dimension
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    host = '172.30.4.27'  
    port = 11386
    buffer_size = 65536 #max datagram dimension
    

    cap1 = cv2.VideoCapture(0)  #  #0 = video camera ; path_to_video
    #cap = capture
    #cv2 = library to handle images
    
    def recive_video():
        while True:
            try:
                packet, _ = client_socket.recvfrom(buffer_size)
                print("Packet received")
                #np = numpy = library to handle multidimensional array
                data = np.frombuffer(packet, dtype=np.uint8) #datatype of the buffer = 8bytes integer (unsigned long integer)
                frame = cv2.imdecode(data, cv2.IMREAD_COLOR) #convert bytes to image
                if frame is not None:
                    cv2.imshow("Streaming Video", frame)#show image, Streaming Video window name
                    cv2.imshow("Streaming video 2", frame)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
            except Exception as e:
                print(f"An error occurred: {e}")
                break

    client_socket.close()
    cv2.destroyAllWindows()
    
    #######################################################
    #upn thread deve fare seta roba
    ######################################################
    def invio_immagine():
        while cap1.isOpened():
            #ret = boolean value; frame is the image
            ret, frame = cap1.read()


            #The frame can be bigger than the buffer size. To avoid that we resize it. 
            frame = cv2.resize(frame, (640, 480))
            #encoded is a bool
            encoded, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 50])
            if len(buffer) > 65536:#max dim of the buffer
                print("The frame is too large to be sent over UDP")
            else:
                client_socket.sendto(buffer, (host, port))#send the data

    
    #######################################################
    # un thread deve ricevere
    #######################################################
    def ricezzione_immagine():
        cv2.namedWindow("Streaming Video", cv2.WINDOW_NORMAL)

        while True:
            try:
                packet, _ = client_socket.recvfrom(buffer_size)
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
    
    invio_thread = threading.Thread(target=invio_immagine, args=())
    invio_thread.daemon = True #Imposta il thread come daemon per terminarlo quando il programma termina
    invio_thread.start()
    
    ricezzione_thread = threading.Thread(target=ricezzione_immagine, args=())
    ricezzione_thread.daemon = True #Imposta il thread come daemon per terminarlo quando il programma termina
    ricezzione_thread.start()

    
    cap1.release()#end the capture
    client_socket.close()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
