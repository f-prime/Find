#!/usr/bin/python
import sys
import re
import os
import string

def regex(pattern, content, ifTrue, ignoreCase):
    try: 
        for c in content:
            if ignoreCase:
                c = c.lower()
                pattern = pattern.lower()
            if re.findall(pattern, c):
                print ifTrue
                break
    except Exception, e:
        print e

if len(sys.argv) < 2:
    print "Usage: findinfile <string> [--ignorecase] [--startpath=/]"
    sys.exit()

pattern = ''.join(sys.argv[1])

directory = os.getcwd()
joined = ' '.join(sys.argv)
if "--startpath" in joined:
    path = re.findall("--startpath=([a-zA-Z{}]+)".format(string.punctuation), joined)
    if path:
        directory = path[0]

for path, folder, files in os.walk(directory):
    for files in files:
        if "--ignorecase" in sys.argv:
            try:
                content = open(path+"/"+files)
            except IOError, e:
                print e
            regex(pattern, content, path + "/" + files, True)
        else:
            try:
                content = open(path+"/"+files)
            except IOError, e:
                print e
            regex(pattern, content, path + "/" + files, False)

