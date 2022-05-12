#!/usr/bin/env python3

# compare two strings to see if any common letters in the two strings
a = 'ABC'
b = 'XYZA'
c = 'xyza'

if set(a)&set(b):
	print('yes')

if set(a)&set(c):
	print('yes')

'''
The test is case sensitive as shown here
>>> a = 'ABC'
>>> b = 'XYZA'
>>> c = 'xyza'
>>> if set(a)&set(b):
...     print('yes')
... 
yes
>>> if set(a)&set(c):
...     print('yes')
... 
>>> 
'''

# make a list of common letters in two strings
a = 'XYZUVW'
b = 'XYZA'
c = list(set(a)&set(b))

'''
>>> a = 'XYZUVW'
>>> b = 'XYZA'
>>> c = list(set(a)&set(b))
>>> c
['Y', 'X', 'Z']
>>> 
'''
