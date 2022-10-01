#!/usr/bin/env python3

import configparser
from collections import OrderedDict

def save_comments(config_file):
	# find and log comments and more than one blank line in a row
	with open('test.ini', 'r') as f:
		content = f.readlines()

	test = ('#', ';')
	blank = False
	# an ordered dictionary must be used to insert from the start of the file
	# otherwise the insertion points will be off if you use a dict
	comments = OrderedDict() # create the ordered dictionary
	# check for empty line after a comment and add that to the comment map
	for index, line in enumerate(content):
		if not line.startswith(test) and line.strip() != '':
			comment = False
		if line.startswith(test): # a comment
			comments[index] = line
			comment = True
		if line.strip() == '':
			if blank or comment: # second blank line
				comments[index] = line
				print('blank')
			blank = True
		else:
			blank = False
	return comments

def restore_comments(config_file, comment_map):
	"""Write comments to config file at their original indices"""
	with open(config_file, 'r') as file:
		lines = file.readlines()
	for (index, comment) in comment_map.items():
		lines.insert(index, comment)
	with open(config_file, 'w') as file:
		file.write(''.join(lines))

config_file = 'test.ini'
comment_map = save_comments(config_file)
for key, value in comment_map.items():
	print(key, value)

# open config file and load it into configparser
with open(config_file, 'r') as file:
	config = configparser.ConfigParser()
	config.optionxform = str
	config.read_string(file.read())
# change every value in the config file to "CLASSIFIED"
for section in config.sections():
	for key, value in config.items(section):
		config.set(section, key, "Changed")
# write the new config to the config file
with open(config_file, 'w') as file:
	config.write(file)
# put the comments back in their original indices
restore_comments(config_file, comment_map)
print('Done')


