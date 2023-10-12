import socket

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM,0)
 
servidor.bind(("", 61182))
 
servidor.listen(5)
 

cliente, addr = servidor.accept()

while True:

    
    recibido = cliente.recv(1024)

    print ("Recibo conexion de la IP: " + str(addr[0]) + " Puerto: " + str(addr[1]))
    respuesta =("       _    " + "\n"+
             "      | |   "+"\n"+
             "  ___ | | __"+"\n"+
             " / _ \| |/ /"+"\n"+
             "| (_) |   <"+"\n"+
             " \___/|_|\_)")
    
    cliente.send(respuesta.encode())
    comando = input("comando: ")#codigo que permite terminar el while desde el lado del servidor
    if comando == '\salir':
        break
cliente.close()
servidor.close()

print("Conexiones cerradas")