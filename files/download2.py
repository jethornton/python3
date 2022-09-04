#!/usr/bin/env python3

# status: unknown or broken

import sys, time, requests

# use a context manager to make an HTTP request and file
with requests.get("https://github.com/jethornton/mesact/raw/master/mesact_0.4.0_amd64.deb", stream=True) as r:
	with open("mesact_0.4.0_amd64.deb", 'wb') as file:
		# Get the total size, in bytes, from the response header
		total_size = int(r.headers.get('Content-Length'))
		# Define the size of the chunk to iterate over (Mb)
		chunk_size = 1
		# iterate over every chunk and calculate % of total
		for i, chunk in enumerate(r.iter_content(chunk_size=chunk_size)):
			# calculate current percentage
			c = i * chunk_size / total_size * 100
			# write current % to console, pause for .1ms, then flush console
			sys.stdout.write(f"\r{round(c, 4)}%")
			time.sleep(.1)
			sys.stdout.flush()
