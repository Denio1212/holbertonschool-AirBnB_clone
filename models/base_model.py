#!usr/bin/python3
"""
Houses the base model of the other classes
"""
import models
import uuid
from datetime import datetime
import json
from os import path


class BaseModel():
    """
    base of goods
    """
    def __init__(self, *args, **kwargs):
        """
        constructor
        :param id: id of object instance
        :param created_at: where it was created at
        :param updated_at: where it was updated at
        """
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        prints out the name the id and the dict of the object
        """
        name = self.__class__.__name__
        return "[{}] ({}) {}".format(name, self.id, self.__dict__)

    def save(self):
        """
        :return: updates the current datetime by modifying the updated_at variable
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of
        __dict__ of the instance
        """
        d = {}
        for k, v in self.__dict__.items():
            if k == "created_at" or k == "updated_at":
                d[k] = datetime.isoformat(v)
            else:
                d[k] = v
        d["__class__"] = self.__class__.__name__
        return d