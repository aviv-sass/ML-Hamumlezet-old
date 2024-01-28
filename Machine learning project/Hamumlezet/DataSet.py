class DataSet:
    __instance = None

    def __init__(self):
        #student_sict is a dictionary that contains all the students in the data set sorted by their completed points
        self.student_dct = dict()

        if DataSet.__instance is None:
            DataSet.__instance = self
        else:
            raise Exception("DataSet instance already exists")

    @staticmethod
    def get_instance():
        if DataSet.__instance is None:
            raise Exception("DataSet instance does not exist")
        return DataSet.__instance

    def add_student_dct(self, key, student):
        if key in self.student_dct:
            self.student_dct[key].append(student)
        else:
            self.student_dct[key] = [student]

