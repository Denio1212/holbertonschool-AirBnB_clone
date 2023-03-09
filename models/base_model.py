#!usr/bin/python3
"""
Houses the base model of the other classes
"""
import uuid

import models
import uuid
from datetime import datetime


class BaseModel:
    """
    base of goods
    """
    def __init__(self, id, created_at, updated_at):
        """
        constructor
        :param id: id of object instance
        :param created_at: where it was created at
        :param updated_at: where it was updated at
        """
        updated = datetime.now()
        ided = str(uuid.uuid4())
        created = datetime.now()
        self.id = ided
        self.created_at = created
        self.updated_at = updated

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
        return self.updated_at

    def to_dict(self):
        """
        :return: dictionary containing all keys/values
        isoformat -> makes the datetime into a string in the ISO date format.
        """
        dict = {}
        for idx, n in self.__dict__.items():
            if idx == "created_at" or n == "updated_at":
                dict[idx] = datetime.isoformat(n)
            else:
                dict[idx] = n
        dict["__class__"] = self.__class__.__name__
        return dict

