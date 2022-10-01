#!/usr/bin/env python3

import configparser

config = configparser.ConfigParser(allow_no_value=True, strict=False)
config.optionxform = str
config.read('test.ini')
config.set('MESA', '; This Comment Will Keep Its Original Case', None)

with open('test_out.ini', 'w') as configfile:
	config.write(configfile)
