import sqlalchemy as db

class DBEngine:
    def get_engine(self):
        engine = db.create_engine('postgresql://postgres:123456@localhost:5432/umsPython')
        return engine
