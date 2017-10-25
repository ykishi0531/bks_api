from bottle import route, response, abort, request
from bottle import get
from utils import *
from national_lib import *


@route('/', method='GET')
def home():
	abort(404)


@get('/api/')
def api_home():
	return get_items()


@route('/search/isbn/<isbn>', method='GET')
def search_isbn(isbn):
	return nl_isbn(isbn)
