
'''
	Aim :: Using requests module for REST - Representational State Transfer

'''

import requests,urllib2

from lxml import html


buyer_Name = "//*[@title='buyer-name']/text()"
buyer_Cost = "//*[@class='item-price']/text()"
paginationList = "//*[@align='center']/a"
base_Url = "http://econpy.pythonanywhere.com/ex/001.html"


page = urllib2.urlopen(base_Url)
tree = html.fromstring(page.read())

print 'Buyers :: ', '\n\n', tree.xpath(buyer_Name), '\n\n','Cost :: ','\n\n',tree.xpath(buyer_Cost),'\n\n','Pages :: ','\n\n',tree.xpath(paginationList),'\n\n'


for items in tree.xpath(paginationList): 
	page = urllib2.urlopen(items.values()[0])
	tree = html.fromstring(page.read())
	print 'Buyers :: ', '\n\n', tree.xpath(buyer_Name), '\n\n','Cost :: ','\n\n',tree.xpath(buyer_Cost),'\n\n'

