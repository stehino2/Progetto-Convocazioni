import cv2
import numpy as np
import socket

def main():
    #udp socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    host = '127.0.0.1'
    port = 11500
    buffer_size = 65536 #max datagram dimension

    server_socket.bind((host, port))
    print(f"UDP server listening on {host}:{port}...")
    #Like tkinter
    cv2.namedWindow("Streaming Video", cv2.WINDOW_NORMAL)


    while True:
        try:
            packet, _ = server_socket.recvfrom(buffer_size)
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

    server_socket.close()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()