import socket
import logging
from datetime import datetime

# === Configuration ===
HOST = '0.0.0.0'
PORT = 2222
LOGFILE = 'honeypot_logs.txt'
MAX_ATTEMPTS = 3

# === Logging Setup ===
logging.basicConfig(
    filename=LOGFILE,
    level=logging.INFO,
    format='%(asctime)s | %(message)s',
)

def log_attempt(ip, port, username, password):
    logging.info(f"IP: {ip}:{port} | Username: {username} | Password: {password}")

def handle_client(client, addr):
    ip, port = addr
    print(f"[!] Connection from {ip}:{port}")

    try:
        client.sendall(b"SSH-2.0-OpenSSH_8.4\r\n")

        for i in range(MAX_ATTEMPTS):
            client.sendall(b"Username: ")
            username = client.recv(1024).strip().decode()

            client.sendall(b"Password: ")
            password = client.recv(1024).strip().decode()

            log_attempt(ip, port, username, password)
            client.sendall(b"Access denied\r\n")

        client.close()
        print(f"[+] Closed connection from {ip}")

    except Exception as e:
        print(f"[-] Error handling {ip}:{port} -> {e}")
        client.close()

def start_honeypot():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"[+] Honeypot running on port {PORT}...")

    while True:
        client, addr = server.accept()
        handle_client(client, addr)

if __name__ == "__main__":
    start_honeypot()
