import os


def fullpath(path):
    return os.path.normpath(os.path.join(os.path.dirname(__file__), path))
