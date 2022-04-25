import socket
import psutil
import time
import getpass


def net_usage():
    net_stat = psutil.net_io_counters()

    # return network input and output
    return net_stat.bytes_recv/1024/1024, net_stat.bytes_sent/1024/1024 #convert to MB

def disk_usage():
    disk_stat = psutil.disk_io_counters()

    #return disk input and output
    return disk_stat.write_bytes/1024/1024, disk_stat.read_bytes/1024/1024 #convert to MB


serverAddressPort   = ("20.26.215.131", 2390)
bufferSize          = 256
# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)



while True:
    currentTime = int(time.strftime("%S", time.localtime()))
    if currentTime % 5 == 0: 
        # Send to server using created UDP socket
        
        # record disk and network statistics at the start of period
        net_recv_start, net_sent_start = net_usage()
        disk_write_start, disk_read_start = disk_usage()

        # calculate per second statistics
        time.sleep(1)

        # record disk and network statistics at the end of period
        net_recv_end, net_sent_end = net_usage()
        disk_write_end, disk_read_end = disk_usage()

        msg = ""
        msg += getpass.getuser() + ","

        msg += time.strftime("%I:%M:%S %p", time.localtime()) + ","
        msg += str(int(psutil.cpu_percent())) + ","
        msg += str(int(psutil.virtual_memory().percent)) + ","
        msg += str(int(net_recv_end-net_recv_start)) + ","
        msg += str(int(net_sent_end-net_sent_start)) + ","
        msg += str(int(disk_write_end-disk_write_start)) + ","
        msg += str(int(disk_read_end-disk_read_start))

        bytesToSend         = str.encode(msg)
        UDPClientSocket.sendto(bytesToSend, serverAddressPort)

        print("Sent util info to server")
