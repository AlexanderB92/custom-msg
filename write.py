import os
import time
import hashlib

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

        os.popen("echo \""+ algo.hexdigest() + "\" > a.txt")
        b = os.popen("git add . && git commit --date=\"" + workingDate + "\" -m \"test\" && git push")

        print(workingDate + " " + str(b))


