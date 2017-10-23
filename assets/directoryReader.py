import os
import sys
f = open('poetList.txt', 'w+')
path = "./collection/"
dirs = os.listdir(path)
for fl in dirs:
    print(fl)
    f.write(fl + ", ")
f.close()