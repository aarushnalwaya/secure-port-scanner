import socket
import ssl

HOST = "127.0.0.1"
PORT = 5000

context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    secure_client = context.wrap_socket(client, server_hostname=HOST)

    secure_client.connect((HOST, PORT))

    target = input("Enter target IP: ")
    start_port = input("Start port: ")
    end_port = input("End port: ")

    message = f"SCAN {target} {start_port} {end_port}"

    secure_client.send(message.encode())

    result = secure_client.recv(4096).decode()

    print("\nScan Results:")
    print(result)

except Exception as e:
    print("Error:", e)

finally:
    secure_client.close()