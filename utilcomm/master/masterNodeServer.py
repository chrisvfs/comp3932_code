import socket
from pcEstimate import runSearch

localIP     = "20.26.215.131"
localPort   = 2390
bufferSize  = 256



msgFromServer       = "Hello UDP Client"
bytesToSend         = str.encode(msgFromServer)

# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))    

f = open("log.txt", "w")

while(True):
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]

    clientMsg = message.decode()

    searchlist = clientMsg.split(',')
    power = runSearch(list(map(int,searchlist[2:])))
    finaloutput = searchlist[0] + "," + searchlist[1] + "," + str(power)
    print(finaloutput)

    f.write(finaloutput + '\n')

    # Sending a reply to client
    UDPServerSocket.sendto(bytesToSend, address)