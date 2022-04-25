#!/usr/bin/env python3
#Module psutil needs to be installed via pip3 first.
#Python script to Monitor Server Resources.

import time
import psutil

#set interval time for script gathering data
SCRIPT_INTERVAL = 0
ACTIVE = True

def net_usage():
    net_stat = psutil.net_io_counters()

    # return network input and output
    return net_stat.bytes_recv/1024/1024, net_stat.bytes_sent/1024/1024 #convert to MB

def disk_usage():
    disk_stat = psutil.disk_io_counters()

    #return disk input and output
    return disk_stat.write_bytes/1024/1024, disk_stat.read_bytes/1024/1024 #convert to MB


#if ACTIVE == False: #FOR TESTING PURPOSES


f = open("utillog"+time.strftime("%I:%M:%S %p", time.localtime())+".txt","w")
f.write("time,cpu,memu,netuin,netuout,disuin,disuout\n")

while ACTIVE == True:
    #implement delay for frequency of data collection
    time.sleep(SCRIPT_INTERVAL)

    # record disk and network statistics at the start of period
    net_recv_start, net_sent_start = net_usage()
    disk_write_start, disk_read_start = disk_usage()

    # calculate per second statistics
    time.sleep(1)

    # record disk and network statistics at the end of period
    net_recv_end, net_sent_end = net_usage()
    disk_write_end, disk_read_end = disk_usage()

    #record variables
    strtime = time.strftime("%I:%M:%S %p", time.localtime())
    cpuu = str(int(psutil.cpu_percent()))
    memu = str(int(psutil.virtual_memory().percent))
    netin = str(int(net_recv_end-net_recv_start))
    netout = str(int(net_sent_end-net_sent_start))
    diskwri = str(int(disk_write_end-disk_write_start))
    diskrea = str(int(disk_read_end-disk_read_start))

    # print all statistics
    print("Current time: ",strtime)
    print("CPU usage: ",cpuu, "%")
    print("Memory Usage: ", memu, "% used")
    print(f"Current net-usage: IN: {netin} MB/s, OUT: {netout} MB/s")
    print(f"Current disk-usage: WRITE: {diskwri} MB/s, READ: {diskrea} MB/s")
    print("------------------------\n")

    f.write(strtime+","+cpuu+","+memu+","+netin+","+netout+","+diskwri+","+diskrea+"\n")


