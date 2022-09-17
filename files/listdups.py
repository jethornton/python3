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
	dupCount = 0
	for k, v in d.items():
		if len(v) > 1: # more than one file of the same size
			checksum = []
			for i in v: # get md5sum for each file of the same length
				with open(i, 'rb') as f2c:
					data = f2c.read()
					md5 = hashlib.md5(data).hexdigest()
					checksum.append(md5)

			if len(set(checksum)) < len(checksum): # check for exact matches
				result = True
				print('\n\tDuplicate Files')
				md5List = []
				for file in v:
					with open(file, 'rb') as f2c:
						data = f2c.read()
						thismd5 = hashlib.md5(data).hexdigest()
						if checksum.count(thismd5) > 1:
							dupCount += 1
							print(f'File: {file}\nMD5: {thismd5}')
	print(f'\n{len(filelist)} Files Checked, {dupCount} Duplicates')
	return result

main()
