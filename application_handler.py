import json
from bson import json_util
from tornado import gen
from tornado.web import RequestHandler
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

    @gen.coroutine
    def get(self, application_id=None):
        if application_id:
            application = yield self.application_repository.get_application(application_id)
            j = json.dumps(application, default=json_util.default)
            self.write(j)
        else:
            application_list = yield self.application_repository.list_applications()
            j = json.dumps(application_list, default=json_util.default)
            self.write(j)

    @gen.coroutine
    def put(self):
        data = json.loads(self.request.body.decode('utf-8'))
        application_id = yield self.application_repository.insert_application(data)
        self.write(json.dumps({"id": application_id,}))

    def set_default_headers(self):
        self.set_header('Content-Type', 'application/json')
