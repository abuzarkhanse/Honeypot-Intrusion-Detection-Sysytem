# 🍯 Honeypot Intrusion Detection System

A Python-based **Honeypot Intrusion Detection System** designed to capture, log, and analyze suspicious network activity and potential intrusion attempts.

The system acts as a controlled honeypot environment that records connection attempts and security events, providing useful information such as source IP addresses, timestamps, and geographical information for further analysis.

## 🚀 Features

- 🔐 Captures suspicious network connection attempts
- 📝 Logs intrusion and honeypot activity
- 🌍 Retrieves geographical information associated with IP addresses
- 📊 Provides a dashboard for monitoring captured events
- 📁 Stores collected security logs in CSV and text formats
- 🔎 Supports analysis of source IP addresses and intrusion activity
- ⚙️ Includes multiple honeypot implementations and utilities

## 🛠️ Technologies Used

- **Python**
- **IP Geolocation**
- **CSV / Text-based Logging**
- **Network Monitoring**
- **Data Processing**
- **Dashboard Visualization**

## 📂 Project Structure

```text
Honeypot-Intrusion-Detection-System/
│
├── add_geoip.py              # Adds geographical information to IP data
├── dashboard.py              # Dashboard for monitoring security events
├── honeypot.py                # Main honeypot implementation
├── honeypot_v2.py             # Updated honeypot implementation
├── log_to_csv.py              # Converts/processes logs into CSV format
│
├── honeypot_logs.csv          # Collected honeypot logs
├── honeypot_logs.txt          # Raw activity logs
├── honeypot_logs_geo.csv      # Logs enriched with geolocation data
│
└── README.md
