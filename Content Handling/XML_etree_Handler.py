# import os
import xml.etree.ElementTree as ET

r"""
Expanding linux home directory shorthand
----------------------------------------
filepath = os.path.expanduser(r"~\OneDrive\Desktop\Learning\VSCode\Python-References\Content Handling\Books.xml")
tree = ET.parse(filepath)

Linux absolute path convention
------------------------------
tree = ET.parse("c:/Users/ajayn/OneDrive/Desktop/Learning/VSCode/Python-References/Content Handling/Books.xml")

Path in windows convention(raw string literal)
----------------------------------------------
tree = ET.parse(r"C:\Users\ajayn\OneDrive\Desktop\Learning\VSCode\Python-References\Content Handling\Books.xml")
"""  

tree = ET.parse('Python-References/Content Handling/Books.xml')
# Loads the whole content into memory

root = tree.getroot()

print("Root Element : ", root.tag)
print("Books in library:\n")

for child in root:
    print(f"Title\t: {child[1].text}")
    print(f"Author\t: {child[0].text}")
    print(f"Genre\t: {child[2].text}")
    print(f"Price\t: {child[3].text}", end = "\n\n")

book = root.find(".//book[@id='bk101']")
book_price = book.find('price')
book_price.text ='45'

tree.write('Python-References/Content Handling/Books.xml') # Overwriting the same file
ET.dump(root)
