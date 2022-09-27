#!/usr/bin/env python3

import getopt, sys

# Remove 1st argument from the
# list of command line arguments
argumentList = sys.argv[1:]

# Options
options = "fh:"

# Long options
long_options = ["Help", "file="]
	
try:
	# Parsing argument
	arguments, values = getopt.getopt(argumentList, options, long_options)

	# checking each argument
	for currentArgument, currentValue in arguments:

		if currentArgument in ("-h", "--Help"):
			print ("Displaying Help")

		elif currentArgument in ("-f", "--file"):
			print ("Displaying file_name:", sys.argv[0])

except getopt.error as err:
	# output error, and return with an error code
	print (str(err))
