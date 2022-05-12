#!/usr/bin/env python3

'''
Writing XML Documents
Using ElementTree

ElementTree is also great for writing data to XML files. The code below shows how to create an XML file with the same structure as the file we used in the previous examples.

The steps are:

    Create an element, which will act as our root element. In our case the tag for this element is "data".
    Once we have our root element, we can create sub-elements by using the SubElement function. This function has the syntax:

SubElement(parent, tag, attrib={}, **extra)

Here parent is the parent node to connect to, attrib is a dictionary containing the element attributes, and extra are additional keyword arguments. This function returns an element to us, which can be used to attach other sub-elements, as we do in the following lines by passing items to the SubElement constructor.
3. Although we can add our attributes with the SubElement function, we can also use the set() function, as we do in the following code. The element text is created with the text property of the Element object.
4. In the last 3 lines of the code below we create a string out of the XML tree, and we write that data to a file we open.
'''
import xml.etree.ElementTree as ET

# create the file structure
data = ET.Element('data')
items = ET.SubElement(data, 'items')
item1 = ET.SubElement(items, 'item')
item2 = ET.SubElement(items, 'item')
item1.set('name','item1')
item2.set('name','item2')
item1.text = 'item1abc'
item2.text = 'item2abc'

# create a new XML file with the results
mydata = ET.tostring(data, encoding='unicode')
# print(type(mydata))
myfile = open("items2.xml", "w")
myfile.write(mydata)
