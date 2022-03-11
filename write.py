import os
import time
import hashlib
import random
import subprocess

datefile = "dates.txt"
workingfile = "store.txt"


with open(datefile) as file, open(workingfile,'rb',buffering=0) as worker:
    for line in file:
        workingDate = line.rstrip()

        blocksize = bytearray(128*1024)
        mem = memoryview(blocksize)
        algo = hashlib.sha256()

        for i in iter(lambda : worker.readinto(mem),0):
            algo.update(mem[:i])

        time.sleep(6)

        retOne = subprocess.run("echo \""+ algo.hexdigest() + str(random.random()) + "\" > a.txt", capture_output=True, shell=True)
        retTwo = subprocess.run("git add .; git commit --date=\"" + workingDate + "\" -m \""+ str(random.random()) +"\"; git push")

        print(workingDate + " " + str(retTwo))


