#!/usr/bin/env python3

'''
Deleting XML Elements
Using ElementTree

As you'd probably expect, the ElementTree module has the necessary functionality to delete node's attributes and sub-elements.

Deleting an attribute

The code below shows how to remove a node's attribute by using the pop() function. The function applies to the attrib object parameter. It specifies the name of the attribute and sets it to None.
'''

import xml.etree.ElementTree as ET

tree = ET.parse('items.xml')
root = tree.getroot()

# removing an attribute
root[0][0].attrib.pop('name', None)

# create a new XML file with the results
tree.write('newitems3.xml')
