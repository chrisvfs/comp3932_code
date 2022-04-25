import socket
import time
from time import sleep

msgFromClient       = "Data request"
bytesToSend         = str.encode(msgFromClient)
serverAddressPort   = ("172.20.10.3", 2390)
bufferSize          = 256
# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# Send to server using created UDP socket
f = open("ammeterlog.txt","a")

while(True):
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)
    msgFromServer = UDPClientSocket.recvfrom(bufferSize)
    msg = msgFromServer[0]
    print(msg, "A at "+ time.strftime("%I:%M:%S %p", time.localtime())+"\n")
    f.write(time.strftime("%I:%M:%S %p", time.localtime())+","+str(msg)+"\n")
    
f.close()