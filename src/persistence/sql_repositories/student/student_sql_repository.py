from src.domain.abstract_sql_repositories.student.abstract_student_sql_repository import AbstractStudentSqlRepository
import sqlalchemy as db
import pandas as pd


class StudentSqlRepository(AbstractStudentSqlRepository):

    def __init__(self, engine):
        self.engine = engine

    def get_student(self, received_name: str, received_email: str) -> list:
        engine = self.engine.get_engine()
        connection = engine.connect()
        metadata = db.MetaData()
        users_table = db.Table('users', metadata, autoload=True, autoload_with=engine)

        query = db.select([users_table]).where(users_table.columns.name == received_name and users_table.columns.email == received_email
                                               and users_table.columns.role_id == 3)
        result_proxy = connection.execute(query)
        result_set = result_proxy.fetchall()
        return result_set

    def add_student(self, received_name:str, received_email: str):
        # engine = db.create_engine('postgresql://postgres:123456@localhost:5432/umsPython')
        engine = self.engine.get_engine()
        connection = engine.connect()
        metadata = db.MetaData()
        users_table = db.Table('users', metadata, autoload=True, autoload_with=engine)

        query = db.insert(users_table).values(name=received_name, email=received_email, role_id=3)
        result_proxy = connection.execute(query)

        #get the row we added from the db to get its auto incremented id
        query = db.select([users_table]).where(users_table.columns.name == received_name and users_table.columns.email == received_email)
        result_proxy = connection.execute(query)
        result_set = result_proxy.fetchall()

        return result_set[0]

    def get_all_students(self) -> pd.DataFrame:
        engine = self.engine.get_engine()
        connection = engine.connect()
        metadata = db.MetaData()
        users_table = db.Table('users', metadata, autoload=True, autoload_with=engine)

        query = db.select([users_table]).where(users_table.columns.role_id == 3)
        result_proxy = connection.execute(query)
        result_set = result_proxy.fetchall()  # fetches all the data we have

        df = pd.DataFrame(result_set)
        return df
