import os


def find_pipfile(start_path="packages"):
    for dirpath, _, filenames in os.walk(start_path):
        if 'Pipfile.lock' in filenames:
            return dirpath
    return None


def find_managepy():
    py_dir = find_pipfile()
    for dirpath, _, finames in os.walk(py_dir):
        if "manage.py" in finames:
            return dirpath

    return None
