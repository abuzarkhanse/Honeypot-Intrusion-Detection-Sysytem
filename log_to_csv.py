import csv
import re

with open('honeypot_logs.txt', 'r') as log_file:
    lines = log_file.readlines()

with open('honeypot_logs.csv', 'w', newline='') as csvfile:
    fieldnames = ['timestamp', 'ip', 'port', 'username', 'password']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for line in lines:
        match = re.search(r'^(.*?) \| IP: ([\d.]+):(\d+) \| Username: (.*?) \| Password: (.*)', line)
        if match:
            timestamp, ip, port, username, password = match.groups()
            writer.writerow({
                'timestamp': timestamp,
                'ip': ip,
                'port': port,
                'username': username,
                'password': password
            })


