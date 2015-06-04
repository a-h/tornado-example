import json
from bson import json_util
from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application, url
from application_repository import ApplicationRepository


class ApplicationHandler(RequestHandler):
    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs)
        if False:
            # These are the fields, but initialize is called
            # prior to __init__
            self.application_repository = None

    def initialize(self, application_repository):
        # injection of arguments from the handler configuration is done
        # here.
        assert isinstance(application_repository, ApplicationRepository)
        self.application_repository = application_repository

    def data_received(self, chunk):
        pass

    def get(self):
        application_list = self.application_repository.list_applications()
        j = json.dumps(application_list, default=json_util.default)
        self.write(j)

    def set_default_headers(self):
        self.set_header('Content-Type', 'application/json')


def make_app():
    return Application(get_handlers())


def get_handlers():
    return [
        url(r"/application/?", ApplicationHandler, dict(application_repository=ApplicationRepository()))
    ]


def main():
    app = make_app()
    app.listen(8888)
    IOLoop.current().start()


if __name__ == "__main__":
    main()
