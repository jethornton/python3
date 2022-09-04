#!/usr/bin/env python3
# import python modules
import os

# print(os.getcwd())

# directory name from which we are
# going to extract our files with its size
path = os.getcwd()
 
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
# now we have print the result by
# sorting the size of the file
# so, we have call sorted function
# to sort according to the size of the file
 
# created a lambda function that help us
# to sort according the size of the file.
fun = lambda x : x[1]
 
 
# in this case we have its file path instead of file
for f,s in sorted(size_of_file,key = fun):
	print(f'{os.path.join(path,f)}: {s}')
	#print("{} : {}mb".format(os.path.join(path,f),round(s/(1024*1024),3)))

