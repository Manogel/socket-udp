from socket import *

serverName = 'ip_server'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM) #UDP

message = input('Digite a mensagem: ')
message_bytes = message.encode('utf-8')

clientSocket.sendto(message_bytes, (serverName, serverPort))
modifiedMessage, serverAdress = clientSocket.recvfrom(2048)

print(modifiedMessage.decode('utf-8'))

clientSocket.close()
