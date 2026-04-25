from socket import *
import sys

serverName = sys.argv[1]
serverPort = int(sys.argv[2])

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

while True:
    cmd = input("ftp> ")
    clientSocket.send(cmd.encode())

    if cmd == "quit":
        break

    response = clientSocket.recv(1024).decode()
    print("Server:", response)

clientSocket.close()
