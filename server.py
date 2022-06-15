import socket

HOST = 'localhost'
PORT = 50000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()

while True:
    conn, ender = s.accept()

    while True:
        data = conn.recv(1024)
        if not data:
            conn.close()
            break

        textoBinario = ' '.join(format(ord(c), 'b') for c in data.decode())
        print(textoBinario)
        conn.sendall(str.encode(textoBinario))