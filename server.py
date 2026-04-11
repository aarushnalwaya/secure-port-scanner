# import socket
# import ssl
# import threading
# import time
# from services import detect_service

# HOST = "0.0.0.0"
# PORT = 5000

# def scan_ports(target, start_port, end_port):
#     results = []
#     threads = []
#     lock = threading.Lock()
#     start_time = time.time()

#     # scanning logic

#     end_time = time.time()
#     print("Time taken:", end_time - start_time)

    

# def scan_ports(target, start_port, end_port):
#     start_time = time.time()   # START HERE

#     results = []
#     threads = []
#     lock = threading.Lock()

#     def scan_port(port):
#         try:
#             s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#             s.settimeout(0.5)

#             if s.connect_ex((target, port)) == 0:
#                 service = detect_service(port)
#                 with lock:
#                     results.append(f"{port} OPEN ({service})")

#             s.close()
#         except:
#             pass

#     for port in range(start_port, end_port + 1):
#         thread = threading.Thread(target=scan_port, args=(port,))
#         threads.append(thread)
#         thread.start()

#     for thread in threads:
#         thread.join()

#     end_time = time.time()   # END HERE

#     print("Time taken:", round(end_time - start_time, 3), "seconds")

#     return results


# def handle_client(conn, addr):
#     print("Client connected:", addr)

#     try:
#         data = conn.recv(1024).decode()

#         if not data:
#             return

#         parts = data.split()

#         # Input validation
#         if len(parts) != 4:
#             conn.send("Invalid input format".encode())
#             return

#         target = parts[1]
#         start_port = int(parts[2])
#         end_port = int(parts[3])

#         if start_port < 0 or end_port > 65535:
#             conn.send("Invalid port range".encode())
#             return

#         results = scan_ports(target, start_port, end_port)

#         if not results:
#             conn.send("No open ports found".encode())
#         else:
#             conn.send("\n".join(results).encode())

#     except ssl.SSLError:
#         print("SSL handshake failed")

#     except Exception as e:
#         conn.send(f"Error: {str(e)}".encode())

#     finally:
#         conn.close()
#         print("Client disconnected")


# # SSL Setup
# context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
# context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")

# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.bind((HOST, PORT))
# server.listen(5)

# print("Secure Port Scanner Server Running...")

# with context.wrap_socket(server, server_side=True) as secure_server:
#     while True:
#         conn, addr = secure_server.accept()

#         thread = threading.Thread(target=handle_client, args=(conn, addr))
#         thread.start()


        #python -m http.server 8000 


import socket
import ssl
import threading
import time
from services import detect_service

HOST = "0.0.0.0"
PORT = 5000


def scan_ports(target, start_port, end_port):
    results = []
    threads = []
    lock = threading.Lock()

    total_ports = end_port - start_port + 1
    start_time = time.time()

    def scan_port(port):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)

            if s.connect_ex((target, port)) == 0:
                service = detect_service(port)
                with lock:
                    results.append(f"{port} OPEN ({service})")

            s.close()
        except:
            pass

    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(port,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()

    total_time = end_time - start_time
    response_time = round(total_time, 3)
    throughput = round(total_ports / total_time, 2) if total_time > 0 else 0
    latency = round(total_time / total_ports, 5)

    print("\n=== PERFORMANCE METRICS ===")
    print("Response Time:", response_time, "sec")
    print("Throughput:", throughput, "ports/sec")
    print("Average Latency:", latency, "sec")
    print("===========================\n")

    return results


def handle_client(conn, addr):
    print(f"Client connected: {addr}")

    try:
        data = conn.recv(1024).decode()

        if not data:
            print("Client disconnected abruptly")
            return

        parts = data.split()

        if len(parts) != 4:
            conn.send("Invalid input format".encode())
            return

        _, target, start_port, end_port = parts

        start_port = int(start_port)
        end_port = int(end_port)

        if start_port < 0 or end_port > 65535:
            conn.send("Invalid port range".encode())
            return

        results = scan_ports(target, start_port, end_port)

        response = "\n".join(results) if results else "No open ports found"
        conn.send(response.encode())

    except Exception as e:
        print("Error:", e)

    finally:
        conn.close()
        print("Client disconnected")


def start_server():
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)

    print("Secure Port Scanner Server Running...")

    while True:
        try:
            client_socket, addr = server.accept()

            try:
                secure_conn = context.wrap_socket(client_socket, server_side=True)
            except ssl.SSLError:
                
                client_socket.close()
                continue

            thread = threading.Thread(
                target=handle_client, args=(secure_conn, addr)
            )
            thread.start()

        except Exception as e:
            print("Server error:", e)


if __name__ == "__main__":
    start_server()