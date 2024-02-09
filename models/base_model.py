#!/usr/bin/python3
import uuid
from datetime import datetime


class BaseModel:
    '''A class that defines all common attributes/methods for other classes'''
    def __init__(self, *args, **kwargs):
        ''' A function to initialise a unique id to a class and the time when instance is created or modified '''
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.fromisoformat(value))
                elif key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        '''A function to print the name of the class '''
        name = self.__class__.__name__
        return "[{}] ({}) {}".format(name, self.id, self.__dict__)

    def save(self):
        ''' A function to update the public attribute update_at '''
        self.updated_at = datetime.now()
            
    def to_dict(self):
        ''' A function that  returns a dictionary with all keys of __dict__ of the instance '''
        dic = self.__dict__.copy()
        dic['__class__'] = self.__class__.__name__
        dic['created_at'] = self.created_at.isoformat()
        dic['updated_at'] = self.updated_at.isoformat()
        return dic
