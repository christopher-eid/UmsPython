from src.domain.abstract_nosql_repositories.course.abstract_course_nosql_repository import AbstractCourseNoSqlRepository


class CourseNoSqlRepository(AbstractCourseNoSqlRepository):

    def __init__(self, mongo_db_client):
        self.mongo_db_client = mongo_db_client

    def get_course(self, received_name: str) -> list:
        # my_client = pymongo.MongoClient("mongodb://mongoadmin:123456@localhost")
        # my_db = my_client["umsPythonMongo"]
        my_db = self.mongo_db_client.get_client()
        my_collection = my_db["courses"]

        my_query = {"name": received_name}

        result = my_collection.find(my_query)
        found_rows = []
        for x in result:
            found_rows.append(x)
        print(found_rows)
        return found_rows

    def add_course(self, received_course) -> dict:
        # my_client = pymongo.MongoClient("mongodb://mongoadmin:123456@localhost")
        # my_db = my_client["umsPythonMongo"]
        my_db = self.mongo_db_client.get_client()
        my_collection = my_db["courses"]

        #in order to keep the id as int, I get the max id that we reached, i increment it and insert it with the new course i am adding
        x = my_collection.find().sort('_id', -1).limit(1)
        list_from_top = []
        for i in x:
            list_from_top.append(i)
            print(x)
        if list_from_top:
            max_row = list_from_top[0]
            max_id = max_row["_id"]
        else:
            max_id = 0

        new_max_id = max_id + 1

        mx = received_course.max_students_number
        course_to_add = {"_id": new_max_id, "name": received_course.name, "max_students_number": mx}

        #adding the new course
        x = my_collection.insert_one(course_to_add)

        #replace _id attribute name with id since this is this is the name we are using in our project
        #x.inserted_id is the id of the object we added in the collection, we used inserted_id to check if the id we actually added is correct
        added_row = {"id": x.inserted_id, "name": received_course.name, "max_students_number": mx}

        return added_row
