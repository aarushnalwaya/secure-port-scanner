services = {
21: "FTP",
22: "SSH",
23: "TELNET",
25: "SMTP",
53: "DNS",
80: "HTTP",
110: "POP3",
143: "IMAP",
443: "HTTPS",
135: "RPC",
445: "SMB",
8000: "HTTP-ALT"
}

def detect_service(port):
    return services.get(port, "Unknown")