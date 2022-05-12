#!/usr/bin/env python3

'''
Using ElementTree

ElementTree presents us with an very simple way to process XML files. As always, in order to use it we must first import the module. In our code we use the import command with the as keyword, which allows us to use a simplified name (ET in this case) for the module in the code.

Following the import, we create a tree structure with the parse function, and we obtain its root element. Once we have access to the root node we can easily traverse around the tree, because a tree is a connected graph.

Using ElementTree we obtain the node attributes and text using the objects related to each node.

The attrib object is simply a dictionary object, which makes it a bit more compatible with other Python code.

Accessing objects and attributes with ElementTree is a bit more Pythonic. This is because the XML data is parsed as simple lists and dictionaries
'''

import xml.etree.ElementTree as ET
tree = ET.parse('items.xml')
root = tree.getroot()

# one specific item attribute
print('Item #2 attribute:')
print(root[0][1].attrib)

# all item attributes
print('\nAll attributes:')
for elem in root:
    for subelem in elem:
        print(subelem.attrib)

# one specific item's data
print('\nItem #2 data:')
print(root[0][1].text)

# all items data
print('\nAll item data:')
for elem in root:
    for subelem in elem:
        print(subelem.text)

