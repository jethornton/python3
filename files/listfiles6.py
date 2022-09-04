#!/usr/bin/env python3

status: working

import os

#dir = os.getcwd()

def ls_files(dir):
	files = list()
	for item in os.listdir(dir):
		abspath = os.path.join(dir, item)
		try:
			if os.path.isdir(abspath):
				files = files + ls_files(abspath)
			else:
				files.append(abspath)
		except FileNotFoundError as err:
			print('invalid directory\n', 'Error: ', err)
	return files

for file in ls_files(os.getcwd()):
	print(file)
