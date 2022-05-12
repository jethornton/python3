#!/usr/bin/env python3

'''
Finding XML Elements
Using ElementTree

The ElementTree module offers the findall() function, which helps us in finding specific items in the tree. It returns all items with the specified condition. In addition, the module has the function find(), which returns only the first sub-element that matches the specified criteria. The syntax for both of these functions are as follows:

findall(match, namespaces=None)

find(match, namespaces=None)

For both of these functions the match parameter can be an XML tag name or a path. The function findall() returns a list of elements, and find returns a single object of type Element.

In addition, there is another helper function that returns the text of the first node that matches the given criterion:

findtext(match, default=None, namespaces=None)

'''

import xml.etree.ElementTree as ET
#tree = ET.parse('items.xml')
tree = ET.parse('eng-de.ts')
root = tree.getroot()

# find the first 'item' object
#for elem in root:
#    print(elem.find('message').get('name'))

# find all "item" objects and print their "name" attribute
for elem in root:
    for subelem in elem.findall('message'):
    
        # if we don't need to know the name of the attribute(s), get the dict
        print(subelem.attrib)      
    
        # if we know the name of the attribute, access it directly
        print(subelem.get('type'))
