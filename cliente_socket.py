import socket

host = 'localhost'
port = 61182

clienteSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)

clienteSocket.connect((host, port))
print("Conexion con servidor")

while True:

    mensaje = input("enviar mensaje ")#codigo que permite terminar la conexion por parte del cliente
    if mensaje == '\salir':
        break
    clienteSocket.send(mensaje.encode())
    print(f'>>> {clienteSocket.recv(1024).decode()}')
print("Conexion terminada")
clienteSocket.close()