import json
from wsgiref.simple_server import make_server
import json


def home_view():
    with open('wsgi/tmp.json', 'r', encoding='utf-8') as json_data:
        data = json_data.read()
        parsed_data = json.loads(data)
        print(parsed_data)
        text = json.dumps(parsed_data)
        print(text)
        text.encode('utf-8')
    return '200 OK', text


def index_view():
    return '200 OK', '<h1>Index page</h1>'


def test_view():
    return '200 OK', '<h1>Test page</h1>'


def page_not_found_404():
    return '404 WHAT', '<h1>Page not found</h1>'


routes = {
    '/': home_view,
    '/index/': index_view,
    '/test/': test_view,
}


class Application:
    def __init__(self, routers):
        self.routes = routers

    def __call__(self, environ, start_response):
        print(environ)
        path = environ['PATH_INFO']

        if path in self.routes:
            view = self.routes[path]
        else:
            view = page_not_found_404

        code, body = view()
        start_response(code, [('Content-Type', 'text/html')])
        print(type(body))
        return [body.encode('utf-8')]


app = Application(routes)


with make_server('', 8000, app) as httpd:
    print('Server star')
    httpd.serve_forever()


if __name__ == '__main__':
    home_view()
