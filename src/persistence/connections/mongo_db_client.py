import pymongo


class MongoDBClient:
    def get_client(self):
        my_client = pymongo.MongoClient("mongodb://mongoadmin:123456@localhost")
        my_db = my_client["umsPythonMongo"]
        return my_db
