#!/usr/bin/env python3

#from configparser import RawConfigParser
import configparser

input_file = 'test.ini'
output_file = 'test_out.ini'

with open(input_file, 'r') as file:
	config = configparser.ConfigParser(allow_no_value=True)
	# Set the option to retain case
	config.optionxform = str
	config.read_string(file.read())
# change every value in the config file to "Changed"
for section in config.sections():
	for key, value in config.items(section):
		#print(key, value)
		config.set(section, key, "Changed")
# write the new config to the config file
with open(output_file, 'w') as file:
	config.write(file)

