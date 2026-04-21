NAME:SRN
ABHINAV:PES2UG24AM007
AARUSH:PES2UG24AM006
CHANDANA:PES2UG24AM043
# Secure Multi-Client Port Scanner with SSL

## Description
This project implements a secure multi-client port scanner using socket programming and SSL/TLS encryption. Multiple clients can connect to the server and request port scanning on a target system.

## Features
- Multi-client support using threading
- SSL/TLS encrypted communication
- Port scanning using TCP connect method
- Service detection for common ports
- Error handling and input validation

## Technologies Used
- Python
- Socket Programming
- SSL/TLS
- Multithreading

## How to Run

### Step 1: Start Server
python server.py

### Step 2: Run Client
python client.py in terminal

python ui_client.py for UI

### Step 3: Enter Input
Enter target IP: 127.0.0.1
Start port: 1
End port: 500

## Example Output
80 OPEN (HTTP)
443 OPEN (HTTPS)
135 OPEN (RPC)
445 OPEN (SMB)


---

## 📊 Performance Evaluation

| Ports Scanned | Time Taken |
|--------------|----------|
| 1–100 | ~0.5 sec |
| 1–500 | ~0.58 sec |
| 1–1000 | ~0.78 sec |

### Observations
- Scanning time increases with number of ports
- Multithreading improves speed significantly
- System handles multiple clients efficiently
- SSL adds minor overhead but ensures security

---

## ⚡ Optimization and Fixes
- Added timeout optimization for faster scanning
- Handled invalid inputs
- Managed client disconnections gracefully
- SSL error handling implemented
- Improved stability using exception handling

---

## 🎯 Expected Outcome
- Detect open ports on local and remote systems
- Identify common services
- Support secure and concurrent scanning

---
