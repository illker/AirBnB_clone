#!/usr/bin/python3
"""
Class FileStorage
"""

from models.base_model import BaseModel
import json

atri = {"BaseModel": BaseModel, "City": City}


class FileStorage():
    """that serializes instances to a JSON"""

    # string - path to the JSON file
    __file_path = "file.json"
    # dictionary - empty but will store all objects by <class name>.id
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        json_ob = {}
        for key in self.__objects:
            json_ob[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(json_ob, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as burger:
                beer = json.load(burger)
            for malta in beer:
                self.__objects[malta] = atri[beer[malta]["__class__"]](
                    beer[malta])
        except:
            pass
