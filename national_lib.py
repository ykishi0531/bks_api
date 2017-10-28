import urllib.request
import re
from xml.etree import ElementTree


api_url = 'http://iss.ndl.go.jp/api/sru?operation=searchRetrieve&query=isbn='


def nl_isbn(isbn):
	global api_url
	
	res = urllib.request.urlopen(api_url + isbn)
	xml_data = res.read()
	xml_data = re.sub(r'\d', 'l', xml_data)
	
	root = ElementTree.fromstring(xml_data)
	return xml_data

