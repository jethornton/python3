#!/usr/bin/env python3

'''
Deleting one sub-element

One specific sub-element can be deleted using the remove function. This function must specify the node that we want to remove.

As we can see from the XML code above, there is now only one "item" node. The second one has been removed from the original tree.
'''

import xml.etree.ElementTree as ET

tree = ET.parse('items.xml')
root = tree.getroot()

# removing one sub-element
root[0].remove(root[0][0])

# create a new XML file with the results
tree.write('newitems4.xml')

