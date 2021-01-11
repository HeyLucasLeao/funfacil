import csv
import pickle
import json

from dataclasses import dataclass


@dataclass
class GenericClass:
    id: str
    name: str
    email: str


def csv_to_class(path, encoding):
    arr = []

    with open(path, encoding=encoding) as file:
        to_read = csv.reader(file)
        for line in to_read:
            id, name, email = line

            line = GenericClass(id, name, email)
            arr.append(line)
    return arr


def obj_to_pickle(arr, path):
    with open(path, mode='wb') as file:
        pickle.dump(arr, file)
    return f'the file has been pickled. You can look at the PATH: ({path})'


def pickle_to_class(path):
    with open(path, mode='rb') as file:
        data = pickle.load(file)
    return data


def obj_to_json(obj, path):
    with open(path, mode='w') as file:
        json.dump(obj, file, default=_dict_to_json)


def _dict_to_json(obj):
    obj.__dict__


def json_to_obj(path):
    with open(path) as file:
        arr_dict = json.load(file)
