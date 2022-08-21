from mediatr import Mediator
from src.application.student_cqrs.commands.add_students_excel_mediatr.add_students_excel_command import AddStudentsExcelCommand


@Mediator.handler
class AddStudentsExcelCommandHandler:

    def __init__(self, db_service):
        self.db_service = db_service

    def handle(self, request: AddStudentsExcelCommand):
        return self.db_service.get_course("ood") #CHANGE NAME

#check container, command file and students endpoint

# DO NOT FORGET TO ADD Mediator.register_handler(GetArrayQueryHandler) inside the container to register the handler