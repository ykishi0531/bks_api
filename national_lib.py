import urllib.request
import re
import xml.etree.ElementTree as ET


api_url = 'http://iss.ndl.go.jp/api/sru?operation=searchRetrieve&query=isbn='


def nl_isbn(isbn):
	global api_url
	
	res = urllib.request.urlopen(api_url + isbn)
	xml_data = res.read()
	xml = '<?xml version="1.0" encoding="UTF-8"><test>aaa</test>'
	# ET.fromstring(xml)
	
	root = ET.fromstring(xml_data)
	return root.tag

