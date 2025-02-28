import socket
import threading

HOST = '127.0.0.1'
PORT = 12345

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            if not message:
                break
            print(message)
        except ConnectionResetError:
            print("Conexiune pierdută.")
            break
    client_socket.close()

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        client.connect((HOST, PORT))

        server_message = client.recv(1024).decode("utf-8")
        print(server_message)

        nickname = input("Introdu-ți numele: ").strip()
        client.send(nickname.encode("utf-8"))

        threading.Thread(target=receive_messages, args=(client,)).start()

        while True:
            message = input()
            if message.lower() == 'iesire':
                break
            client.send(message.encode("utf-8"))

    except ConnectionResetError:
        print("Serverul nu este disponibil.")
    finally:
        client.close()

if __name__ == "__main__":
    start_client()
