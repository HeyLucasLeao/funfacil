import csv

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
