#!usr/bin/python3
"""
file storage
"""
from models.base_model import BaseModel
import os
import json
from os import path
from models.user import User


class FileStorage:
    '''Class used to manipulate json obj'''
    __file_path = "file.json"
    __objects = {}

    # Returns all objects stored in FileStorage
    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        k = obj.__class__.__name__ + "." + obj.id
        self.__objects[k] = obj

    def save(self):
        """Serialises __objects to the JSON file (path: __file_path)"""
        d = {k: v.to_dict()
             for k, v in self.__objects.items()}
        with open(self.__file_path, mode='w') as f:
            json.dump(d, f)

    def reload(self):
        """Deserialises the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing. If the file doesn’t
        exist, no exception should be raised)
        """
        if path.isfile(self.__file_path):
            with open(self.__file_path) as f:
                d = json.load(f)
                for k, v in d.items():
                    cls = v["__class__"]
                    self.new(eval(cls)(**v))

    def file_path():
        return FileStorage.__file_path
