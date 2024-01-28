from abc import ABC
from exceptions import *


class Singleton(ABC):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._initialized = False
        return cls._instance

    def __init__(self):
        if not self._initialized:
            self._initialized = True
        else:
            raise SingletonAlreadyExistError("Singleton already exist.")

    @classmethod
    def get_instance(cls, *args, **kwargs):
        if cls._instance is None:
            raise SingletonDoesNotExistError("Singleton does not exist.")
        return cls._instance

    @classmethod
    def delete_instance(cls):
        if cls._instance is not None:
            cls._instance = None
        else:
            raise SingletonDoesNotExistError("Singleton does not exist.")