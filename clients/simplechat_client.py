# SimpleChat Chat Room Clients
# Written by M.V.Harish Kumar
# Language - Python3

import socket
import random
from threading import Thread
from datetime import datetime
from colorama import Fore, Back, init

def listen_msg():
    while True:
        msg = client.recv(1024).decode()
        print("\n" + msg)

init()
colors = [
    Fore.BLUE,
    Fore.CYAN,
    Fore.GREEN,
    Fore.LIGHTBLACK_EX,
    Fore.LIGHTBLUE_EX,
    Fore.LIGHTCYAN_EX,
    Fore.LIGHTGREEN_EX,
    Fore.LIGHTMAGENTA_EX,
    Fore.LIGHTRED_EX,
    Fore.LIGHTWHITE_EX,
    Fore.LIGHTYELLOW_EX,
    Fore.MAGENTA,
    Fore.RED,
    Fore.WHITE,
    Fore.YELLOW
]

client_color = random.choice(colors)

SERVER_HOST = '192.168.0.210'
SERVER_PORT = 2791
SEP_TOKEN = "<SEP>"

client = socket.socket()
print(f"[*] Connecting to {SERVER_HOST}:{SERVER_PORT}")
client.connect((SERVER_HOST,SERVER_PORT))
print("[+] Connected to Chat Room Server\n")

name = input("Enter your name: ")

t = Thread(target=listen_msg)
t.daemon = True
t.start()

while True:
    send_msg = input("\n!? > ")
    if send_msg.lower() == 'q':
        break
    date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    send_msg = f"{client_color}[{date_now}] {name}{SEP_TOKEN}{send_msg}{Fore.RESET}"
    client.send(send_msg.encode())

client.close()