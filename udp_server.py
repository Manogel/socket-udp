from socket import * 

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('ip_server', serverPort))
print('O servidor está pronto para receber!')

while 1:
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode('utf8').upper().encode('utf8') 
    serverSocket.sendto(modifiedMessage, clientAddress)
