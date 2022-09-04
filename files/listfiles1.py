#!/usr/bin/env python3

# status: unknown or broken

import os
 
# directory name from which
# we are going to extract our files with its size
path = "D:\Books"
 
# Get list of all files only in the given directory
fun = lambda x : os.path.isfile(os.path.join(path,x))
files_list = filter(fun, os.listdir(path))
 
# Create a list of files in directory along with the size
size_of_file = [
    (f,os.stat(os.path.join(path, f)).st_size)
    for f in files_list
]
# Iterate over list of files along with size
# and print them one by one.
for f,s in size_of_file:
    print("{} : {}mb".format(f, round(s/(1024*1024),3)))
