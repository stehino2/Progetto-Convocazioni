import cv2
import socket
import os
import numpy as np

def main():
    
    #Family address IPV4   //UDP Protocol, send different datagrams, limited dimension
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    host = '127.0.0.1'  
    port = 12345
    buffer_size = 65536 #max datagram dimension

    client_socket.connect((host, port)) ## !

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
            # Invio il frame al server
            client_socket.sendto(buffer, (host, port))

            # Ricevo il frame dal server
            packet, _ = client_socket.recvfrom(buffer_size)
            data = np.frombuffer(packet, dtype=np.uint8)
            received_frame = cv2.imdecode(data, cv2.IMREAD_COLOR)
            
            
            def filtro(numero_filtro, recived_frame):
                if filter == 1:  # gray scale
                    received_frame = cv2.cvtColor(received_frame, cv2.COLOR_BGR2GRAY) 
                    return received_frame
                elif filter == 2: 
                    ksize = (15, 15)
                    received_frame = cv2.blur(received_frame, ksize)  
                    return received_frame
                    
                elif filter == 3:
                    received_frame = cv2.flip(received_frame, 0)
                    return received_frame

                elif filter == 4:
                    #src = cv2.imread(data, cv2.IMREAD_UNCHANGED)

                    # extract red channel
                    red_channel = received_frame[:,:,0]

                    # create empty image with same shape as that of src image
                    red_img = np.zeros(received_frame.shape)

                    #assign the red channel of src to empty image
                    red_img[:,:,0] = red_channel
                    return red_img[:,:,0]

            x = filtro(4)



            # Visualizzo il frame ricevuto dal server
            if received_frame is not None:
                cv2.imshow("Streaming Video - Client", x)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

    cap.release()#end the capture
    client_socket.close()

if __name__ == '__main__':
    main()