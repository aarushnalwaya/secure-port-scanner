import http.server
import ssl

PORT = 443

server_address = ("", PORT)

httpd = http.server.HTTPServer(
    server_address,
    http.server.SimpleHTTPRequestHandler
)

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")

httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

print("HTTPS Server running on port 443")

httpd.serve_forever()