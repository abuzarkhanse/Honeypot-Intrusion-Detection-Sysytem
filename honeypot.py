import socket
import logging
from datetime import datetime

# === Configuration ===
HOST = '0.0.0.0'     # Listen on all network interfaces
PORT = 2222          # Port to mimic SSH (not 22 to avoid conflicts)
LOGFILE = 'honeypot_logs.txt'

# === Logging Setup ===
logging.basicConfig(
    filename=LOGFILE,
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
)

# === Start Server ===
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)
print(f"[+] Honeypot running on port {PORT}...")

while True:
    client, addr = server.accept()
    ip, port = addr
    print(f"[!] Connection from {ip}:{port}")
    
    try:
        client.sendall(b"SSH-2.0-OpenSSH_8.4\r\n")
        client.sendall(b"Username: ")
        username = client.recv(1024).strip().decode()

        client.sendall(b"Password: ")
        password = client.recv(1024).strip().decode()

        # Log the attempt
        logging.info(f"Attempt from {ip}:{port} | Username: {username} | Password: {password}")
        print(f"[+] Logged attempt from {ip} with user: {username}")

        # Respond with fake rejection
        client.sendall(b"Access denied\r\n")
        client.close()

    except Exception as e:
        print(f"[-] Error: {e}")
        client.close()


