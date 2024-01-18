import socket
import cv2 #libreria open cv ci aiuta per lavorare con i video
import numpy  as np #ci permette di lavorare con array multidimensionali
#pip install opencv-python
#pip install numpy

def send():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    hostC = "172.30.4.26"
    portC = 11386

    capC = cv2.VideoCapture(0)# 0 vuol dire automaticamente che mi prende la telecamera

    while capC.isOpened():
        #bool image
        retC, frameC = capC.read() #variabile booleana che mi dice se l'operazione di cattura è avvenuta con successo frame invece mi rappresenta l'immagine
        frameC = cv2.resize (frameC, (640,480)) #gli passo l'immagine insieme a una tupla che contiene i dati della dimensione dell'immagine
        #BOOL
        encodedC , bufferC = cv2.imencode('.jpg', frameC, [cv2.IMWRITE_JPEG_QUALITY,50])#encoded booleano mi nserve per vedere se l'operazione è andata a buon fine
        
        #guardo se è inferiore alla massima lughezza
        if len(bufferC) > 65536:
            print("Frame too long")
        else:
            client_socket.sendto(bufferC,(hostC,portC))

    capC.release()
    client_socket.close()


def recive():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    hostS = "172.30.4.27"
    portS = 11386
    buffer_sizeS = 65536

    cv2.namedWindow("Streaming Video", cv2.WINDOW_NORMAL)

    server_socket.bind((hostS,portS))
    print("server listening")
    while True:
        try: 
            packetS,_ = server_socket.recvfrom(buffer_sizeS)
            print("packet received")
            dataS = np.frombuffer(packetS, dtype = np.uint8)
            frameS = cv2.imdecode(dataS, cv2.IMREAD_COLOR)
            if frameS is not None:
                cv2.imshow("Streaming Video", frameS)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        except Exception as e:
            print(f"Ab errir iccured; {e}")
            break

    server_socket.close()
    cv2.destroyAllWindows()

def main(): 
    send()
    recive()

if __name__ == "__main__":
    main()