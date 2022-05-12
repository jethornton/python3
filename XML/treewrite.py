#!/usr/bin/env python3

'''
Modifying XML Elements
Using ElementTree

The ElementTree module presents several tools for modifying existing XML documents. The example below shows how to change the name of a node, change the name of an attribute and modify its value, and how to add an extra attribute to an element.

A node text can be changed by specifying the new value in the text field of the node object. The attribute's name can be redefined by using the set(name, value) function. The set function doesn't have to just work on an existing attribute, it can also be used to define a new attribute.

As we can see when comparing with the original XML file, the names of the item elements have changed to "newitem", the text to "new text", and the attribute "name2" has been added to both nodes.

You may also notice that writing XML data in this way (calling tree.write with a file name) adds some more formatting to the XML tree so it contains newlines and indentation.
'''

import xml.etree.ElementTree as ET

tree = ET.parse('items.xml')
root = tree.getroot()

# changing a field text
for elem in root.iter('item'):
    elem.text = 'new text'

# modifying an attribute
for elem in root.iter('item'):
    elem.set('name', 'newitem')

# adding an attribute
for elem in root.iter('item'):
    elem.set('name2', 'newitem2')

tree.write('newitems.xml')

