import json
from os.path import isfile


class FileStorage:
    __file_path = "file.json"
    __object = {}

    def all(self):
        return FileStorage.__object

    def new(self):
        key ="{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        serialized_objects = {key: obj.to_dict() for key, obj in FileStorage.__object
        with open(FileStorage.__file_path, 'w') as file:
                              json.dump(serialised_objects, file)

    def reload(self):
        if isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    class_obj = globals()[class_name]
                    obj_instance = class_obj(**value)
                    FileStorage.__objects[key] = obj_instance
