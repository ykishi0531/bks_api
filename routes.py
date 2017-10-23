from bottle import route, response, abort, request
from bottle import get
from utils import *

@route('/', method='GET')
def home():
    abort(404)

@get('/api/')
def api_home():
    return get_items()
