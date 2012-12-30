#!/usr/bin/python 
import os,sys

def find():
    for dir,b,c in os.walk(sys.argv[1]):
        for file in c:
            a = dir+"/"+file
            if sys.argv[2] in a:
                 print a 


if __name__ == "__main__":
    find()
