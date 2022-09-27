#!/usr/bin/env python3

# status: working

import os, argparse
parser = argparse.ArgumentParser()
# add argument with a default if nothing is passed
parser.add_argument('-p', '--path', help="a directory to search",
	default=os.getcwd(), required=False)

args = parser.parse_args()

print(args.path)

