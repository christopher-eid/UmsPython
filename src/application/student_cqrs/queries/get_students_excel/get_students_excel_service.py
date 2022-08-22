from src.application.student_cqrs.queries.get_students_excel.abstract_get_students_excel_service import AbstractGetStudentsExcelService
from src.application.exceptions.already_available_exception import AlreadyAvailableException
from src.domain.dtomodels.status_model import StatusModel
import os
import shutil
from pathlib import Path
from numpy import random
from fastapi.responses import FileResponse
from threading import Timer

'''
how to return downloadable files:
https://www.tutorialsbuddy.com/python-fastapi-download-files
'''


class GetStudentsExcelService(AbstractGetStudentsExcelService):

    def __init__(self, db):
        self.db = db

    def get_students(self):
        students_dataframe = self.db.get_all_students()

        destination_path = os.getcwd()
        random_name = random.randint(1, 1000000)
        string_name = str(random_name) + ".xlsx"
        string_dest_path = os.path.join(destination_path, "src", "application", "stored_files", string_name)
        dest_path = Path(string_dest_path)
        students_dataframe.to_excel(dest_path)

        '''we are returning the excel file that we created and created a timer so our file is deleted on our server after it has been returned
        
            -file response will read from a specific path when called and return the file read
            -path.unlink is used to delete the file from a certain path
            -background is to apply it after returning the file
            -we should dest_path.unlink WITHOUT THE PARANTHESES, or it will be called before returning file'''

        file_res = FileResponse(path=string_dest_path, filename=string_dest_path)
        s = Timer(10.0, dest_path.unlink)

        s.start()
        #
        # background = dest_path.unlink
        # print("File " + string_name + " removed")

        return file_res
