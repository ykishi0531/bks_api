import urllib.request


api_url = 'http://iss.ndl.go.jp/api/sru?operation=searchRetrieve&query=isbn='


def nl_isbn(isbn):
	global api_url
	print(api_url)
	res = urllib.request.urlopen(api_url + isbn)
	
	return res.read()

