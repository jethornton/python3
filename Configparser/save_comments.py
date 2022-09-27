#!/usr/bin/env python3

# status: working

'''
Program to save comments and extra blank lines in an ini file
'''

import configparser
from collections import OrderedDict

def save_comments(config_file):
	with open(config_file, 'r') as f:
		content = f.readlines()
	test = ('#', ';')
	comments = OrderedDict() # create the ordered dictionary
	firstSection = False
	for index, line in enumerate(content):
		if line.startswith(test) or line.strip() == '': # not a key:value pair
			comments[index] = line
		# new section always has a preceeding blank line after the first section
		if line.strip().startswith('['):
			if firstSection:
				del comments[index-1]
			firstSection = True
	return comments

def restore_comments(parsed_file, out_file, comment_map):
	with open(parsed_file, 'r') as file:
		lines = file.readlines()
	for (index, comment) in comment_map.items():
		lines.insert(index, comment)
	with open(out_file, 'w') as file:
		file.write(''.join(lines))

in_file = 'tom.ini'
comment_file = 'tom_comment.ini'
parsed_file = 'tom_parsed.ini'
out_file = 'tom_out.ini'
comment_map = save_comments(in_file)

with open(comment_file, 'w') as file:
	for key, value in comment_map.items():
		file.write(f'Line: {key} Value: {value}')

# open config file and load it into configparser
with open(in_file, 'r') as file:
	config = configparser.ConfigParser()
	config.optionxform = str
	config.read_string(file.read())
# change every value in the config file to "Changed"
for section in config.sections():
	for key, value in config.items(section):
		config.set(section, key, "Changed")
# write the new config to the config file
with open(parsed_file, 'w') as file:
	config.write(file)
# put the comments back in their original indices
restore_comments(parsed_file, out_file, comment_map)
print('Done')


