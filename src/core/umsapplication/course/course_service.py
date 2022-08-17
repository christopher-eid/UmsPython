import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'course'))
import course_interface

#IN OUR CASE HERE, WHEN WE CREATE AN INSTANCE OF UserService, we can use the method display_message even if we did not
#write it inside the service, since it is defined inside the interface. so this is how we did abstraction


#interface understanding from: https://realpython.com/python-interface/#formal-interfaces
#interface abstraction understood from: https://www.askpython.com/python/oops/abstraction-in-python


@course_interface.CourseInterface.register
class CourseService(course_interface.CourseInterface):
    ...
    # def display_message(self, message):
    #     return {"Message": message}
