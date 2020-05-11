import xml.etree.ElementTree as ET

for event, ele in ET.iterparse("input.xml"):
    # print(ele, 'jkjkjkjkjkjkjjkjkj')
    for elem in ele.iter():
        print(elem.tag)
        if elem.tag =="product":
            print(elem.tag,"lklklklklklklkl")

# for child in root:
#     mainlevel = child.tag
#     xmltocsv = ''
#     for elem in root.iter():
#         if elem.tag == root.tag:
#             continue
# tree = ET.parse(r"input.xml")
# root = tree.getroot()
# tag = root.tag
# att = root.attrib
#
# print(root,'\n',tag,'\n',att)