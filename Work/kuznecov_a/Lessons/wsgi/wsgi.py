from request import Request


class Framework:

    def __init__(self, urls):
        self.urls = urls

    def __call__(self, environ, start_response):
        request = Request(environ)

        start_response('200 OK', [('Content-Type', 'text/html')])
        return [b'Hello world']

    def _get_view(self, request):
        path = request.path
        for url in self.urls:
            if url.path == path:
                return url.view
            else:
                return None

    def _get_response(self, request, view):
        if hasattr(view, request.method):
            return getattr(view, request.method)(view, request)
        else:
            return 'Not allowed'