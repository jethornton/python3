import os

# to test if a directory exists
if not os.path.exists(directory):
	os.makedirs(directory)

# to test if a file exists
if os.path.isfile(fname):
	#do some stuff

# get home directory
os.path.expanduser('~')

#Gives the name of the imported operating system dependent module
os.name

# To loop through the provided directory, and not subdirectories we can
# use the following code:

for file in os.listdir("/Users/darren/Desktop/test"):
	if file.startswith("art"):
		print(file)

"""
The above code will loop through all the files in my test directory.
On each iteration it will check to see if the filename starts with art,
In my case, the following prints out:
"""

# listing all files in the given directory and all of its subdirectories
# where the file starts with a given string/prefix.

for path, currentDirectory, files in os.walk("/Users/darren/Desktop/test"):
	for file in files:
		if file.startswith("art"):
			print(file)

"""
The code is very similar, but now we use os.walk instead of os.listdir.
os.walk will allow us to go through all the subdirectories as well.

In each directory we loop through each file. We will then check to see
if that file's name starts with art and if it does we will print out the
file name.
"""

# If you want to print out the full path for the file you can replace
# print(file) with

print(os.path.join(path, file))

#In long form (with for loops),

import os
path = 'C:/'
files = []
for i in os.listdir(path):
    if os.path.isfile(os.path.join(path,i)) and '001_MN_DX' in i:
        files.append(i)

Code, with list-comprehensions is

import os
path = 'C:/'
files = [i for i in os.listdir(path) if os.path.isfile(os.path.join(path,i)) and \
         '001_MN_DX' in i]
