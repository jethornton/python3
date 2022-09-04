#!/usr/bin/env python3

# status: working


'''
Find duplicate files by size and print duplicates
'''

import os,sys
d = {}
gen = os.walk(os.getcwd())

for i in gen:
	dirname, dirlist, filelist = i
	for f in filelist:
		fullname = os.path.join(dirname,f)
		sz = os.path.getsize(fullname)
		if sz in d:
			d[sz].append(fullname)

		else:
			d[sz] = []
			d[sz].append(fullname)

for k, v in d.items():
	if len(v) > 1:
		for i in v:
			print(i, k)


