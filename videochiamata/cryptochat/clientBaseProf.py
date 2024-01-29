"""
import socket
import cv2 #libreria open cv ci aiuta per lavorare con i video
import numpy  as np #ci permette di lavorare con array multidimensionali
#pip install opencv-python
#pip install numpy

def main(): 

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    host = "127.0.0.1"
    port = 11386

    cap = cv2.VideoCapture(0)# 0 vuol dire automaticamente che mi prende la telecamera

    while cap.isOpened():
        #bool image
        ret, frame = cap.read() #variabile booleana che mi dice se l'operazione di cattura è avvenuta con successo frame invece mi rappresenta l'immagine
        frame = cv2.resize (frame, (640,480)) #gli passo l'immagine insieme a una tupla che contiene i dati della dimensione dell'immagine
        #BOOL
        encoded , buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY,50])#encoded booleano mi nserve per vedere se l'operazione è andata a buon fine
        
        #guardo se è inferiore alla massima lughezza
        if len(buffer) > 65536:
            print("Frame too long")
        else:
            client_socket.sendto(buffer,(host,port))

    cap.release()
    client_socket.close()

if __name__ == "__main__":
    main()
"""
import cv2
import socket
import os

def main():
    #Family address IPV4   //UDP Protocol, send different datagrams, limited dimension
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    host = '127.0.0.1'  
    port = 11500

    video_path = 'video.mp4'

    cap = cv2.VideoCapture(video_path)  #  #0 = video camera ; path_to_video
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
            client_socket.sendto(buffer, (host, port))#send the data

    cap.release()#end the capture
    client_socket.close()

if __name__ == '__main__':
    main()