#!/usr/bin/python3
"""
Has the FileStorage class.
"""

import os
import json


class FileStorage():
    """
    Serializes instances to a JSON file and
    deserializes JSON file to instances.
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path).
        """
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            new_objects = {}
            for k, v in FileStorage.__objects.items():
                new_objects[k] = v.to_dict()
            json.dump(new_objects, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists.
        Otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised).
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                new_dict = json.load(file)
                for k, v in new_dict.items():
                    class_name = new_dict[k].pop('__class__')
                    FileStorage.__objects[k] = eval(class_name)(**v)
