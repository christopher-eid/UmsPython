from src.application.student_cqrs.commands.add_students_excel.abstract_add_students_excel_service import AbstractAddStudentsExcelService
from src.application.exceptions.already_available_exception import AlreadyAvailableException
from src.application.models.response_models.status_model import StatusModel
import os
import shutil
from pathlib import Path
import pandas as pd
from numpy import random

class AddStudentsExcelService(AbstractAddStudentsExcelService):

    def __init__(self, db):
        self.db = db

#how to save files with fast api :
#inspired from: https://stackoverflow.com/questions/63580229/how-to-save-uploadfile-in-fastapi
    def add_students(self, received_excel):
        destination_path = os.getcwd();
        random_name = random.randint(1, 1000000)
        string_name = str(random_name) + ".xlsx"
        des_path = Path(os.path.join(destination_path, "src", "application", "stored_files", string_name))
        print(des_path)
        with des_path.open("wb") as buffer:
            shutil.copyfileobj(received_excel.file, buffer)
        df = pd.read_excel(des_path)
        students_added = []
        # try:

        for index, row in df.iterrows():
            if self.db.get_student(row["name"], row["email"]):
                raise AlreadyAvailableException("Student already existing")
            new_student = self.db.add_student(row["name"], row["email"])
            students_added.append(new_student)
        des_path.unlink()
        return students_added  # return the dataframe of students we added, without their ids and role ids
        #
        # except AlreadyAvailableException:
        #     return StatusModel(success=False, description="Student Already Available")
        #



