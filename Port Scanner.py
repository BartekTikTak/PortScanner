import socket

target = input(">") 
min_port = int(input("P1>")) 
max_port = int(input("P2>"))

open_ports = []

def scan_port(target, port): 
    try: 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        s.settimeout(1) 
        s.connect((target, port)) 
        print(f"Port {port} Jest Otwarty na {target}") 
        open_ports.append(port) 
    except: 
        print(f"Port {port} Jest Zamkniety na {target}")

for port in range(min_port, max_port + 1): 
    scan_port(target, port)

with open("open_ports.txt", "w") as file: 
    for port in open_ports: 
        file.write(f"Port {port} jest otwarty na {target}")
