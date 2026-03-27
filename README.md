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
python client.py

### Step 3: Enter Input
Enter target IP: 127.0.0.1
Start port: 1
End port: 500

## Example Output
80 OPEN (HTTP)
443 OPEN (HTTPS)
135 OPEN (RPC)
445 OPEN (SMB)


## Performance
- Multithreading reduces scan time significantly
- Supports multiple concurrent clients
