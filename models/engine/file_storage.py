import json
from os.path import isfile


class FileStorage:
    ''' Class attributes to hold path to the JSON file
        but also an empty dictionary to be used in storing classname.id
    '''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        ''' A function to returns the dictionary of ids '''
        return FileStorage.__objects

    def new(self):
        ''' A function that the object with key of ids in __obj dictionary '''
        key ="{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        ''' A function to serialize __obj dictionary
            to the JSON file by the path __file_path
        '''
        serialized_objects = {key: obj.to_dict() for key, obj in FileStorage.__objects
        with open(FileStorage.__file_path, 'w') as file:
                              json.dump(serialied_objects, file)

    def reload(self):
        ''' A function that deselializes back JSON file to
            __object. but if and only if file_path exist otherwise do nothing
        '''
        if isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    class_obj = globals()[class_name]
                    obj_instance = class_obj(**value)
                    FileStorage.__objects[key] = obj_instance
