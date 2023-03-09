#!/usr/bin/python3
"""
The steam engine
"""
import json
from os import path


class FileStorage():
    """
    The storage for all files
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        :return: The dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        sets the object with a key <obj class name>.id in __objects
        """
        ob = obj.__class__.__name__ + "." + obj.id

    def save(self):
        """
        :return: serializes objects into a json file
        (path: __file_path)
        """
        dicti = {}
        for a, b in self.__objects.items():
            dicti = {a: b.to_dict()}
        with open(self.__file_path, mode="w") as f:
            json.dump(dicti, f)

    def reload(self):
        """
        :return: deserializes the JSON file
        """
        if path.isfile(self.__file_path):
            with open(self.__file_path) as f:
                dict = json.load(f)
                for a, b in dict.items():
                    cls = a["class"]
                    self.new(eval(cls)(**a))
