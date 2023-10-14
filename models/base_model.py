#!/usr/bin/python3
"""
Has the Base Class.
"""

import datetime
import uuid
from models import storage


class BaseModel():
    """
    Defines all common attributes/methods for other classes.
    """

    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        if len(kwargs) == 0:
            storage.new(self)
        elif len(kwargs) > 0:
            for k, v in kwargs.items():
                if k == '__class__':
                    continue
                if k in ('created_at', 'updated_at'):
                    v = datetime.datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                self.__dict__[k] = v

    def __str__(self):
        """
        Called when a Base Object is called.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the public instance attribute \
        updated_at with the current datetime.
        """
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values \
            of __dict__ of the instance.
        """
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
