from src.persistence.course.course_db_interface import CourseDBInterface
import sqlalchemy as db


class CourseDBService(CourseDBInterface):

    def __init__(self, engine):
        self.engine = engine

    def add_course(self, received_course):
        # engine = db.create_engine('postgresql://postgres:123456@localhost:5432/umsPython')
        engine = self.engine.get_engine()
        connection = engine.connect()
        metadata = db.MetaData()
        courses_table = db.Table('courses', metadata, autoload=True, autoload_with=engine)

        query = db.select([courses_table]).where(courses_table.columns.name == received_course.name)
        result_proxy = connection.execute(query)
        result_set = result_proxy.fetchall()
        print(result_set)
        if result_set:
            raise Exception("Course is already added")

        mx = received_course.max_students_number
        query = db.insert(courses_table).values(name=received_course.name, max_students_number=mx)
        result_proxy = connection.execute(query)

        query = db.select([courses_table]).where(courses_table.columns.name == received_course.name)
        result_proxy = connection.execute(query)
        result_set = result_proxy.fetchall()

        return result_set[0]
