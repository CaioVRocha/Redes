import socket

HOST = '127.0.0.1'
PORT = 50000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    texto = input(("Texto a ser convertido em binário: "))

    s.sendall(str.encode(texto))
    data = s.recv(1024)

    print("Texto Convertido:", data.decode())