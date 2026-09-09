import socket
print("PORT SCANNER")
target = input("target IP>>")
start = int(input("port: START>>"))
end = int(input("port: END>>"))
pst = float(input("port scanning timeout>>"))
ports = list(range(start, end))
for port in ports:
    s = socket.socket()
    s.settimeout(pst)
    try:
        s.connect((target, port))
        if port == 21:
            print(f"[+] port {port} is OPEN (FTP)")
        elif port == 22:
            print(f"[+] port {port} is OPEN (SSH)")
        elif port == 23:
            print(f"[+] port {port} is OPEN (TELNET)")
        elif port == 25:
            print(f"[+] port {port} is OPEN (SMTP)")
        elif port == 53:
            print(f"[+] port {port} is OPEN (DNS)")
        elif port == 80:
            print(f"[+] port {port} is OPEN (HTTP)")
        elif port == 110:
            print(f"[+] port {port} is OPEN (POP3)")
        elif port == 143:
            print(f"[+] port {port} is OPEN (IMAP)")
        elif port == 443:
            print(f"[+] port {port} is OPEN (HTTPS)")
        elif port == 445:
            print(f"[+] port {port} is OPEN (SMB)")
        elif port == 853 :
            print(f"[+] port {port} is OPEN (DNS over TLS)")
        elif port == 3306:
            print(f"[+] port {port} is OPEN (MySQL)")
        elif port == 3389:
            print(f"[+] port {port} is OPEN (RDP)")
        elif port == 5900:
            print(f"[+] port {port} is OPEN (VNC)")
        elif port == 8080:
            print(f"[+] port {port} is OPEN (HTTP-ALT)")
        else:
            print(f"[+] port {port} is OPEN")
        s.close
    except:
        print(f"[-] {port} is closed")