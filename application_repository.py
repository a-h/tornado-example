from bson import ObjectId
from motor import MotorClient
from tornado import gen
from tornado.gen import Return


class ApplicationRepository:
    def __init__(self):
        self.client = MotorClient()

    @gen.coroutine
    def list_applications(self):
        db = self.client.applications
        cursor = db.applications.find()
        result = yield cursor.to_list(1000)
        return result

    @gen.coroutine
    def insert_application(self, application):
        db = self.client.applications

        return str((yield db.applications.insert(application)))

    @gen.coroutine
    def get_application(self, application_id):
        db = self.client.applications
        cursor = db.applications.find({"_id": ObjectId(application_id)})
        return (yield cursor.to_list(1000))

    @gen.coroutine
    def clear_all(self):
        db = self.client.applications
        applications = db.applications

        yield applications.drop()
