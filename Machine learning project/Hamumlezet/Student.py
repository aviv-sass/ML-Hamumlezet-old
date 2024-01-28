from State import State
from Singleton import Singleton


class Student(Singleton):
    def __init__(self, name : str, id: str, catalog: str, degree_type: str, state: State):
        super().__init__()
        self.__name = name
        self.__id = id
        self.__catalog = catalog  # "2022-2023"
        self.__degree_type = degree_type  # "Computer Science"
        self.__state = state

    @staticmethod
    def get_instance():
        if Student._instance is None:
            raise Exception("Student instance does not exist")
        return Student._instance

    def get_name(self) -> str:
        return self.__name

    def get_id(self) -> str:
        return self.__id

    def get_catalog(self) -> str:
        return self.__catalog

    def get_degree_type(self) -> str:
        return self.__degree_type

    def set_new_state(self, new_state: State) -> None:
        self.__state = new_state

    def is_graduate(self) -> bool:
        return self.__state.is_graduate()

    def get_state(self) -> State:
        return self.__state

    def delete_instance(cls):
        cls.__name = None
        cls.__id = None
        cls.__catalog = None
        cls.__degree_type = None
        cls.__state = None
        super().delete_instance()