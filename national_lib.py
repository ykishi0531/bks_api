import urllib.request


api_url = 'https://www.googleapis.com/books/v1/volumes?q=isbn:'


def nl_isbn(isbn):
	global api_url
	print(api_url)
	res = urllib.request.urlopen(api_url + isbn)
	
	return res.read()

