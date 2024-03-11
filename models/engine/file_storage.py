#!/usr/bin/python3
import json

class FileStorage:
    """
    FileStorage class responsible for serializing instances to a JSON file and
    deserializing JSON files to instances.
    """

    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """
        Initialize FileStorage class.
        """
        self.reload()

    def all(self):
        """
        Returns the dictionary __objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id.
        
        Args:
            obj: Instance to be stored.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (__file_path).
        """
        with open(self.__file_path, 'w') as file:
            json.dump({key: obj.to_dict() for key, obj in self.__objects.items()}, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects if the file exists.
        """
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, obj_data in data.items():
                    class_name, obj_id = key.split('.')
                    if class_name == 'User':
                        obj = User(**obj_data)
                    else:
                        # Handle other classes if needed
                        obj = eval(class_name)(**obj_data)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
