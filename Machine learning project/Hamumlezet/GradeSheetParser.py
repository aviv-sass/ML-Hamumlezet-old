from Singleton import Singleton


class GradeSheetParser(Singleton):
    def __init__(self, grade_sheet_path: str):
        super().__init__()
        sheet = open(grade_sheet_path, "r")
        lines = sheet.readlines()
        for i in range(len(lines)):
            if '\n' in lines[i]:
                lines[i] = lines[i].replace("\n", "")
        self.__name = lines[1]
        self.__id = lines[3]
        self.__catalog_type = lines[5]
        self.__degree_type = lines[7]
        self.__courses_completed = [line for line in lines[9:]]

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
