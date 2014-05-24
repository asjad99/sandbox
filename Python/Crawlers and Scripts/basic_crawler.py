#!/usr/bin/env python
import re
import mechanize
import pickle
import StringIO
import io,json
import simplejson
from lxml import etree
from lxml.cssselect import CSSSelector
from lxml.etree import fromstring
from StringIO import StringIO

br = mechanize.Browser()
page = br.open("http://www.mrporter.com/Shop/Clothing/Coats_and_Jackets")
page_source = page.read()

 #---test html---
#broken_html = "<html><head><title>test<body><h1><div class=\"designer\"> <p>text </p></div>page title</h3>"  

html = etree.HTML(page_source)
#result = etree.tostring(html, pretty_print=True, method="html")


sel_product_title = CSSSelector("div.designer span.product-title")
sel_product_img = CSSSelector("div.product-images div.product-image img")
sel_product_url = CSSSelector("div.product-images div.product-image a")
sel_product_price = CSSSelector("div.price-container p")

#pass HTML tree to the selectors
h1 = sel_product_title(html) 
h2 = sel_product_url(html)
h3 = sel_product_img (html)
h4 = sel_product_price(html)

all_products_info =[[0,1,2]]
print all_products_info
product_texts = []
product_imgs = []
product_urls = []
product_prices = []

#Extract relevent information
for e in h1: 
	product_texts.append(e.text)
for e1 in h2: 
	product_urls.append("http://www.mrporter.com" + e1.get('href'))	#appending of home page URL
for e2 in h3: 
	product_imgs.append(e2.get('src'))
for e3 in h4: 
	product_prices.append(e3.text)

#For saving the data to disk in JSON format

list_of_objects=[]

for i in range(15):
	dic_products = {}
	dic_products['product_text'] = product_texts[i]
	dic_products['product_url']  = product_urls[i]
	dic_products['product_img'] = product_imgs[i]
	dic_products['product_price'] = product_prices[i]
	list_of_objects.append(dic_products);

f = open("product_data.txt","w")
simplejson.dump(list_of_objects,f)

print simplejson.dumps(list_of_objects)       

print("done")