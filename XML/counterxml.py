#!/usr/bin/env python3

import xml.etree.ElementTree as ET
tree = ET.parse('items.xml')
root = tree.getroot()

# total amount of items
print(len(root[0]))
