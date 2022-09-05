#!/usr/bin/env python3

# status: working

import os, sys, hashlib, argparse

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('-p', '--path', help="a directory to search",
		default=os.getcwd(), required=False)
	args = parser.parse_args()

	filelist = ls_files(args.path)

	if not dupes(filelist):
		print('No Duplicates Found')

def ls_files(dir):
	#files = {}
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

def dupes(filelist):
	d = {}
	result = False
	for file in filelist:
		sz = os.path.getsize(file)
		if sz in d:
			d[sz].append(file)
		else:
			d[sz] = []
			d[sz].append(file)

	for k, v in d.items():
		if len(v) > 1:
			test = []
			for i in v: # get md5sum for each file of the same length
				with open(i, 'rb') as f2c:
					data = f2c.read()
					md5 = hashlib.md5(data).hexdigest()
					test.append(md5)
			if len(set(test)) < len(test): # check for exact matches
				result = True
				print('Duplicate Files')
				for i in v:
					with open(i, 'rb') as f2c:
						data = f2c.read()
						md5 = hashlib.md5(data).hexdigest()
					print(f'File: {i}\nMD5: {md5}')
	print(f'\n{len(filelist)} Files Checked')
	return result

main()
