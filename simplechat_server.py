# SimpleChat Chat Room Server
# Written by M.V.Harish Kumar

import socket
from threading import Thread

def listen_client(client_sock):
    while True:
        try:
            msg = client_sock.recv(1024).decode()
        except Exception as e:
            print(f"[!] Error: {e}")
            clients.remove(client_sock)
        else:
            msg = msg.replace(SEP_TOKEN,": ")
            for client in clients:
                client.send(msg.encode())

SERVER_HOST = '0.0.0.0'
SERVER_PORT = 2791
SEP_TOKEN = "<SEP>"

clients = set()

print("Welcome to SimpleChat Chat Room")
print("[*] Initialising Server")


server = socket.socket()
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((SERVER_HOST,SERVER_PORT))
server.listen(7)


print("[*] Server Started")
print(f"[*] Server listening at {SERVER_HOST}:{SERVER_PORT}")

while True:
    csock, caddr = server.accept()
    print(f"[+] Client {caddr} connected")
    clients.add(csock)
    t = Thread(target=listen_client,args=(csock,))
    t.daemon = True
    t.start

for cs in clients:
    cs.close()
server.close()