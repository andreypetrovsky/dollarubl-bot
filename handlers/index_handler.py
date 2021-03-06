from tornkts.base.server_response import ServerError
from tornkts.handlers import BaseHandler
from os import path
from settings import options


class IndexHandler(BaseHandler):
    @property
    def get_methods(self):
        return {
            'index': self.index
        }

    @property
    def default_get_method(self):
        return 'index'

    def index(self):
        template = path.join(options.static_root, 'index.html')

        if path.isfile(template) is False:
            raise ServerError('not_found')

        with open(template, 'r') as file:
            result = file.read()
            self.set_header('Content-type', 'text/html')
            self.write(result, nocontenttype=True)
