#!/usr/bin/env python

import urllib2
from xml.dom import minidom
from xml.etree import ElementTree as ET 

url = urllib2.urlopen('http://www.nbp.pl/Kursy/xml/LastA.xml')
#xml = minidom.parse(url)
xml = ET.parse(url)
url.close()

waluty = {}
limit = ['EUR', 'USD']

for poz in xml.getiterator('pozycja'):
	d = dict([(c.tag, c.text) for c in poz.getchildren()])
	if d['kod_waluty'] not in limit: continue
	waluty[d['kod_waluty']] = d
	d['kurs_sredni'] = float(d['kurs_sredni'].replace(',','.'))


for k, v in waluty.iteritems():
	print k, v['kurs_sredni']


