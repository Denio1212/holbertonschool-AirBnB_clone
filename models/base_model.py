#!usr/bin/python3
"""
Houses the base model of the other classes
"""
import models
import uuid
from datetime import datetime



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
        if kwargs:
            for i, j in kwargs.items():
                if i == "created_at" or i == "updated_at":
                    setattr(self, i, datetime.strftime(j, "%Y-%m-%d:%H.%M.%S.%f"))
                elif i == "__class__":
                    continue
                else:
                    setattr(self, i, j)
        else:
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
        models.storage.save()

    def to_dict(self):
        """
        :return: dictionary containing all keys/values
        isoformat -> makes the datetime into a string in the ISO date format.
        """
        dict = {}
        for i, n in self.__dict__.items():
            if i == "created_at" or n == "updated_at":
                dict[i] = datetime.isoformat(n)
            else:
                dict[i] = n
        dict["__class__"] = self.__class__.__name__
        return dict

