import json
from os.path import isfile
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.state import State


class FileStorage:
    ''' Class attributes to hold path to the JSON file
        but also an empty dictionary to be used in storing classname.id
    '''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        ''' A function to returns the dictionary of ids '''
        return FileStorage.__objects

    def new(self, obj):
        ''' A function that the object with key of ids in __obj dictionary '''
        key ="{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj
        self.save()

    def save(self):
        """Serialize and save the objects to the JSON file."""
        filename = FileStorage.__file_path
        
        if FileStorage.__objects is not None:
            serialized_objects = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
            
            with open(filename, 'w', encoding='utf-8') as file:
                json.dump(serialized_objects, file)

    def reload(self):
        ''' Deserialize the JSON file back to __objects if the file exists, otherwise, do nothing. '''
        if isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    class_obj = globals().get(class_name)
                    if class_obj:
                        obj_instance = class_obj(**value)
                        FileStorage.__objects[key] = obj_instance
