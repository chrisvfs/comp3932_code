#This script takes CPU usage, Memory usage, Network I/O, Disk I/O and returns and estimate for the power consumption
from re import search
import sys

def runSearch(searchValues):
    culog = open("cleanutillog.txt", "r")
    headers = culog.readline()
    bestdiff = sys.maxsize
    bestrow = []
    for lines in culog.readlines():
        lines = lines[:-1].split(',')
        currentDiff = 0
        for i in range(0, 6):
            currentDiff += abs(searchValues[i] - int(lines[i+1]))

        if currentDiff < bestdiff:
            bestdiff = currentDiff
            bestrow = lines
    #print(bestrow, bestdiff)
    return float(bestrow[0])

