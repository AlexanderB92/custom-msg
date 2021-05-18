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

        time.sleep(2)
        os.system("echo \""+ algo.hexdigest() + str(random.random()) + "\" > " + workingfile)
        time.sleep(3)
        os.system("git add . && git commit --date \"" + workingDate + "\" -m \""+ str(random.random()) +"\" && git push")

        print(workingDate)


