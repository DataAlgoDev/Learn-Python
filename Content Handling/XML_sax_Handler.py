import xml.sax # Simple API for XML
'''
SAX is an event-driven, streaming parser that processes the document sequentially and is more memory-efficient for large files.
'''

# class BookHandler(xml.sax.ContentHandler):
#     def startElement(self, name, attrs):
#         self.curr = name
#         if name == "book":
#             self.id = attrs['id']
#             print(f"Book ID\t: {self.id}")
            
#     def characters(self, content):
#         # print(f"Content : {content}")
#         if self.curr == "author":
#             self.author = content
#         elif self.curr == "title":
#             self.title = content
#         elif self.curr == "genre":
#             self.genre = content
#         elif self.curr == "price":
#             self.price = content
#         elif self.curr == "publish_date":
#             self.publish_date = content
#         elif self.curr == "description":
#             self.description = content

#     def endElement(self, name):
#         # print(f"End name : {name}")
#         if name == "author":
#             print(f"Author\t\t\t: {self.author}")
#         elif name == "title":
#             print(f"Title\t\t\t: {self.title}")
#         elif name == "genre":
#             print(f"Genre\t\t\t: {self.genre}")
#         elif name == "price":
#             print(f"Price\t\t\t: {self.price}")
#         elif name == "publish_date":
#             print(f"Publish_date\t: {self.publish_date}")
#         elif name == "description":
#             print(f"Description\t\t: {self.description}", end = "\n\n")


class BookHandler(xml.sax.ContentHandler):
    def startElement(self, name, attrs):
        self.curr = name
        if name == "book":
            self.id = attrs['id']
            
    def characters(self, content):
        # print(f"Content : {content}")
        if self.curr == "author":
            self.author = content
        elif self.curr == "title":
            self.title = content
        elif self.curr == "genre":
            self.genre = content
        elif self.curr == "price":
            self.price = content
        elif self.curr == "publish_date":
            self.publish_date = content
        elif self.curr == "description":
            self.description = content

    def endElement(self, name):
        # print(f"End name : {name}")
        if name == "title":
            print(f"Title\t\t\t: {self.title}")
            print(f"Book ID\t\t\t: {self.id}")
            print(f"Author\t\t\t: {self.author}")
        elif name == "genre":
            print(f"Genre\t\t\t: {self.genre}")
        elif name == "price":
            print(f"Price\t\t\t: {self.price}")
        elif name == "publish_date":
            print(f"Publish_date\t: {self.publish_date}")
        elif name == "description":
            print(f"Description\t\t: {self.description}", end = "\n\n")
        self.curr =""   # Since there can be new lines white spaces in the content

handler = BookHandler()
parser = xml.sax.make_parser()
parser.setContentHandler(handler)
parser.parse("Python-References/Content Handling/Books.xml")


# when a new book id is encountered print the book details in below format
#
# Title         : XML Developer's Guide ---
# Book Id       :
# Author        : 
# genre         : 
# Price         :
# Publish Date  :
# Description   :
#
