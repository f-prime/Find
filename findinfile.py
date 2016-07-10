#!/usr/bin/python
import sys
import re
import os

if len(sys.argv) < 2:
    print "Usage: findinfile <string> [--ignorecase]"
    sys.exit()

pattern = ''.join(sys.argv[1])

for path, folder, files in os.walk(os.getcwd()):
    for files in files:
        if "--ignorecase" in sys.argv:
            content = open(path+"/"+files).read().lower()
            pattern = pattern.lower()
        else:
            content = open(path+"/"+files).read()
        if re.findall(pattern, content):
            print path + "/" + files    
            
