import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'course'))
import course_db_interface


@course_db_interface.CourseDBInterface.register
class CourseDBService(course_db_interface.CourseDBInterface):
    ...
