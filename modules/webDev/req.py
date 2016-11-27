
'''
	Aim :: Using requests module for REST - Representational State Transfer

'''

import requests, httplib,json

from lxml import html


buyer_Name = "//*[@title='buyer-name']/text()"
buyer_Cost = "//*[@class='item-price']/text()"
paginationList = "//*[@align='center']/a"
base_Url = "http://econpy.pythonanywhere.com/ex/001.html"

page = requests.get(base_Url)
tree = html.fromstring(page.content)

print 'Buyers :: ', '\n\n', tree.xpath(buyer_Name), '\n\n','Cost :: ','\n\n',tree.xpath(buyer_Cost),'\n\n','Pages :: ','\n\n',tree.xpath(paginationList),'\n\n'

for items in tree.xpath(paginationList): 
	page = requests.get(items.values()[0])
	tree = html.fromstring(page.content)
	print 'Buyers :: ', '\n\n', tree.xpath(buyer_Name), '\n\n','Cost :: ','\n\n',tree.xpath(buyer_Cost),'\n\n'