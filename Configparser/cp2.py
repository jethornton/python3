#!/usr/bin/env python3

from collections import OrderedDict

with open('test.ini','r') as file:
	content = file.readlines()
print(type(content))
sections = OrderedDict() # create the ordered dictionary
for index, line in enumerate(content):
	if line.strip().startswith('['):
		sections[line.strip()] = [index + 1, 0]

# set start and stop index for each section
previous = ''
for key, value in sections.items():
	if previous:
		sections[previous][1] = value[0] - 2
	previous = key

#print(sections['[MESA]'])
#print(content.index('VERSION', sections['[MESA]'][0], sections['[MESA]'][1]))

#print(type(sections['[MESA]'][0]))
#for item in content[sections['[MESA]'][0]: sections['[MESA]'][1]]:
#	if item.startswith('VERSION'):
#		print(item)

#for key, value in sections.items():
#	print(key, value)
#print(sections.items())

#content[sections['[MESA]']

def update(section, key, value):
	start = sections[f'[{section}]'][0]
	end = sections[f'[{section}]'][1]
	#print(f'Start: {start} End: {end}')
	for item in content[start:end]:
		if item.startswith(key):
			index = content.index(item)
			#print(item)
			content[index] = f'{key} = {value}\n'
			#print(content[index])

update('MESA', 'VERSION', '0.7.3')

with open("test_out.ini", "w") as outfile:
    outfile.write(''.join(content))


