from bson import ObjectId
from pymongo import MongoClient

class ApplicationRepository:
    def __init__(self):
        self.client = MongoClient()

    def list_applications(self):
        db = self.client.applications
        applications = db.applications
        return list(applications.find())

    def insert_application(self, application):
        db = self.client.applications
        applications = db.applications

        return applications.insert_one(application).inserted_id

    def get_application(self, application_id):
        db = self.client.applications
        applications = db.applications

        return list(applications.find({"_id": ObjectId(application_id)}))

    def clear_all(self):
        db = self.client.applications
        applications = db.applications

        applications.remove()
