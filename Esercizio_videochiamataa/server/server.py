import cv2
import numpy as np
import socket



######################## variabili
nomi = [] # array di nomi gia utilizzati



def main():
    #udp socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    host = '127.0.0.1'
    port = 11500
    buffer_size = 65536 #max datagram dimension

    server_socket.bind((host, port))
    print(f"UDP server listening on {host}:{port}...")
    #Like tkinter
    
    

if __name__ == '__main__':
    main()
