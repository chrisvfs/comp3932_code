#imports
import csv
import random
import sys

#Required operating voltage of a raspberry pi
RP_VOLTAGE = 5.1

# functions
def generateFakeData(ul,fd):
    for line in ul.readlines():
        sline = line[:-1].split(',')
        fd.write(sline[0]+","+str(random.random()* (int(sline[1]) + int(sline[2])) )+'\n')

#search array and return index or -1 if not found
def searchArray(ar,item):
    count = 0
    for row in ar:
        if ar[count][0] == item:
            return count
        count += 1
    return -1

#global variables
utillogheadings = ["power","cpu","memu","netuin","netuout","disuin","disuout"]

#open necessary files
print("Opening files...")
utillog = open("utillog.txt","r")
ammeterlog = open("ammeterlog.txt","r")

#generate fake data

# fakedata = open("ammeterlog.txt","w")
# generateFakeData(utillog,fakedata)
# fakedata.close()
# print("fake data generated...")
# utillog.close()

# move ammeter log to array and convert to power
ammeterArray = []
for line in ammeterlog.readlines():
    row = line[:-1].split(',')
    # Convert current reading to power using P = I x V
    row[1] = float(row[1]) * RP_VOLTAGE
    ammeterArray.append(row)

print("Cleansing ammeter readings")
# clean ammeter array (merge values)
indexCount = 0
cleanAmmeterArray = []
while indexCount < len(ammeterArray):
    indexCountTemp = indexCount
    mergeTime = ammeterArray[indexCount][0]
    total = ammeterArray[indexCount][1]
    count = 1
    while indexCountTemp+2 < len(ammeterArray) and ammeterArray[indexCountTemp+1][0] == mergeTime:
        indexCountTemp += 1
        total += ammeterArray[indexCountTemp][1]
        count += 1
    indexCount += count
    cleanAmmeterArray.append([mergeTime,(total/count)])



utillog = open("utillog.txt","r")

# merge data
print("Merging data...")
mergearray = []
for line in utillog.readlines():
    # remove the \n from the line and add to array
    mergearray.append((line[:-1]).split(','))

for reading in cleanAmmeterArray:
    index = searchArray(mergearray,reading[0])
    if index != -1:
        mergearray[index][0] = reading[1]


print("Removing data that does not have an associated reading...")

for count in range(len(mergearray)-1,-1,-1):
    if(isinstance(mergearray[count][0], str)):
        mergearray.pop(count)

for i in mergearray:
    print(i)

# cleanse data
print("Cleansing utilisation readings...")
utillogheadings = ["power","cpu","memu","netuin","netuout","disuin","disuout"]


indexC = 0
for items in mergearray:
    utilval = items[1:]
    checkIndex = indexC + 1
    #count total and count to calculate average
    total = float(items[0])
    count = 1
    while checkIndex < len(mergearray):
        if mergearray[checkIndex][1:] == utilval:
            total += float(mergearray[checkIndex][0])
            count += 1
            mergearray.pop(checkIndex)
        else:
            checkIndex += 1
    items[0] = str(total / count)

    indexC += 1

#for i in mergearray:
#    print(i)

# #normalise data

# cpumax, cpumin = -1, sys.maxsize
# memumax, memumin = -1, sys.maxsize
# netuinmax, netuinmin = -1, sys.maxsize
# netuoutmax, netuoutmin = -1, sys.maxsize
# disuinmax, disuinmin = -1, sys.maxsize
# disuoutmax, disuout = -1, sys.maxsize

cleandata = open("cleanutillog.txt","w")
cleandata.write("power,cpu,memu,netuin,netuout,disuin,disuout\n")
for values in mergearray:
    cleandata.write(values[0])
    for value in values[1:]:
        cleandata.write(","+value)
    cleandata.write("\n")

#close files
utillog.close()
cleandata.close()
ammeterlog.close()