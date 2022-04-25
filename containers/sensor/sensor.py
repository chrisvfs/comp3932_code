# import numpy as np
import math

SIZE = 10000000
ACTUAL_SD = 100

# # Generte data
# data = np.random.normal(100000,ACTUAL_SD,SIZE)

# #Write the data to the file
# file = open("data.txt","w")

# count = 0
# for i in data:
#     file.write(str(i) + ",")
#     count += 1
#     if count % 1000000 == 0:
#         print(count)

# file.close()
# print("file write complete")

while True:
    file = open("data.txt", "r")

    stri = file.readline()
    arr = stri.split(",")[:-1]
    file.close()
    print("file opened")
    # Mean
    mean = 0.0
    for data in arr:
        mean += float(data)
    mean = mean / SIZE
    print("mean calculated")
    # standard deviation
    # sd = sqrt( SUM( (data - mean)^2 ) / SIZE )
    total = 0.0

    for data in arr:
        total += (float(data) - mean)**2
    sd = math.sqrt( total / SIZE )
    print("Difference = " + str(abs(ACTUAL_SD - sd)))
