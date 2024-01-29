from Singleton import Singleton
import json


class GradeSheetParser(Singleton):
    def __init__(self, grade_sheet_path_text: str, grade_sheet_path_json: str):
        super().__init__()
        if grade_sheet_path_json is None:
            sheet = open(grade_sheet_path_text, "r")
            lines = sheet.readlines()
            for i in range(len(lines)):
                if '\n' in lines[i]:
                    lines[i] = lines[i].replace("\n", "")
            self.__name = lines[1]
            self.__id = lines[3]
            self.__catalog_type = lines[5]
            self.__degree_type = lines[7]
            self.__courses_completed = [line for line in lines[9:]]
        else:
            with open(grade_sheet_path_json, 'r') as f:
                data = json.load(f)
            self.__name = 'Israel Israeli'
            self.__id = '123456789'
            self.__catalog_type = '2020-2021'
            self.__degree_type = '3 years - Computer Science'
            #data['Completed courses'] look like this: {sem1: ['123456', '123457', '123458'], sem2: ['123459', '123460']}
            self.__courses_completed = [course for sem in data['Completed courses'].values() for course in sem]

    @staticmethod
    def get_instance():
        if GradeSheetParser._instance is None:
            raise Exception("GradeSheetParser instance does not exist")
        return GradeSheetParser._instance

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id

    def get_completed_courses_id(self) -> list[str]:
        return self.__courses_completed

    def get_catalog_type(self):
        return self.__catalog_type

    def get_degree_type(self):
        return self.__degree_type

    def delete_instance(cls):
        cls.__name = None
        cls.__id = None
        cls.__catalog_type = None
        cls.__degree_type = None
        cls.__courses_completed = None
        super().delete_instance()
