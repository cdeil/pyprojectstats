from .core import BaseFile
from .cython import CythonFile
from .notebook import NotebookFile
from .python import PythonFile
from .rst import RSTFile


FILETYPES = [CythonFile, NotebookFile, PythonFile, RSTFile]


class UnknownFile:
    pass


def make_file(path):
    for filetype in FILETYPES:
        if path.suffix[1:] in filetype.extensions:
            return filetype(path)
    return UnknownFile(path)
