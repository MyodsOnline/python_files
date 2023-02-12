from wsgi import Framework
from url import Url
from view import View


class MyFirstView(View):
    def get(self, request):
        return 'i am a get'

    def post(self, request):
        return 'i am a post'


urls = [
    Url('homepage', MyFirstView)
]


app = Framework(urls)
