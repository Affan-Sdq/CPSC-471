from socket import *

serverPort = int(input("Port: "))
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

print("Server ready")

while True:
    connectionSocket, addr = serverSocket.accept()
    print("Connected:", addr)

    while True:
        data = connectionSocket.recv(1024).decode()
        if not data:
            break
        print("Client:", data)
        connectionSocket.send("OK".encode())

    connectionSocket.close()
