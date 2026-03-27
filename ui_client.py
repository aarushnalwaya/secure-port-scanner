import socket
import ssl
import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

HOST = "127.0.0.1"
PORT = 5000

def scan_ports():
    target = ip_entry.get()
    start_port = start_entry.get()
    end_port = end_entry.get()

    try:
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE

        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        secure_client = context.wrap_socket(client, server_hostname=HOST)

        secure_client.connect((HOST, PORT))

        message = f"SCAN {target} {start_port} {end_port}"
        secure_client.send(message.encode())

        result = secure_client.recv(4096).decode()

        output_box.delete("1.0", "end")
        output_box.insert("end", result)

        secure_client.close()

    except Exception as e:
        output_box.delete("1.0", "end")
        output_box.insert("end", f"Error: {e}")


# UI Window
app = ctk.CTk()
app.title("Secure Port Scanner")
app.geometry("500x500")

title = ctk.CTkLabel(app, text="Secure Port Scanner", font=("Arial", 20))
title.pack(pady=10)

ip_entry = ctk.CTkEntry(app, placeholder_text="Target IP")
ip_entry.pack(pady=10)

start_entry = ctk.CTkEntry(app, placeholder_text="Start Port")
start_entry.pack(pady=10)

end_entry = ctk.CTkEntry(app, placeholder_text="End Port")
end_entry.pack(pady=10)

scan_button = ctk.CTkButton(app, text="Scan Ports", command=scan_ports)
scan_button.pack(pady=15)

output_box = ctk.CTkTextbox(app, height=200)
output_box.pack(pady=10, padx=10, fill="both", expand=True)

app.mainloop()