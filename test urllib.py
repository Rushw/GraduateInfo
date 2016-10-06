import urllib
from bs4 import BeautifulSoup
import re
import HTMLParser
responce = urllib.urlopen(
                'http://202.119.4.150/nstudent/ggxx/xsggxxinfo.aspx?xh=101000')
text = responce.read().decode('utf-8')
print text
#
#
# class LinksParser(HTMLParser.HTMLParser):
#     def __init__(self):
#         HTMLParser.__init__(self)
#         self.recording = 0
#         self.data = []
#
#     def handle_starttag(self, tag, attributes):
#         if tag != 'span':
#             return
#         if self.recording:
#             self.recording += 1
#             return
#         for name, value in attributes:
#             if name == 'id' and value == 'lblxh':
#                 break
#         else:
#             return
#         self.recording = 1
#
#     def handle_endtag(self, tag):
#         if tag == 'span' and self.recording:
#             self.recording -= 1
#
#     def handle_data(self, data):
#         if self.recording:
#             self.data.append(data)
#
# p=LinksParser
# p.feed(text)
# p.close()
# print p.data

soup = BeautifulSoup(text,"html.parser")
# tag=soup.span
# print(tag.string)
print soup.find('span',{'id':'lblxnbh'}).text