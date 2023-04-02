#!usr/bin/python3
"""
Houses the base model of the other classes
"""
import models
import uuid
from datetime import datetime


class BaseModel:
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
                    setattr(self, i, datetime.strptime(j, "%Y-%m-%dT%H:%M:%S.%f"))
                elif i == "__class__":
                    continue
                else:
                    setattr(self, i, j)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    # String representation of instance
    def __str__(self):
        string = "[{}]".format(self.__class__.__name__)
        string += " ({}) {}".format(self.id, self.__dict__)
        return string

    # Updates datetime and calls storage.save method
    def save(self):
        self.updated_at = datetime.utcnow()
        models.storage.save()
        return self.updated_at

    # Json serialisation dict representation
    def to_dict(self):
        new_d = {}
        new_d = self.__dict__.copy()
        new_d["__class__"] = str(self.__class__.__name__)
        new_d['created_at'] = self.created_at.isoformat()
        new_d['updated_at'] = self.updated_at.isoformat()
        return new_d
