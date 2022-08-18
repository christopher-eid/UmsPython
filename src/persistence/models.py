from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
#check out note file written in WORK> inmindAcademy > ONBOARDING > discoveringLibraries to see how to use alembic
#to build models, check out https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_orm_building_relationship.htm

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    role_id = Column(Integer, ForeignKey('roles.id'))
    email = Column(String)


class Role(Base):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True)
    name = Column(String)


class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    max_students_number = Column(Integer)


class TeacherPerCourse(Base):
    __tablename__ = 'teacher_per_course'

    id = Column(Integer, primary_key=True)
    teacher_id = Column(Integer, ForeignKey('users.id'))
    course_id = Column(Integer, ForeignKey('courses.id'))


class ClassEnrollment(Base):
    __tablename__ = 'class_enrollment'

    id = Column(Integer, primary_key=True)
    class_id = Column(Integer, ForeignKey('teacher_per_course.id'))
    student_id = Column(Integer, ForeignKey('users.id'))
#we can add sessiontime and teacher per course per session time in future versions if i wanted
#but during last project, serge told me that this part of the database is not very correct so i will not add it now