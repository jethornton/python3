#!/usr/bin/env python3

import os
#from configparser import ConfigParser
from configparser import ConfigParser
# instantiate
config = ConfigParser()

def readINI():
	# parse existing file
	config.read(iniPath)
	print('config read')

def checkSection():
	if config.has_section('mailbox1'):
		print('section there')
		updateSection()
	else:
		print('section not there')
		addSection()

def addSection():
	print('adding section')
	config.add_section('mailbox1')
	config.set('mailbox1', 'user', 'cl@gnipsel.com')
	config.set('mailbox1', 'password', '404')
	# save to a file
	with open(iniPath, 'w') as configfile:
		config.write(configfile)

def updateSection():
	config.set('mailbox1', 'user', 'cl@gnipsel.com')
	# save to a file
	with open(iniPath, 'w') as configfile:
		config.write(configfile)

def createFile():
	pass

home = os.path.expanduser('~')
iniPath = os.path.join(home, '.config/jtmail/jtmail.ini')
print(iniPath)
if os.path.isfile(iniPath):
	print("it's there")
	readINI()
	checkSection()
else:
	print("it's not there")
	createFile()

"""


# parse existing file
config.read('test.ini')

# read values from a section
string_val = config.get('section_a', 'string_val')
bool_val = config.getboolean('section_a', 'bool_val')
int_val = config.getint('section_a', 'int_val')
float_val = config.getfloat('section_a', 'pi_val')

# update existing value
config.set('section_a', 'string_val', 'world')

# add a new section and some values
config.add_section('section_b')
config.set('section_b', 'meal_val', 'spam')
config.set('section_b', 'not_found_val', '404')

# save to a file
with open('test_update.ini', 'w') as configfile:
	config.write(configfile)
"""
