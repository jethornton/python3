#!/usr/bin/env python3

'''
Creating XML Sub-Elements
Using ElementTree

The ElementTree module has more than one way to add a new element. The first way we'll look at is by using the makeelement() function, which has the node name and a dictionary with its attributes as parameters.

The second way is through the SubElement() class, which takes in the parent element and a dictionary of attributes as inputs.

In our example below we show both methods. In the first case the node has no attributes, so we created an empty dictionary (attrib = {}). In the second case, we use a populated dictionary to create the attributes.

As we can see when comparing with the original file, the "seconditems" element and its sub-element "seconditem" have been added. In addition, the "seconditem" node has "name2" as an attribute, and its text is "seconditemabc", as expected.
'''

import xml.etree.ElementTree as ET

tree = ET.parse('items.xml')
root = tree.getroot()

# adding an element to the root node
attrib = {}
element = root.makeelement('seconditems', attrib)
root.append(element)

# adding an element to the seconditem node
attrib = {'name2': 'secondname2'}
subelement = root[0][1].makeelement('seconditem', attrib)
ET.SubElement(root[1], 'seconditem', attrib)
root[1][0].text = 'seconditemabc'

# create a new XML file with the new element
tree.write('newitems2.xml')
