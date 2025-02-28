import socket
import threading
import datetime

HOST = '127.0.0.1'
PORT = 12345

clients = {}
lock = threading.Lock()

def handle_client(client_socket, nickname):
    try:
        while True:
            message = client_socket.recv(1024).decode("utf-8")
            if not message:
                break
            timestamp = datetime.datetime.now().strftime("%H:%M:%S")
            formatted_message = f"[{timestamp}] {nickname}: {message}"
            print(formatted_message)
            broadcast(formatted_message, client_socket)
    except ConnectionResetError:
        print(f"{nickname} s-a deconectat.")
    finally:
        with lock:
            del clients[client_socket]
        client_socket.close()

def broadcast(message, sender_socket):
    with lock:
        for client in list(clients.keys()):
            if client != sender_socket:
                try:
                    client.send(message.encode("utf-8"))
                except:
                    client.close()
                    del clients[client]

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"Serverul pornit {HOST}:{PORT}")

    while True:
        try:
            client_socket, addr = server.accept()
            print(f"Conexiune nouă {addr}")

            client_socket.send("Introdu-ți numele: ".encode("utf-8"))
            nickname = client_socket.recv(1024).decode("utf-8").strip()

            if not nickname:
                client_socket.close()
                continue

            with lock:
                clients[client_socket] = nickname

            print(f"{nickname} s-a conectat!")
            broadcast(f"{nickname} s-a conectat!", client_socket)

            thread = threading.Thread(target=handle_client, args=(client_socket, nickname))
            thread.start()
        except Exception as e:
            print(f"Server error: {e}")

if __name__ == "__main__":
    start_server()
