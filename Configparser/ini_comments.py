#!/usr/bin/env python3

'''
The python configparser will change the case of everything and remove any
comments. This program reads in the ini file, saves the comments and blank lines
to a dictionary then updates the ini and lastly restores the comments and blank
lines.

Default is the current working directory and test.ini
The output file will be the file name appended with _out
To get the options use -h
ini_comments.py -h 
'''

import os, argparse, configparser
from collections import OrderedDict

class main():
	def __init__(self):
		super().__init__()

		parser = argparse.ArgumentParser()
		# add argument with a default if nothing is passed
		parser.add_argument('-p', '--path', help="path to file",
			default=os.getcwd(), required=False)
		parser.add_argument('-f', '--file', help="the file name to test",
			default='test.ini', required=False)
		parser.add_argument('-a', '--all', help="create files for each step",
			default=True, required=False)
		args = parser.parse_args()
		name = os.path.splitext(args.file)[0]
		ext = os.path.splitext(args.file)[1]
		self.input_file = os.path.join(args.path, args.file)
		self.comment_file = os.path.join(args.path, name + "_comments" + ext)
		self.parsed_file = os.path.join(args.path, name + "_parsed" + ext)
		self.output_file = os.path.join(args.path, name + "_out" + ext)
		self.all = args.all
		self.process_ini()

	def process_ini(self):
		#print(f'Input File: {self.input_file}')
		#print(f'Output File: {self.output_file}')
		#print(f'Save All: {self.all}')
		# First save the comments and blank lines to a dictionary
		comment_dict = self.save_comments()
		if self.all:
			with open(self.comment_file, 'w') as file:
				for key, value in comment_dict.items():
					file.write(f'Line: {key} Value: {value}')
		self.modify_ini()
		self.restore_comments(comment_dict)
		print('Done')

	def save_comments(self):
		with open(self.input_file, 'r') as file:
			content = file.readlines()
		test = ('#', ';')
		comments = OrderedDict() # create the ordered dictionary
		firstSection = False
		for index, line in enumerate(content):
			if line.strip().startswith(test) or line.strip() == '': # not a key:value pair
				comments[index] = line
			# new section always has a preceeding blank line after the first section
			if line.strip().startswith('['):
				if firstSection:
					del comments[index-1]
				firstSection = True
		return comments

	def modify_ini(self):
		# open config file and load it into configparser
		with open(self.input_file, 'r') as file:
			config = configparser.ConfigParser()
			# Set the option to retain case
			config.optionxform = str
			config.read_string(file.read())
		# change every value in the config file to "Changed"
		for section in config.sections():
			for key, value in config.items(section):
				config.set(section, key, "Changed")
		# write the new config to the config file
		if self.all:
			with open(self.parsed_file, 'w') as file:
				config.write(file)
		else:
			with open(self.output_file, 'w') as file:
				config.write(file)

	def restore_comments(self, comment_dict):
		with open(self.output_file, 'r') as file:
			lines = file.readlines()
		for (index, comment) in comment_dict.items():
			lines.insert(index, comment)
		with open(self.output_file, 'w') as file:
			file.write(''.join(lines))


if __name__ == "__main__":
	main()


