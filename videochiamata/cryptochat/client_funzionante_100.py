import socket
import threading
#from crypto import encrypt, decrypt, public_key, private_key, serialize_key, deserialize_key

# Funzione che gestisce i messaggi ricevuti dal server
def receive_messages(client_socket):
    try:
        while True:
            #ciphertext = client_socket.recv(1024)
            #message = decrypt(ciphertext, private_key)
            message = client_socket.recv(1024).decode()
            print(message)
    except:
        pass

# Funzione che gestisce i messaggi inviati dal client
def send_messages(client):
    

# Funzione principale
def main():
    # Crea il socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 8080))

    # Scelta del client (creare o entrare in una stanza)
    choice = input("Vuoi creare una stanza o unirti a una stanza? (create/join): \n")
    client.send(choice.encode('utf-8'))

    # Mostra il messaggio di connessione al server
    response = client.recv(1024).decode('utf-8')
    print(response)

    # Nel caso la risposta dal server sia "Sei nella stanza" o "Stanze disponibili"
    if "Sei nella stanza" in response or "Stanze disponibili" in response:
        # Crea il thread per ricevere i messaggi dal server
        receive_thread = threading.Thread(target=receive_messages, args=(client,))
        receive_thread.start()

        # Crea il thread per inviare i messaggi al server
        input_thread = threading.Thread(target=send_messages, args=(client,))
        input_thread.start()

        # Attendi la fine dei thread
        receive_thread.join()
        input_thread.join()

    # Nel caso la risposta dal server sia "Non sei nella stanza"
    else:
        print("Errore nella scelta.")

# Esegue il programma
if __name__ == "__main__":
    main()
