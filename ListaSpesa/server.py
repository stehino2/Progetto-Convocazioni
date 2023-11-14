from http.server import BaseHTTPRequestHandler, HTTPServer
import json

hostName = "127.0.0.1"
serverPort = 8080

# Dizionario per la lista della spesa
lista_spesa = []
# Dizionario per tenere traccia delle richieste di ciascun utente
user_requests = {}

class ServerHandler(BaseHTTPRequestHandler):

    def set_headers(self, ctype):
        self.send_response(200)
        self.send_header('Content-type', ctype)
        self.end_headers()

    def write_response(self, content):
        self.wfile.write(bytes(content, "utf-8"))

    def do_GET(self):
        if self.path == "/lista":
            # Gestisci la richiesta per visualizzare la lista della spesa
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(lista_spesa).encode())
        elif self.path == "/richieste":
            # Gestisci la richiesta per visualizzare il conteggio delle richieste
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            richieste_totali = sum(user_requests.values())
            username = self.headers.get('Username')
            richieste_utente = user_requests.get(username, 0)
            response = {
                "richieste totali": richieste_totali,
                "mie richieste": richieste_utente
            }
            self.wfile.write(json.dumps(response).encode())

    def do_POST(self):
        if self.path == "/aggiungi":
            # Gestisci la richiesta per aggiungere un elemento alla lista della spesa
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            item = json.loads(post_data.decode('utf-8'))
            lista_spesa.append(item)

            # Registra la richiesta dell'utente
            username = self.headers.get('Username')
            if username:
                user_requests[username] = user_requests.get(username, 0) + 1

            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write("Elemento aggiunto alla lista della spesa.".encode())

if __name__ == "__main__": 
    # Esegui il server e mantienilo in ascolto
    webServer = HTTPServer((hostName, serverPort), ServerHandler)
    print("Server started")

    try:
        # Serve per fermare il server quando necessario
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("\nServer stopped")
