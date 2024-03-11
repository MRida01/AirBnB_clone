#!/usr/bin/python3
import uuid
from datetime import datetime

class BaseModel:
    """
    BaseModel class representing a base model with common attributes and methods.

    Attributes:
        id (str): A unique identifier generated using UUID.
        created_at (datetime): The datetime when the instance is created.
        updated_at (datetime): The datetime when the instance is last updated.
    """

    def __init__(self):
        """
        Initializes a new instance of the BaseModel class.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.

        Returns:
            str: A string containing class name, id, and dictionary representation of the instance.
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the updated_at attribute with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Converts the BaseModel instance to a dictionary.

        Returns:
            dict: A dictionary containing all instance attributes in a serialized format.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
    
