#!/usr/bin/python3
"""
The steam engine
"""
import json
from os import path
import os


class FileStorage:
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
        with open(FileStorage.__file_path, 'w') as f:
            new_dict = {}
            x = self.all()
            for element in x:
                new_dict[element] = x[element].to_dict()
            f.write(json.dumps(new_dict))
        return True

    def reload(self):
        """
        deserializes the Json file
        """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as f:
                content = f.read()
                if len(content) != 0:
                    obj = json.loads(content)
                    for key, value in obj.items():
                        value = eval(value['__class__'])(**value)
                        FileStorage.new(self, value)
        return True
