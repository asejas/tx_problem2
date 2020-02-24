import json


def load_students_from_file(file_path):
    """Load a Student list from a json file path(file_path)"""
    with open(file_path) as studentsFile:
        return load_data_set(studentsFile, 'Students')


def load_classes_from_file(file_path):
    """Load a Clas list from a json file path(file_path)"""
    with open(file_path) as classesFile:
        return load_data_set(classesFile, 'Classes')


def load_data_set(file, type_name):
    """Load a Element (type_name) list from a json file (file)"""
    elements = json.load(file)
    print('{}: {}'.format(type_name, elements))
    return elements
