#!/usr/bin/env python3

'''
Deleting all sub-elements

The ElementTree module presents us with the clear() function, which can be used to remove all sub-elements of a given element.
'''

import xml.etree.ElementTree as ET

tree = ET.parse('items.xml')
root = tree.getroot()

# removing all sub-elements of an element
root[0].clear()

# create a new XML file with the results
tree.write('newitems5.xml')
