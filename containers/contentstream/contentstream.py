# Purpose is to resemble content delivery
# Container will download data and process it

# pip requirements:
    # wget

import wget
import os
import time

URL = "http://212.183.159.230/200MB.zip"

while True:
    print("Starting download...")
    response = wget.download(URL)
    print("File downloaded...")
    os.remove("200MB.zip")
    print("File deleted... waiting 10 seconds")
    time.sleep(10)