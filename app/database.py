import pymongo
from pymongo import MongoClient
# import config as cfg  # Uncomment in Production
import instance.config as cfg  # Uncomment in Development


class Database(object):
    DATABASE = None
    URI = cfg.DATABASE_URI

    @staticmethod
    def initialize():
        client = MongoClient(Database.URI, connect=False)
        Database.DATABASE = client['test']

    @staticmethod
    def insert(collection, data):
        if type(data) == dict:
            Database.DATABASE[collection].insert(data)
        elif type(data) == list:
            Database.DATABASE[collection].insert_many(data)

    @staticmethod
    def find_one(collection, query):
        print(Database.DATABASE.collection_names())
        if collection not in Database.DATABASE.collection_names():
            return False
        else:
            return Database.DATABASE[collection].find_one(query)

    @staticmethod
    def find_many(collection, query):
        if collection not in Database.DATABASE.collection_names():
            return False
        else:
            return Database.DATABASE[collection].find(query)

    @staticmethod
    def delete_one(collection, query):
        result = Database.DATABASE[collection].delete_one(query)
        return result.deleted_count

    @staticmethod
    def delete_many(collection, query):
        result = Database.DATABASE[collection].delete_many(query)
        return result.deleted_count

    @staticmethod
    def create_index(collection, field, unique=True):
        Database.DATABASE[collection].create_index([field, pymongo.ASCENDING], unique)

    @staticmethod
    def index_info(collection):
        return sorted(list(Database.DATABASE[collection].index_information()))
